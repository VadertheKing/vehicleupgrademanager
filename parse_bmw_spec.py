import re
import pandas as pd
from io import StringIO
from typing import Tuple
from PyPDF2 import PdfFileReader
from collections import defaultdict


def extract_text(file_path: str) -> str:
    with open(file_path, mode='rb') as file:
        reader = PdfFileReader(file)
        contents = []
        for page in reader.pages:
            contents.append(page.extract_text())
        return ''.join(contents)


def extract_list(regex_str: str, text: str) -> list:
    pattern = re.compile(regex_str, re.IGNORECASE)
    matches = pattern.findall(text)
    return [match[0] for match in matches]


def extract_specs(file_path: str, specs: Dict[str, Tuple[str, str]]) -> Dict[str, list]:
    text = extract_text(file_path).replace('\n', '')
    extracted_data = defaultdict(list)
    for key, val in specs.items():
        regex_str = fr'{val[0]}{val[1]}'
        extracted_data[key] = extract_list(regex_str, text)
    return extracted_data


if __name__ == '__main__':
    # Regular Expressions for extracting engine, suspension, and exhaust system upgrades
    engine_regex = ('POWERTRAIN', r':(.+?)@.*
.+
(.+?)
.+HP.+RPM
T.+MPH')
    suspension_regex = ('CHASSIS', r':
(.+?)
.+Stabilizer Bars (.+?)
.+Rear Axle (.+?)
.+Suspension Type')
    exhaust_regex = ('PERFORMANCE', r'
(.+?)
.+SOUND
(.+?)
.+TIP STYLE
(.+?)
')
    # Dictionary containing the specs and their associated regex patterns
    specs = {'engine': engine_regex, 'suspension': suspension_regex, 'exhaust': exhaust_regex}
    # Extract specs and append to separate lists
    extracted_data = extract_specs('BMW 3 Series 330i xDrive Sedan 2022.pdf', specs)
    engine_upgrades = extracted_data['engine']
    suspension_upgrades = extracted_data['suspension']
    exhaust_upgrades = extracted_data['exhaust']
    # Display the extracted data in a Pandas DataFrame
    data = {
        'Engine Upgrades': engine_upgrades,
        'Suspension Upgrades': suspension_upgrades,
        'Exhaust Upgrades': exhaust_upgrades
    }
    df = pd.DataFrame(data)
    print(df)
    # Output the data to a CSV file
    df.to_csv('bmw_upgrades.csv')