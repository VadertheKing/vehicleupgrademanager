# -*- coding: utf-8 -*-

import json


def update_upgrade_list(event: dict, context: dict) -> dict:
    #### READ ##########
    with open('formatted_text_file.txt', 'r') as f:
        data = f.read()
        keyWords = ['Exhaust', 'Suspension', 'Engine']
        upgrades = {}
        for keyword in keyWords:
            # For each category, retrieve all text between the category name and next category name
            if keyword == keyWords[0]:
                upgrades[keyword] = data
            else:
                upgrades[keyword] = \
                data.split(f'{keyword}:', 1)[-1].split(f'{keyWords[keyWords.index(keyword) + 1]}:', 1)[0]

    ###### ANALYZE ########
    bmw_330i_xdrive_upgrade_options_3 = {}
    upgradeTypes = ["exhaust", "suspension", "engine"]
    for upgradeType in upgradeTypes:
        budget_levels = ['low', 'mid', 'high']
        upgrade_options = []
        for level in budget_levels:
            data = upgrades[upgradeType]
            if level == 'low':
                budget = '$0 - $500'
            elif level == 'mid':
                budget = '$500 - $1500'
            else:
                budget = '>$1500'
            options = [option.strip() for option in data.split(f'{budget}:')[1].split('\n') if option != ''][:-1]
            for option in options:
                opt = option.split('$')
                title = opt[0].strip()
                price = int(opt[1].strip().replace(',', '').replace('+', ''))
                upgrade_options.append({
                    'title': title,
                    'price': price,
                    'budget': budget,
                    'type': upgradeType
                })

        bmw_330i_xdrive_upgrade_options_3[upgradeType] = upgrade_options

    with open('bmw_330i_xdrive_upgrade_options_3.json', 'w') as f:
        json.dump(bmw_330i_xdrive_upgrade_options_3, f)


if __name__ == "__main__":
    update_upgrade_list({}, {}))
