#function to get upgrade details

def get_upgrade_details(file_contents: str) -> Tuple:
    upgrade = None
    price = None

    #parse the contents of the file to retrieve upgrade name and price
    for line in file_contents.split('\n'):
        tokens = line.strip().split(':')
        if len(tokens) != 2:
            continue
        key, value = tokens
        if key == 'upgrade':
            upgrade = value
        elif key == 'price':
            price = int(value.strip('$'))
    return (upgrade, price)


#loop over all files in the car_file_list directory and generate a dictionary of car upgrades and their prices
all_upgrades = {}
for car_file_path in car_file_path_list:
    with open(car_file_path) as f:
        contents = f.read()
        upgrade, price = get_upgrade_details(contents)
        all_upgrades[upgrade] = price

#write dictionary to file
with open('car_upgrade_prices.txt', 'w') as f:
    f.write(str(all_upgrades))