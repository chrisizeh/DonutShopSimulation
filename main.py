from machine import *
from product import SugarDonut
from env import DonutShop
import simpy

env = simpy.Environment()

machines = {}
machines[1] = Machine(env, 'Mixer', 3)
machines[2] = Machine(env, 'Donut Cutter', 1)
machines[3] = Machine(env, 'Deep Fryer', 5)
machines[4] = Machine(env, 'Glazing Station', 2)


shop = DonutShop(env, 'Best Sugar Donuts!', machines, 4)
shop.start_shift(480)