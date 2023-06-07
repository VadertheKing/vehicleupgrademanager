# Import necessary libraries
import pandas as pd

# Upload BMW 330i specs sheet data
bmw_330i_specs = pd.read_csv('bmw_330i_specs.csv')

# Filter data to focus on engine, suspension, and exhaust-related specifications
e_specs = bmw_330i_specs[['Engine Type', 'Fuel System', 'Valves', 'Horsepower (hp)', 'Torque (ft-lbs)', 'Gears', 'Front Suspension Type', 'Rear Suspension Type', 'Anti-lock Brakes']]

# Determine ranges for each specification
valves_range = pd.IntervalIndex.from_breaks([0, 2, 4, 6, 8], closed='left')
horsepower_range = pd.IntervalIndex.from_breaks([0, 200, 300, 400, 500], closed='left')
torque_range = pd.IntervalIndex.from_breaks([0, 250, 350, 450, 550], closed='left')
gears_range = pd.IntervalIndex.from_breaks([3, 4, 5, 6, 7], closed='left')

# Upgrade option categories
engine_upgrade_options = {'low': ['Cold Air Intake System Air Filter', 'High Performance Air Filter', 'Performance Chips'], 'mid': ['Exhaust Headers', 'High Performance Fuel Pump', 'Performance Camshaft'], 'high': ['Supercharger Kit', 'Turbocharger Kit', 'Nitrous Oxide System']}
suspension_upgrade_options = {'low': ['Springs', 'Struts and Shocks', 'Sway Bars'], 'mid': ['Coilovers', 'Lift Kits', 'Lowering Kits'], 'high': ['Air Suspension', 'Body Kits', 'Camber Plates']}
exhaust_upgrade_options = {'low': ['Cat-Back Exhaust Kit', 'Performance Muffler', 'Exhaust Tips'], 'mid': ['Mid-Pipe', 'Long-Tube Headers', 'Down-Pipe'], 'high': ['Turbo-Back Exhaust Kit', 'Header-Back Exhaust Kit', 'Axle-Back Exhaust Kit']} 
