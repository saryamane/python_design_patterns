import types

class StrategyExample(object):

	def __init__(self, func=None):
		self.name = 'Main Strategy'
		if func:
			self.execute = types.MethodType(func, self, StrategyExample)
			# This one checks if the method type is a StrategyExample child.

	def execute(self):
		print "Original execution"

def executeReplacement1(self):
	print self.name + "Strategy 1"

def executeReplacement2(self):
	print self.name + "Strategy 2"

def strategy_add(a,b):
	return a + b

def strategy_minus(a,b):
	return a - b


if __name__ == "__main__":
	strat0 = StrategyExample()
	strat1 = StrategyExample(executeReplacement1)
	strat1.name = 'Coming from 1: '
	strat2 = StrategyExample(executeReplacement2)
	strat2.name = 'Coming from 2: '

	strat0.execute()
	strat1.execute()
	strat2.execute()

	solver = strategy_add
	print solver(2,5)
	solver = strategy_minus
	print solver(10,4)