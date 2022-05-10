
class Product:

	def __init__(self, name, cost, recipe):
		self.name = name
		self.cost = cost
		self.recipe = recipe
		
		self.state = -1

	def nextStep(self):
		self.state += 1

		if(self.state < len(self.recipe)):
			self.recipe[self.state].addProduct(self)
		else:
			print('Done!')

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name + '; ' + str(self.cost) + '$; Recipe: ' + str(self.recipe) + '; Current State: ' + str(self.state)



class SugarDonut (Product):

	def __init__(self, machines):
		self.name = 'Sugar Donut'
		self.cost = 1
		self.recipe = [machines[1], machines[2], machines[3], machines[4]]
		
		self.state = -1