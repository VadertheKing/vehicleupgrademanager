# Define script to parse contents of car upgrades list file and return list of file names

def parse_car_file_list(file_contents: str) -> List[str]:
    # Split list of filenames
    filenames = file_contents.split('\n')
    # Remove any empty filenames
    res = [f.strip() for f in filenames if f.strip()]
    return res


def get_file_list(directory: str) -> List[str]:
    # Get list of files in directory
    try:
        with os.scandir(directory) as dir_entries:
            files = [entry.name for entry in dir_entries if entry.is_file()]
    except:
        files = []
    return files


# Parse file containing car upgrades list
upgrades_filename = 'car_upgrades_list.txt'
with open(upgrades_filename) as f:
    car_file_contents = f.read()

car_file_list = parse_car_file_list(car_file_contents)
car_file_path_list = []

for car_file in car_file_list:
    # Get path of car upgrade file
    car_file_path = os.path.join('car_upgrades', car_file)

    # Sanity check to see if file exists
    if os.path.isfile(car_file_path):
        car_file_path_list.append(car_file_path)

# Write car upgrade file paths to file for future reference
with open('car_file_list.txt', 'w') as f:
    f.writelines('
'.join(car_file_path_list))