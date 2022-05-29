from product import SugarDonut

# SimPy goes here

class DonutShop:

	def __init__(self, env, name, machines, creation_interval, ):
		self.env = env

		self.name = name
		self.machines = machines

		self.profit = 0
		self.donuts_created = 0
		self.creation_interval = creation_interval

	# Start creation process of donuts and add profit for finished donut
	def run_donut(self, env, donut):
	    self.donuts_created += 1
	    yield self.env.process(donut.startCreation())
	    self.profit += donut.cost
	    print('Time: ' + str(env.now) + '; Donut done; Profit: ' + str(self.profit))


	# Unlimited loop to create donuts after a specified wait time
	def create_donuts(self, env):
	    while True:
	        #create instance of activity generator
	        donut = SugarDonut(self.env, self.machines)
	        #run the activity generator for this donut
	        self.env.process(self.run_donut(env, donut))
	        #freeze till time next donut enters queue has passed
	        yield self.env.timeout(self.creation_interval)


	# Start an environment run with a fixed creation interval
	def start_shift(self, length):
		# Start working process for all machines
		for machine in self.machines.values():
		    self.env.process(machine.run())

		# Run process for a specified time
		self.env.process(self.create_donuts(self.env))
		self.env.run(until=length)
		print('Donuts Created: ' + str(self.donuts_created))
		print('End Profit: ' + str(self.profit))

