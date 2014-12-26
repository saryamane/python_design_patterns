import time

class Subject(object):
	def __init__(self):
		self.observers = [] # Initialize the list of observers as empty.
		self.curr_time = None # No value for curr time

	# define the method for registering observers
	def register_observer(self, observer):
		if observer in self.observer:
			print observer, 'already in subscribed observer'
		else:
			self.observer.append(observer)

	# define the method to un-register the observer
	def unregister_observer(self, observer):
		try:
			self.observer.remove(observer)
		except ValueError:
			print 'No such observer in the subject'

	# Method to notify the observer in case of changed events
	# Takes in only the self object.
	# notify() is an abstract method defined in the below function.
	def notify_observer(self):
		self.curr_time = time.time()
		for observer in self.observer:
			observer.notify(self.curr_time)