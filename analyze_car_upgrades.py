#Import necessary libraries
import pandas as pd

#Read in the data from the car_upgrades file
cars_df = pd.read_csv('./car_upgrades', index_col=0)

#Clean and analyze the data
cars_df = cars_df.dropna()
cars_df['Total_Cost_of_Upgrades'] = cars_df.sum(axis=1)

#Save the results to a text file
cars_df.to_csv('./car_upgrades_analysis.txt')