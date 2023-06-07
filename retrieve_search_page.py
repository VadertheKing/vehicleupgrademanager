import urllib.request

query = 'car upgrades'  # specify your Google search query here

search_query = 'https://www.google.com/search?q=' + query

try:
    html_content = urllib.request.urlopen(search_query).read()
    with open('search_results.html', 'wb') as f:
        f.write(html_content)
except:
    print('Error retrieving search results')
