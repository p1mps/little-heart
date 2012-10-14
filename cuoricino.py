#!/usr/bin/python
import time
import sys

while True:
	t = int(round(time.time()*10)) % 50
	a = ""
	for i in range(1,t):
		a+=" "

	a+="<3"
	
	for i in range(1,50 - t):
		a+=" "
	sys.stdout.write("\r%s" %a)	
	sys.stdout.flush()
	
	#sys.stdout.flush()