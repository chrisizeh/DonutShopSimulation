from machine import Machine
from product import SugarDonut
from env import DonutShop

machines = {}
machines[1] = Machine(1, 'Mixer', 3)
machines[2] = Machine(2, 'Donut Cutter', 1)
machines[3] = Machine(3, 'deepFryer', 5)
machines[4] = Machine(4, 'Glazing Station', 2)

sugarDonut = SugarDonut(machines)

print(sugarDonut)
sugarDonut.nextStep()
print(sugarDonut)
print(machines[1])