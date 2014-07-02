#!/usr/bin/env python

import sys
import lib.send

def calc(num):
	sum = 0
	for i in range(num):
		sum+=i
	print sum
		
def main(name):
	print 'hello world'
	lib.send.echo('my prog name is %s'%name)
	calc(10)

if __name__ == '__main__':
	name = sys.argv[0]
	main(name)
