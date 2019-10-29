from coffee_station.human import Human
from coffee_station.supplies import Supplies
from .coffee_station.equipment import Equipment


def make_coffee(how_much=1000, ratio=15, flavoring=False):
	"""
	How to make coffee.
	:param int how_much: Volume of coffee in Milliliters
	:param int ratio: Ratio of water to coffee - 1:15 default
	:param bool flavoring: Do you want flavoring?
	:return:
	"""
	h = Human()  # Get Human
	e = Equipment()  # Get Equipment
	s = Supplies(ratio)  # Get supplies and set the water to coffee ratio
	e.fill_kettle(how_much)  # How much coffee are you making? You need this much water
	e.boil_kettle()  # Got to have hot water
	e.scale(s.water_to_coffee(how_much))  # Weighing the coffee provides consistency
	h.fill("grinder", how_much)  # Grind the coffee
	h.fill("french press")  # Add the grounds to the french press
	e.fill_french_press_water(how_much / 3)  # Add 1/3 of the water to the french press
	h.stir(10)  # Bloom the grounds
	h.wait(20)  # Wait for the bloom to finish
	e.fill_french_press_water(how_much / 3 * 2)  # Add the rest of the water
	h.stir(10)  # Hydrate the coffee by stirring
	h.wait(180)  # Wait 3 minutes
	e.plunge()  # 'Press' the french press
	s.flavoring(flavoring)
	h.drink()  # Drink coffee
	h.clean()  # Clean up after yourself


