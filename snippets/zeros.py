from __future__ import division
from math import *

# Finds zeros in a function between bounds a and b via an iterative method

flist = []
sol = []
def sign(number):return cmp(number,0)

def getZero(func, a=None, b=None):
	if not 'flist' in globals(): 
		print "lol"
		global flist
		flist = []
		global sol
		sol = []
	if not (a == None and b == None): flist.append([a,b])
	nflist = []
	for section in flist:
		print "now trying interval: " + str(section)
		fa = eval(func.replace("x", str(section[0])))
		fb = eval(func.replace("x", str(section[1])))
		if -sign(fa) == sign(fb):
			interval = abs(section[1]-section[0])
			if interval < .001:
				sol.append(section[0])
			else:
				nflist.append([section[0], section[0] + .5*interval])
				nflist.append([section[1] - .5*interval, section[1]])
	flist = nflist
	if flist != []:
		getZero(func)
	if not (a == None and b == None): print str(sol)


getZero("cos(x)**2 - 2*sin(x/4)", 0, 2)
getZero("x**2 -2", -10, 10)


