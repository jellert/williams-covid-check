# williams-covid-check
A simple set of scripts for fetching Williams College Covid-19 statistics and displaying them.

## Usage
The website is updated at some time every morning, I'm not sure when.
I am operating under the assumption that it's done before 9am,
but if not I can change that.

The way these scripts work is that `fetch-data.py` will grab
the data from the webpage and write the 4 stats to a
file in the same directory called
`williams-covid-data.txt`. The script `report-data.py` reads
from that file and uses those numbers to calculate test positivity
rate, and then prints new cases in the last 24 hours and
weekly test positivity rate to stdout (in complete sentences
for readability). If you want to see different things printed,
you can edit `report-data.py`, and if you want to store the raw
data differently, edit `fetch-data.py` (and probably update the file
path in `report-data.py`).

### My setup
I have `cron` running `fetch-data.py` every morning at 9am, but again
this time can be changed if it seems the website isn't updated by then
To set this yourself, run `crontab -e`, 
and then add the line
```
0 9 * * * python3 /PATH/TO/fetch-data.py
```
to that file.

I have the alias `covidreport` set for running `report-data.py`
so I can run it whenever I want, and have also modified
my shell config so it runs on startup.
