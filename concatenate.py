import os

files = os.listdir('')

content = ''
for file in files:
    with open('./car_upgrades/' + file, 'r') as f:
        content += f.read()

with open('./car_upgrades/concatenated.txt', 'w') as f:
    f.write(content)
