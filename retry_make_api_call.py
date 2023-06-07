import json
import time

import requests


def retry_make_api_call(url, endpoint, method, max_retries=3, timeout=120):
    for i in range(max_retries):
        print(f"attempt {i + 1}...")
        try:
            response = requests.request(method, url=url + endpoint)
            response.raise_for_status()
            json_data = json.loads(response.text)

            return json_data

        except requests.exceptions.Timeout as err:
            print(err)
            time.sleep(timeout)

        except requests.exceptions.RequestException as err:
            print(err)
            break


url = 'https://www.edmunds.com'
endpoint = '/bmw/3-series/2020/st-401828691/features-specs/'
method = 'GET'
data = retry_make_api_call(url=url, endpoint=endpoint, method=method)
with open('bmw_specifications_api_response.json', 'w') as f:
    json.dump(data, f)
