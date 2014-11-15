import time
from abc import ABCMeta, abstractmethod
import datetime

class Subject(object):
	def __init__(self):
		self.observers = [] # Initialize the list of observers as empty.
		self.curr_time = None # No value for curr time

	# define the method for registering observers
	def register_observer(self, observer):
		if observer in self.observers:
			print observer, 'already in subscribed observer'
		else:
			self.observers.append(observer)

	# define the method to un-register the observer
	def unregister_observer(self, observer):
		try:
			self.observers.remove(observer)
		except ValueError:
			print 'No such observer in the subject'

	# Method to notify the observer in case of changed events
	# Takes in only the self object.
	# notify() is an abstract method defined in the below function.
	def notify_observer(self):
		self.curr_time = time.time()
		for observer in self.observers:
			#observer.notify(self.curr_time)
			observer.notify(self)

class Observer(object):
	"""Abstract class for observer, provides notify method as interface
	for the subjects"""

	# This is inheriting the Metaclass into the class definition.
	# It is a class of a class. It defines how the class behaves.
	# A class is a instance of a metaclass.
	__metaclass__ = ABCMeta
	@abstractmethod

	def notify(self, unix_timestamp):
		pass

# Now we implement the notify method in the concrete class for Observer

class USATimeObserver(Observer):
	def __init__(self, name):
		self.name = name

	def notify(self, unix_timestamp):
		time = datetime.datetime.fromtimestamp(int(unix_timestamp.curr_time)).strftime('%Y-%m-%d %I:%M:%S%p')
		print 'Observer', self.name, 'says:', time

class EUTimeObserver(Observer):
	def __init__(self, name):
		self.name = name


	def notify(self, unix_timestamp):
		time = datetime.datetime.fromtimestamp(int(unix_timestamp.curr_time)).strftime('%Y-%m-%d %H:%M:%S')
		print 'Observer', self.name, 'says:', time


# Define the main class, where we register the Observers to the subject.

if __name__ == '__main__':
	subject = Subject()
	print 'Adding usa_time Observer'
	observer1 = USATimeObserver('usa_time_observer')
	subject.register_observer(observer1)
	subject.notify_observer()

	time.sleep(2)

	print 'Adding eu_time_observer'
	observer2 = EUTimeObserver('eu_time_observer')
	subject.register_observer(observer2)
	subject.notify_observer()

	time.sleep(2)
	print 'Removing usa_time_observer'

	subject.unregister_observer(observer1)
	subject.notify_observer()

