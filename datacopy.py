import csv
from datetime import datetime

log_files = [
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.1.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/traintrack-EosprintApi.log",
]

# Define the words to search for
search_words = ['error', 'warning', 'FAILURE', 'SUCCESS']

# Create a new CSV file to store the percentage data
with open('percentages.csv', 'w', newline='') as percentages_file:
    writer = csv.writer(percentages_file)
    writer.writerow(['File', 'Word', 'Percentage'])

    for log_file in log_files:
        with open(log_file, "r") as data:
            output_file = log_file.replace(".log", ".csv").split("/")[-1]  # Get the original filename
            with open(output_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Data", "Hour", "Type", "Message", "Time", "Time formatted"])
                word_count = {word: 0 for word in search_words}  # Initialize the count of each word to 0
                total_rows = 0  # Initialize the count of total rows to 0
                for line in data:
                    try:
                        date, type_and_message = line.split("] [")
                        date = date[1:]
                        day, hour = date.split(" ")
                        time_str = day + " " + hour
                        time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
                        type_, message = type_and_message.split("] ")
                        writer.writerow([day, hour, type_, message, time_str + ", " + str(time), time.date().strftime("%Y-%m-%d") + "  " + time.time().strftime("%H:%M:%S.%f")])
                    except ValueError:
                        try:
                            date, message = line.split("] ")
                            date = date[1:]
                            day, hour = date.split(" ")
                            time_str = day + " " + hour
                            time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
                            type_ = "N/A"
                            if line.strip():  # Check if the line is not empty
                                writer.writerow([day, hour, type_, message, time_str + ", " + str(time), time.date().strftime("%Y-%m-%d") + "  " + time.time().strftime("%H:%M:%S.%f")])
                            else:
                                print(f"Empty line: {line}")
                        except ValueError:
                            if line.strip():  # Check if the line is not empty
                                writer.writerow(["", "", "", line.strip(), "", "", ""])
                            else:
                                print(f"Empty line: {line}")
                    # Count the occurrences of each word in the line
                    for word in search_words:
                        if word in line:
                            word_count[word] += 1
                    total_rows += 1
                # Calculate the percentage of rows containing each word
                word_percentages = {word: word_count[word] / total_rows * 100 for word in search_words}
                # Write the results to a new row in the percentages CSV file
                for word in search_words:
                    writer.writerow(['', '', word, f"{word_percentages[word]:.2f}%"])
        #