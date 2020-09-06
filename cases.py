# a script that checks the williams covid dashboard
# for case and testing data

import requests

URL = 'https://www.williams.edu/coronavirus/dashboard/'
page = requests.get(URL)
text = page.text
lines = text.split('\n')
print(lines[514])
