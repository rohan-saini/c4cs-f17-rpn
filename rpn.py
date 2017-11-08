#!/usr/bin/env python3
import readline

#operators
def add(arg1, arg2):
	return arg1 + arg2

def subtract(arg1, arg2):
	return arg1 - arg2

def multiply(arg1, arg2):
	return arg1 * arg2

def divide(arg1, arg2):
	return arg1 / arg2

def exp(arg1, arg2):
	return arg1**arg2

ops = {
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide,
	'^': exp      } 

def calculate(arg):
	# type 'q', then quit rpn program
	if arg == 'q':
		exit()
	# initialize stack
	stack = list()

	# perform calculations based on user input
	for token in arg.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = ops[token]
			result = function(arg1, arg2)
			stack.append(result)
	
	print(result)
	return result
	
def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()

