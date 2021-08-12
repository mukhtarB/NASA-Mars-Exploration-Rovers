import unittest
from rover_problem import Plateau, Rover


class TestPlateauNavigationScript(unittest.TestCase):
	planet = 'Mars'
	grid = '5 5'

	# create plateau for mars
	# NB: Multiple plateaus can be created across Mars also, all having sep rovers exploring them.
	Mars_Plateau = Plateau(planet, grid)

	# rover1
	spawn_location1 = '1 2 N'
	navigation_cmd1 = 'L M L M L M L M M'

	rover1 = Rover(Mars_Plateau, spawn_location1)

	# rover2
	spawn_location2 = '3 3 E'
	navigation_cmd2 = 'M M R M M R M R R M'

	rover2 = Rover(Mars_Plateau, spawn_location2)

	def test_navigate_rover1(self):
		self.assertEqual((1, 3, 'N'), self.rover1.navigate(self.navigation_cmd1))

	def test_navigate_rover2(self):
		self.assertEqual((5, 1, 'E'), self.rover2.navigate(self.navigation_cmd2))

	# testing plateau resize, should plateau need to scale up or down
	def test_plateau_resize(self):
		new_grid = '14 14'
		self.assertEqual('New grid co-ordinates are : 14 14', self.Mars_Plateau.plateau_resize(new_grid))


if __name__ == '__main__':
	unittest.main()
