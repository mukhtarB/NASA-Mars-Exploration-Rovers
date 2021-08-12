class Plateau:
	"""
	Defines the plateau object, it's layout, size, the planets it's deployed to, & the number of rovers navigating
	the plateau.
	:param planet: The planet the plateau is deployed to.
	:param grid: Represents the grid size of the plateau.
	"""

	__no_of_plateau = 0
	_no_of_rovers = 0

	def __init__(self, planet, grid):
		self.planet = planet.capitalize()
		self.grid_size = grid.strip().replace(" ", ",")

		Plateau.__no_of_plateau += 1
		self.name = f"Plateau_{self.__no_of_plateau}: {self.planet}"

		print(f"--> {self.name} initialized at ({self.grid_size})")

	def plateau_resize(self, new_grid):
		self.grid_size = new_grid
		return f"New grid co-ordinates are : {self.grid_size}"

	def rover_count(self):
		return self._no_of_rovers

	def plateau_grid_coord(self):
		plateau_x, plateau_y = self.grid_size.split(',')
		return int(plateau_x), int(plateau_y)

	def plateau_details(self):
		return f"{self.name} Details --> {self.__dict__}"

	@classmethod
	def total_num_of_plateau(cls):
		return cls.__no_of_plateau

	def __repr__(self):
		return f"Plateau('{self.planet}', '{self.grid_size}'))"

	def __str__(self):
		return f"{self.name}"


class Rover:
	"""
	Defines a rover object, it's connected plateau, it's location on the plateau and it's movement along the plateau.
	:param plateau object: an instance of the plateau class
	:param spawn loc: An initial position within the grid
	"""

	__cardinal_points = ['N', 'E', 'S', 'W']
	__navigation_commands = ['M', 'L', 'R']

	@staticmethod
	def format_loc_input(loc):
		if loc.strip()[-1] in Rover.__cardinal_points:

			try:
				x, y, d = loc.split()
				x = int(x)
				y = int(y)
			except ValueError:
				print('PLEASE INPUT COORDINATES IN PROPER FORMAT --> "x y D" <--, separated by spaces only.', 'x \
					= x coordinate', 'y = y coordinate', 'D = cardinal point orientation', sep="\n\r")
				return False
			else:
				return x, y, d
		else:
			print(f"{loc.strip()[-1]} is not a cardinal point (N, E, W, S).")
			return False

	def __init__(self, plateau, loc):
		loc = loc.upper()
		if Rover.format_loc_input(loc):
			x, y, d = Rover.format_loc_input(loc)

			if isinstance(plateau, Plateau):
				p_x, p_y = plateau.plateau_grid_coord()
				if x <= p_x and y <= p_y:
					self.initial_position = loc
					self.x, self.y, self.orientation = x, y, d
					self.plateau = plateau

					plateau._no_of_rovers += 1
					self.name = f"Rover_{plateau.rover_count()}_Of_{plateau.planet}"
					print(f"The plateau is {self.plateau.name}.\n\r The rover spawned at {self.initial_position}")
				else:
					print("Rover cannot be placed outside of plateau", f"Rover Co-ordinates = {x},{y}", f"plateau \
							co-ordinate = {p_x},{p_y}", sep='\n\r')
			else:
				print(f'Invalid instance: The Plateau "{plateau}" does not exist')

	def navigate(self, directions):
		cmd_list = directions.upper().split()

		orientation_index = self.__cardinal_points.index(self.orientation)
		for cmd in cmd_list:
			if cmd in self.__navigation_commands:

				if cmd == 'L':
					# spin the orientation -90deg or -1 on the cardinal plane
					if orientation_index - 1 < 0:
						orientation_index = len(self.__cardinal_points)
					orientation_index -= 1

					self.orientation = self.__cardinal_points[orientation_index]

				elif cmd == 'R':
					# spin the orientation +90deg or +1 on the cardinal plane

					orientation_index += 1
					if orientation_index == len(self.__cardinal_points):
						orientation_index = 0

					self.orientation = self.__cardinal_points[orientation_index]

				# navigate the plane in direction of orientation
				else:
					if self.orientation == 'N':
						self.y += 1
					elif self.orientation == 'S':
						self.y -= 1
					elif self.orientation == 'E':
						self.x += 1
					elif self.orientation == 'W':
						self.x -= 1
					else:
						print("Invalid Orientation")

			else:
				print("Invalid Command")

		p_x, p_y = self.plateau.plateau_grid_coord()
		if self.x > p_x or self.y > p_y:
			return f"ROVER WENT OUT OF BOUNDS OF PLATEAU GRID ({p_x}, {p_y})"
		return self.x, self.y, self.orientation

	def rover_details(self):
		details = {
			'rover name': self.name,
			'spawn position': self.initial_position,
			'final position': f'{self.x} {self.y} {self.orientation}',
			'Navigating Plane (plateau)': self.plateau
		}
		return f"{self.name} Details --> {details}"

	def __repr__(self):
		return f"Rover({self.plateau.name}, '{self.initial_position}')"

	def __str__(self):
		return f"{self.name}"


if __name__ == '__main__':
	while True:
		print('=================================')
		print('a. Create Plateau', 'b. Create Rover', 'c. Navigate Rover', sep="\n\r")
		print('=================================')

		choice = input("====input a, b, c or exit: \n\r").casefold()
		if choice == 'a':
			planet_name = input("Enter Planet Name: ").title()
			planet_grid = input("Enter grid size: ")
			print("----------------")
			if planet_grid.split().__len__() == 2 and ',' not in planet_grid:
				exec(f"{planet_name}_Plateau = Plateau('{planet_name}', '{planet_grid}')")
				print(f"\n\r--> Plateau created, Name: {planet_name}_Plateau\n\r")
				print(locals())
			else:
				print("Grid should be in the format 'x y' separated by spaces only.")

		elif choice == 'b':
			plateau_name = input("Enter plateau to navigate: ").title()
			rover_spawn_pos = input("Give spawn position: ")
			print("----------------")

			try:
				plateau_name = locals()[plateau_name]
			except KeyError:
				print(f"**Plateau {plateau_name} does not exist")

			rover_name = Rover(plateau_name, rover_spawn_pos)
			try:
				locals()[rover_name.__str__()] = rover_name
				print(f"\n\r--> Rover created, Name: {rover_name.__str__()}")
				print(f"\n\r--> {rover_name.rover_details()}\n\r")
			except (ValueError, AttributeError):
				print('PLEASE INPUT COORDINATES IN PROPER FORMAT --> "x y D" <--, separated by spaces only.', 'x \
				= x coordinate', 'y = y coordinate', 'D = cardinal point orientation', sep="\n\r")

		elif choice == 'c':
			rover_name = input("Confirm Name of Rover: ").title()
			navigation_directions = input("Enter navigation commands: ")
			print("----------------")

			try:
				rover_name = locals()[rover_name]
				output = rover_name.navigate(navigation_directions)
				print("OUTPUT***********", output)
			except KeyError:
				print(f"**{rover_name} does not exist")

		else:
			break
