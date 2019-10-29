from coffee_station.supplies import Supplies
from coffee_station.equipment import Equipment


class Human:
	def __init__(self):
		self.s = Supplies()
		self.e = Equipment

	def stir(self, time):
		print('Stir for ' + str(time) + " seconds")

	def fill(self, target, volume=1000):
		if target == "kettle":
			self.e.fill_kettle(volume)
		if target == "grinder":
			print("Fill grinder with " + str(self.s.water_to_coffee(volume)) + " grams beans")
			self.e.grinder()
		if target == "french press":
			print("Fill french press with ground coffee beans")

	def wait(self, how_long):
		print("wait for " + str(how_long) + " seconds")

	def drink(self):
		print('Drink coffee')

	def clean(self):
		print('Clean up the coffee station')
