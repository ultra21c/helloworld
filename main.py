#!/usr/bin/env python

import sys
import lib.send

def ilove_jiwoo():
	print 'i love jiwoo'
	print 'I want to earn a lot of money'

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
	ilove_jiwoo()

print 'hi'

if __name__ == '__main__':
	name = sys.argv[0]
	main(name)
