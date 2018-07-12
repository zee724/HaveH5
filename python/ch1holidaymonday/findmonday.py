#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import datetime
import calendar
import json

def getMonday():
	oneday = datetime.timedelta(days = 1)

	#today = datetime.date.today()
	today = datetime.date(2017,12,31)

	while today != datetime.date(2019,1,1):
		today = today + oneday
		if(1==today.isoweekday()):
			print str(today) + ' ' + str(today.isoweekday())

#getMonday()

with open("cnholiday2018.json",'r') as load_f:
	load_dict = json.load(load_f)
for data in load_dict:
	theday = datetime.date(int(data['yy']),int(data['mm']),int(data['dd']))
	if(1 == theday.isoweekday()):
		print str(theday) + ' ' + '是国假星期一'