#!/usr/bin/env python

import sys
import lib.send

def print-helloworld():
	print 'hello world'

def main(name):
	print 'hello world'
	lib.send.echo('my prog name is %s'%name)

if __name__ == '__main__':
	name = sys.argv[0]
	main(name)
