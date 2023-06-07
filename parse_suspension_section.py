# Importing necessary libraries

import re

from bs4 import BeautifulSoup

# Reading the HTML content of the file
with open('suspension_section.html') as file:
    content = file.read()

# Parsing the HTML file
soup = BeautifulSoup(content, 'lxml')

# Extracting the recommended suspension setups for the BMW model specified
recommended_setups = []
for section in soup.find_all('tr', {'class': re.compile('tire-results-item')})[:3]:
    recommendations = section.find_all('a', {'class': 'make-vehicle-link'})[0].text
    recommended_setups.append(recommendations)

print(recommended_setups)
