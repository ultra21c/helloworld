#!/usr/bin/env python

import sys
import lib.send

def print_helloworld():
	print 'hello world'

def calc(num):
	sum = 0
	for i in range(num):
		sum+=i
	print sum

def help():
	print 'python %s'%sys.argv[0]
		
def main(name):
	print 'hello world'
	lib.send.echo('my prog name is %s'%name)
	calc(10)
	help()

if __name__ == '__main__':
	name = sys.argv[0]
	main(name)
