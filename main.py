from product import SugarDonut
from env import DonutShop

shop = DonutShop('Best Sugar Donuts!', 4)
# shop.start_shift(480)

shop.create()
for i in range(200):
	shop.step('')