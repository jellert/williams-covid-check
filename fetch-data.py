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
# print(text)
lines = text.split('\n')

# look for the correct place to start
dataStart = 0
for i in range(len(lines)):
    # the stat tags are only used around the stats (go figure)
    if "<div class=\"stat\">" in lines[i]:
        dataStart = i
        break
if dataStart == 0:
    # somehow it didn't work?
    print("Oops")
    exit()


dataHTML = ["" for i in range(5)]
for i in range(4):
    dataHTML[i] = lines[dataStart+4*i]
data = list(map(strip_div, dataHTML))
# thanks to John Coleman for the elegant way to remove commas
# https://stackoverflow.com/questions/37662555/valueerror-invalid-literal-for-int-with-base-10
data[3] = ''.join(c for c in data[3] if c.isnumeric())
data[4] = ''.join(c for c in data[4] if c.isnumeric())

file = open(path+fname, 'w')
file.write(data[0]+','+data[1]+','+data[2]+','+data[3]+','+data[4])
file.close()
