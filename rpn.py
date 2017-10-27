#!/usr/bin/env python3

def add(arg1, arg2):
	return arg1 + arg2

def subtract(arg1, arg2):
	return arg1 - arg2

def multiply(arg1, arg2):
	return arg1 * arg2

def divide(arg1, arg2):
	return arg1 / arg2

ops = {
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide    } 

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = ops[token]
			result = function(arg1, arg2)
			stack.append(result)
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()

