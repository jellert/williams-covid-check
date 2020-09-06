# a script that checks the williams covid dashboard
# for case and testing data

import requests
import sys

path = "/home/jellert/Documents/proj/williams-covid-check/"
fname = "williams-covid-data.txt"

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
# thanks to John Coleman for the elegant way to remove commas
# https://stackoverflow.com/questions/37662555/valueerror-invalid-literal-for-int-with-base-10
data[2] = ''.join(c for c in data[2] if c.isnumeric())
data[3] = ''.join(c for c in data[3] if c.isnumeric())

file = open(path+fname, 'w')
file.write(data[0]+','+data[1]+','+data[2]+','+data[3])
file.close()
