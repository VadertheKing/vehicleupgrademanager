import json

import pandas as pd

url = 'https://www.caranddriver.com/bmw/3-series/specs/2020/bmw_3-series_bmw-3-series-sedan_2020'
df = pd.read_html(url)
specs = df[0].set_index(0).squeeze().to_dict()
with open('specs.json', 'w') as file:
    json.dump(specs, file)
