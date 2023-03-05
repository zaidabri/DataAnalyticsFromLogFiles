import csv
from datetime import datetime

log_files = [
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.1.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/traintrack-EosprintApi.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.2.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.2-1.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/georg-EosprintApi.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.2-2.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/logging-http-server-two-prints.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.3.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator-fms.4.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.4.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/FMS-S3-S1--aggregator.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.5.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/EOSPRINT-app-EosprintApi.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/EOSPRINT.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/EosprintApi.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.us-exchange.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.6.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator-two-prints-week2.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.7.log",
    
]

for log_file in log_files:
    with open(log_file, "r") as data:
        output_file = log_file.replace(".log", ".csv").split("/")[-1]  # Get the original filename
        with open(output_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Data", "Hour", "Type", "Message", "Time", "Time formatted"])
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