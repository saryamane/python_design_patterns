#!/usr/bin/python

def get_text(name):
	return "loren ipsum, {0} dolor sit amet" .format(name)

def p_decorate(func):
	def func_wrapper(name):
		return "<p>{0}</p>".format(func(name))

	return func_wrapper

my_get_text = p_decorate(get_text)

print my_get_text("Samir")

print """This was our first decorator, where a function
takes another function as an argument, generates a new 
function, augmenting the work of the original function and 
returning the generated function so we can use it anywhere."""

# My first python decorator implemented here.

def italics(the_function_that_will_be_wrapped):
	def the_function_that_will_wrap():
		return '<i>' + the_function_that_will_be_wrapped() + '</i>'

	return the_function_that_will_wrap

@italics
def hello_world():
	return "Hello World!"

var = hello_world()
print var