#!/usr/bin/env python3

import subprocess

output = subprocess.run(['find', '/', '-name', 'api_access_tokens.csv'], stdout=subprocess.PIPE).stdout.decode()

if output:
    output = output.split('\n')[:-1]
    results = []
    for line in output:
        tokens_loc = line
        with open(tokens_loc, 'r') as f:
            contents = f.read()
            if 'api_key' in contents and 'api_secret' in contents:
                print('Valid API credentials in:', tokens_loc)
            else:
