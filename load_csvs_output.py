# Importing the necessary libraries
import os
import io
import csv
import pandas as pd

# Create a console command to list all CSV files in the 'car_upgrades' directory
command = 'for %i in (car_upgrades*.csv) do @echo %~ni.csv'

# Execute the console command and capture the output
output = os.popen(command).read()

# Create a stream for CSV parsing using the 'io.StringIO' module
stream = io.StringIO(output)

# Load the CSVs into dataframes using the 'pandas.read_csv' function
frames = []
for filename in csv.reader(stream):
    df = pd.read_csv(os.path.join('car_upgrades', filename[0]), index_col=False, header=0)
    frames.append(df)

# Concatenate the dataframes into a single consolidated dataframe using the 'pandas.concat' method
consolidated_df = pd.concat(frames)

# Print the consolidated dataframe
print(consolidated_df.head())