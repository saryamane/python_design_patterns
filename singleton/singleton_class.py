#!/usr/bin/python

class Singleton(object):
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance


singleton = Singleton()
another_singleton = Singleton()

if singleton is another_singleton:
	print "Same object reference returned"
else:
	print "Singleton is not working, they both are different"

singleton.only_one_var = "I'm only one var"
print another_singleton.only_one_var

class Child(Singleton):
	only_one_var="Adding some child attributes"

child = Child()
if child is singleton:
	print "Child is same as singleton"
	print child.only_one_var
else:
	print "Child is not as same as singleton"
	print child.only_one_var