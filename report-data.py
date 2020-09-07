# read data from williams-covid-data.txt and print a
# nice report based on it.

import sys

path = "/home/jellert/Documents/proj/williams-covid-check/"
fname = "williams-covid-data.txt"

file = open(path+fname, 'r')
line = file.read()
data = line.split(',')


last_24_hrs = int(data[0])
week_cases = int(data[1])
week_tests = int(data[2])
week_rate = week_cases/week_tests
# convert week rate into percentage w/ hundredths of a percent
week_rate *= 100
week_rate = round(week_rate, 2)

print("There were " + str(last_24_hrs) + " new cases yesterday.")
print(str(week_rate) + "% of tests came back positive this week.")
