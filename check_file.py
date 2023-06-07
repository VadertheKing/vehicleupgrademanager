import os

if os.path.exists('car_upgrades/car_upgrade_prices.txt'):
    with open('car_upgrades/car_upgrade_prices.txt', 'r') as f:
        print(f.read())
else:
    print('File does not exist.')