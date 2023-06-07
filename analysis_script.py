# Import libraries
import pandas as pd

# Read car upgrade files
file_names = ['bmw_engine_specs.txt', 'audi_engine_specs.txt', 'jeep_engine_specs.txt']
file_data = []
for file_name in file_names:
    with open("./car_upgrades/" + file_name, 'r') as f:
        file_data.append(f.read())

# Merge data into single dataframe
data = pd.concat([pd.read_csv(pd.compat.StringIO(file)) for file in file_data])

# Analyze data
data_analyses = []

# Top 5 cars with most horsepower
data_analyses.append(data[['Make', 'Model', 'Horsepower']].sort_values('Horsepower', ascending=False).head())

# Average torque by make
data_analyses.append(data[['Make', 'Torque']].groupby('Make').mean())

# Top 5 cars with best gas mileage
data_analyses.append(data[['Make', 'Model', 'City mpg', 'Highway mpg']].assign(total_mpg=lambda df: df['City mpg'] + df['Highway mpg']).sort_values('total_mpg', ascending=False).drop('total_mpg', axis=1).head())

for analysis in data_analyses:
    print(analysis)