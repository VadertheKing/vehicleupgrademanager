from bs4 import BeautifulSoup

with open('bmw_specs.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

specs_table = soup.find('table', id='engine-specs')
rows = specs_table.find_all('tr')

engine_details = {}

for row in rows:
    if row.th:
        key = row.th.text.strip().replace(' ', '_').lower()
        if key == 'fuel_economy':
            engine_details[key] = {}
    elif row.td:
        if 'data-specname' in row.td.attrs:
            key = row.td.attrs['data-specname'].strip().replace(' ', '_').lower()
            value = row.td.text.strip()
            if key == 'fuel_economy':
                fuel_key = value.split(maxsplit=1)[0].lower()
                fuel_value = value.split(maxsplit=1)[1].lower()
                engine_details[key][fuel_key] = fuel_value
            else:
                engine_details[key] = value

print(engine_details)
