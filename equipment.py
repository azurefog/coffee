from coffee_station.supplies import Supplies


class Equipment:

	def __init__(self):
		self.s = Supplies()

	def fill_kettle(self, water=1000):
		print('Fill Kettle with ' + str(water) + " milliliters")

	def boil_kettle(self):
		print('Turn on the kettle until it boils and turns off')

	def scale(self, weight):
		print('Weight ' + str(weight) + " grams of beans")

	@staticmethod
	def grinder():
		print("Set switch all the way to the right and grind until beans are gone")

	def fill_french_press_water(self, volume):
		print("Add " + str(volume) + " milliliters water to the french press")

	@staticmethod
	def plunge():
		print("Push down the plunger")


