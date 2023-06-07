import sys

sys.path.insert(1, '../auto_gpt_workspace/upgrade_options/')

from find_best_options import find_best_options
from engine_upgrades import engine_upgrades
from suspension_upgrades import suspension_upgrades
from exhaust_upgrades import exhaust_upgrades

specs_file = read_file('bmw_330i_xdrive_sedan_spec_sheet.txt')

engine_categories = ['air intake system', 'exhaust system', 'engine tune', 'turbocharger upgrade']
suspension_categories = ['springs', 'shocks', 'suspension arms', 'sway bars', 'coil overs']
exhaust_categories = ['cat-back exhaust', 'downpipe', 'muffler', 'exhaust tip']

engine_upgrades_best = find_best_options(specs_file, engine_categories, engine_upgrades)
suspension_upgrades_best = find_best_options(specs_file, suspension_categories, suspension_upgrades)
exhaust_upgrades_best = find_best_options(specs_file, exhaust_categories, exhaust_upgrades)

print(engine_upgrades_best)
print(suspension_upgrades_best)
print(exhaust_upgrades_best)
