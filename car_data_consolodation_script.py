import json

# Create dictionary of relevant fields to use
# to consolidate and organize data

keys = ['make', 'model', 'engine', 'suspension', 'exhaust']
my_data = {}

# Read data from 'car_upgrade_data.txt' file
f = open('car_upgrade_data.txt', 'r')
data = f.readlines()
f.close()

# Consolidate data
for line in data:
	temp_data = line.strip().split(':')
	key = temp_data[0].strip()
	if key in keys:
		my_data[key] = temp_data[1].strip()

# You can use the 'browse_website' command to get more
# data about your car and add them to the my_data dictionary

with open('car_data.json', 'w') as fp:
    json.dump(my_data, fp, indent=4)