# Necessary imports
import requests
from bs4 import BeautifulSoup

# The web page to be loaded
webpage = requests.get('https://www.bmwusa.com/vehicles/3-series/sedan/330i-xdrive')
soup = BeautifulSoup(webpage.content, 'html.parser')
