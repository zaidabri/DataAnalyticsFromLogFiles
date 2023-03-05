import csv

log_files = [
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator-fms.4.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator-two-prints-week2.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.1.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.2-1.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.2-2.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.2.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.3.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.4.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.5.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.6.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.7.log",
    "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator.us-exchange.log",
  
]

for log_file in log_files:
    with open(log_file, "r") as data:
        output_file = log_file.replace(".log", ".csv")
        with open(output_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Data", "Hour", "Type", "Message"])
            for line in data:
                try:
                    date, type_and_message = line.split("] [")
                    date = date[1:]
                    day, hour = date.split(" ")
                    type_, message = type_and_message.split("] ")
                    writer.writerow([day, hour, type_, message])
                except ValueError:
                    try:
                        date, message = line.split("] ")
                        date = date[1:]
                        day, hour = date.split(" ")
                        type_ = "N/A"
                        writer.writerow([day, hour, type_, message])
                    except ValueError:
                        print(f"Could not parse line: {line}")