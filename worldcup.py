#!/usr/bin/env python

import json,requests,time
from termcolor import colored

today='http://worldcup.sfg.io/matches/today'
tomorrow='http://worldcup.sfg.io/matches/tomorrow'
def parse_data(url):
	response=requests.get(url)
	data=json.loads(response.text)
	for results in data:
		d=results['datetime'].split("T")[1].split("-")[0].split(":")[0]
		di=int(d)+4
		print '-----------------------------'
		print colored(str(di)+":00","red")+"\t|"+colored(results['home_team']['country'],"green")+" vs "+\
		colored(results['away_team']['country'],"blue")

# print time.strftime("%A %B %d %Y")
print "#############Today###############"
parse_data(today)
print "#############Tomorrow############"
parse_data(tomorrow)