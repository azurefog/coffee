class Supplies:
	def __init__(self, ratio=15):
		self.ratio = ratio

	def water(self, volume=1000):
		"""
		How much water are you using?
		:param int volume:
		:return: None
		"""
		print("Use " + str(volume) + " milliliters of water")

	def water_to_coffee(self, water_volume):
		coffee_mil = water_volume / self.ratio
		return coffee_mil

	def coffee_beans(self, water_volume):
		print("Use " + str(self.water_to_coffee(water_volume)) + " grams of coffee")

	def flavoring(self, flavor=False):
		"""
		Do you want flavoring? Defaults to False because I am not a savage.
		:param bool flavor: True or False
		:return:
		"""
		if flavor:
			print("Add flavoring to taste, you savage")
		else:
			print("You are not a savage. Enjoy your coffee!")