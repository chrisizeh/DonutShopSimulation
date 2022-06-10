from product import SugarDonut
from machine import Machine
import simpy


# SimPy goes here
class DonutShop:

	def __init__(self, name, creation_interval):
		self.env = simpy.Environment()
		self.stop = False

		self.name = name
		self.machines = self.initialize_machines()

		self.profit = 0
		self.donuts_created = 0
		self.creation_interval = creation_interval


		self.observation_space = []
		self.actions_space = []


	def initialize_machines(self):
		machines = {}
		machines[0] = Machine(self.env, 'Mixer', 3)
		machines[1] = Machine(self.env, 'Donut Cutter', 1)
		machines[2] = Machine(self.env, 'Deep Fryer', 5)
		machines[3] = Machine(self.env, 'Glazing Station', 2)

		return machines

		
	# Initialize environment
	def create(self):
		# Start working process for all machines
		for machine in self.machines.values():
		    self.env.process(machine.run())

		# Run process for a specified time
		self.env.process(self.create_donuts())


	#  Start new episode of environment
	def reset(self):
		self.profit = 0
		self.donuts_created = 0
		self.env = simpy.Environment()

		# Reset Queues of functions
		for machine in self.machines.values():
			machines.reset(self.env)

		self.create()


	# Run environment until next event
	def step(self, action):
		if self.env.peek() < float('inf'):
   			self.env.step()


	# Start creation process of donuts and add profit for finished donut
	def run_donut(self, donut):
	    self.donuts_created += 1
	    yield self.env.process(donut.startCreation())
	    self.profit += donut.cost
	    print('Time: ' + str(self.env.now) + '; Donut done; Profit: ' + str(self.profit))


	# Unlimited loop to create donuts after a specified wait time
	def create_donuts(self):
	    while True:
	        #create instance of activity generator
	        donut = SugarDonut(self.env, self.machines)
	        #run the activity generator for this donut
	        self.env.process(self.run_donut(donut))
	        #freeze till time next donut enters queue has passed
	        yield self.env.timeout(self.creation_interval)


	# Start an environment run with a fixed creation interval
	def start_shift(self, length):
		self.create()
		self.env.run(until=length)
		print('Donuts Created: ' + str(self.donuts_created))
		print('End Profit: ' + str(self.profit))


