"""A script to read car info
"""

import inspect
import os

def get_bmw_specs():
    current_script_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    car_info_file_path = os.path.join(current_script_path, 'initialize_car_info.py')

    with open(car_info_file_path) as f:
        code = compile(f.read(), car_info_file_path, 'exec')
        exec(code, globals(), locals())
    del globals()['f']
    return BMW_330I_XDRIVE_SPECS
