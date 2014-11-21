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


# More examples of decorator within python

def p_decorate(func):
	def func_wrapper(name):
		return "<p>{0}</p>".format(func(name))

	return func_wrapper

def strong_decorate(func):
	def func_wrapper(name):
		return "<strong>{0}</strong>".format(func(name))

	return func_wrapper

def div_decorate(func):
	def func_wrapper(name):
		return "<div>{0}</div>".format(func(name))

	return func_wrapper

@div_decorate
@strong_decorate
@p_decorate

def new_get_text(name):
	return "lorem ipsum, {0} dolor sit amet".format(name)

print new_get_text("Samir")

# Here the order of setting oir decorator does matter and is goes top down

# A better way instead of defining 3 differnt functions, use a tag.

from functools import wraps

def tags(tag_name):
	def tags_decorator(func):
		@wraps(func)
		def func_wrapper(name):
			return "<{0}>{1}</{0}>".format(tag_name, func(name))

		return func_wrapper
	return tags_decorator

@tags("p")

def newest_get_text(name):
	"""returns some text"""
	return "Hello " +name

print newest_get_text("Samir")
print newest_get_text.__doc__
print newest_get_text.__name__
print newest_get_text.__module__
print "This is the site where this exercise was picked from"

print

print "http://thecodeship.com/patterns/guide-to-python-function-decorators/"
