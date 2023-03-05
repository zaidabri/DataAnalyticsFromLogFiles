import pandas as pd

log_files = [
    "/Users/zaidabrito/BTree/BTreeWork/polyData/logs/aggregator2.xlsx"
]

# Loop over each file in the list of log files
for file in log_files:
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(file)

    # Subtract the value of the last row first column from the second row first column
    result = df.iloc[1, 0] - df.iloc[-1, 0]

    # Save the result to a new Excel file
    result_df = pd.DataFrame({"Result": [result]})
    result_df.to_excel(f"{file}_result.xlsx", index=False)