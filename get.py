#! /usr/bin/python
#  coding = utf-8

import requests
import sys
import os
import time
from ThreadPool import ThreadPool

if len(sys.argv) != 3:
	print 'Usage:', sys.argv[0], 'p1 p2'
	print ' p1:\tDomain Name'
	print ' p2:\tHow many page will you to get'
	sys.exit()

result = []

for i in range(int(sys.argv[2])):
	url = 'http://www.baidu.com/s?pn={0}0&wd=site%3A{1}'.format(i, sys.argv[1])
	try:
		r = requests.get(url)
	except KeyboardInterrupt: 
		print ''
		sys.exit()
	except:
		continue
	page = r.content
	r.close()
	while True:
		index = page.find('<span class="g">')
		if index == -1:
			break
		page = page[index + 16:]
		s = page[:page.find('/')].strip()
		result.append(s)
		ts = s
		if len(ts) > 50:
			ts = ts[:47] + '...'
		ts = ' [ %-50s ] \r'%(ts)
		os.system('printf "' + ts + '"')
		time.sleep(0.02)
try:
	os.mkdir('output')
except:
	pass
result = list(set(result))
f = open('output/' + sys.argv[1], 'w')
for s in result:
	f.write(s + '\n')
f.close()
os.system('printf "' + '%60s\r'%'' + '"')
print 'OK!', str(len(result)), ' lines has gotten in output/', sys.argv[1]
