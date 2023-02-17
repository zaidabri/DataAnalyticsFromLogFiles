import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Initialize variables
total_records = 0
total_errors = 0
results = []

# Get the list of log files in the "TestingLogFiles" directory
log_files = os.listdir("TestingLogFiles")

# Iterate through each log file and process the data
for file_name in log_files:
    if file_name.endswith(".log"):
        # Open the log file and read the data
        with open(os.path.join("TestingLogFiles", file_name)) as f:
            lines = f.readlines()
            x = []
            y = []
            for line in lines:
                if line.startswith("X:"):
                    x.append(float(line.split()[1]))
                elif line.startswith("Y:"):
                    y.append(float(line.split()[1]))
                elif line.startswith("Error:"):
                    total_errors += 1
            # Create a graph using Matplotlib
            plt.plot(x, y)
            plt.title("Graph for {}".format(file_name))
            plt.xlabel("X")
            plt.ylabel("Y")
            # Save the graph as a PNG file
            plt.savefig("Graph_{}.png".format(file_name))
            plt.close()
            # Update the total number of records
            total_records += len(x)
            # Calculate the KPIs and append the results to the list
            result = {
                "File Name": file_name,
                "Number of Records": len(x),
                "Minimum X": min(x),
                "Maximum X": max(x),
                "Minimum Y": min(y),
                "Maximum Y": max(y),
                "Number of Errors": lines.count("Error:")
            }
            results.append(result)
            
# Calculate the KPIs and the percentage of errors
average_records = total_records / len(log_files)
error_percentage = total_errors / total_records * 100

# Write the results to an Excel file
df = pd.DataFrame(results)
df.to_excel("Results.xlsx", index=False)

# Display the KPIs and the percentage of errors
print("Average number of records per file: {:.2f}".format(average_records))
print("Percentage of errors in the data: {:.2f}%".format(error_percentage))
