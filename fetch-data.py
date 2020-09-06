# a script that checks the williams covid dashboard
# for case and testing data

import requests
import sys

# pulls out the text from between
# a <div> and a </div>.
# This assumes the tag and the end tag are on the same line,
# which they are for this specific application.
def strip_div(str):
    start = str.find('>')
    end = str.find('<',start)
    if start == -1 or end == -1:
        return "*NOT FOUND*"
    else:
        return str[start+1:end]

url = 'https://www.williams.edu/coronavirus/dashboard/'
page = requests.get(url)
text = page.text
lines = text.split('\n')
# pulling the relevant numbers from the HTML
# by referencing hard-coded line numbers.
# probably a bad idea but I don't expect them to
# change the website very much.
# otherwise, we can search for <div class="stat"> to find them.
dataHTML = ["" for i in range(4)]
for i in range(4):
    dataHTML[i] = lines[514+4*i]
data = list(map(strip_div, dataHTML))

last_24_hrs = int(data[0])
week_cases = int(data[1])
# thanks to John Coleman for the elegant way to get a comma out
# https://stackoverflow.com/questions/37662555/valueerror-invalid-literal-for-int-with-base-10
week_tests = data[2]
week_tests = ''.join(c for c in week_tests if c.isnumeric())
week_tests = int(week_tests)
week_rate = week_cases/week_tests
# convert week rate into percentage w/ hundredths of a percent
week_rate *= 100
week_rate = round(week_rate, 2)

file = open('williams-covid-data.txt', 'w')
file.write(str(last_24_hrs)+','+str(week_rate))
file.close()
