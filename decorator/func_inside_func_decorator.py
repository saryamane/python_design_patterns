#!/usr/bin/python

def greet(name):
	def get_message():
		return "Hello "

	result = get_message()+name
	return result

print greet("Samir")

def greet2(name):
	return "Hello " + name

def call_func(func):
	other_name = "Another function"
	return func(other_name)

print call_func(greet2)


# Functions can also return another functions.

def compose_greet_func():
	def get_message():
		return "Hello there!"

	return get_message

greet = compose_greet_func()
print greet()

# Inner functions can have access to the enclosing scope.
# They are commonly known as closure.