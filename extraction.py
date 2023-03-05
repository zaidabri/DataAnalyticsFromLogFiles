import csv

data_file = "/Users/zaidabrito/Documents/aa Thesis/polyline-trip-2023/aggregator-two-prints-week2.log"

with open("/Users/zaidabrito/BTree/BTreeWork/polyData/datanewnew.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Data", "Hour", "Type", "Message"])
    with open(data_file, "r") as data:
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