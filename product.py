
# Super Class Product with functionality
class Product:

	def __init__(self, env, name, cost, recipe):
		self.name = name
		self.cost = cost
		self.recipe = recipe
		self.stepDone = env.event()

		self.state = -1


	# Start process to work trough recipe
	def startCreation(self):
		while self.state < len(self.recipe):
			self.nextStep()
			yield self.stepDone


	# Add Product to queue of next machine in recipe
	def nextStep(self):
		self.state += 1

		if(self.state < len(self.recipe)):
			self.recipe[self.state].addProduct(self)
		else:
			self.stepDone.succeed()


	def __repr__(self):
		return self.name


	def __str__(self):
		return self.name + '; ' + str(self.cost) + '$; Recipe: ' + str(self.recipe) + '; Current State: ' + str(self.state)


# Subclass with Sugar Donut definitions
class SugarDonut (Product):

	def __init__(self, env, machines):
		name = 'Sugar Donut'
		cost = 1
		recipe = [machines[1], machines[2], machines[3], machines[4]]

		super().__init__(env, name, cost, recipe)