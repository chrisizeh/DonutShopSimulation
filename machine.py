
class Machine:

	def __init__(self, id, name, workTime):
		self.name = name
		self.workTime = workTime

		self.queue = []

	def addProduct(self, product):
		self.queue.append(product)

	def nextProduct(self):
		if(len(self.queue) > 0):
			current = self.queue.pop(0)
			current.updateState()
		else:
			print('Nothing to do!')

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name + '; ' + str(self.workTime) + ' min; Queue: ' + str(self.queue)
