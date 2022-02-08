# NASA-Mars-Exploration-Rovers

### PROBLEM STATEMENT
A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth. A rover’s position and location is represented by a combination of x and y co- ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation.

An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.In order to control a rover, NASA sends a simple string of letters. The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right respectively, without moving from its current spot. ‘M’ means move forward one grid point, and maintain the same Heading. Assume that the square directly North from (x, y) is (x, y+1).

#### Input Description:
The first line of input is the upper-right coordinates of the plateau, the lower- left coordinates are assumed to be 0,0. The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover’s position, and the second line is a series of instructions telling the rover how to explore the plateau. The position is made up of two integers and a letter separated by spaces, corresponding to the x and y coordinates and the rover’s orientation. Each rover will be finished sequentially, which means that the second rover won’t start to move until the first one has finished moving.

#### Output Description:
The output for each rover should be its final coordinates and heading.


##### Sample Input:
```
# max Plateau grid
5 5

# rover1
1 2 N 
L M L M L M L M M

# rover2
3 3 E 
M M R M M R M R R M
```

##### Sample Output:
```
# rover1
1 3 N

# rover2
5 1 E
```


## HOW IT WORKS
This program is implemented using oop concepts to ensure for reusability & organization. Each object `Plateau` and `Rover` are represented by it's own class.
An insance of the Plateau class takes 2 parameters: the planet & the max-grid size.
That of the Rover also takes 2 params, one of which is an instance of the plateau object (i.e the particular plateau the rover is to navigate.) and it's spawn position on the aforementioned plateau.

#### Available methods:
Of all the available methods here some of the most useful ones.
##### Plateau Methods
* `plateau_resize` 
    - scales up or down the max grid size of the plateau. It takes in 1 parameter - `new_grid`(in format `"5 5"`).
* `rover_count` 
    - returns the number of rovers traversing a single plateau.
* `plateau_details` 
    - returns a summary of a plateau details.
##### Rover Methods
* `rover_details` 
    - returns a summary of a rover details.
* `navigate` 
    - which takes 1 parameter - `directions` in a string formart seperated by spaces. It maneuvers the rover according to commands given in the directitons str. Accepted commands are - `"L"`, `"R"` and `"M"`.

#### Example:
```python
# Initialize Plateau
Mars_Plateau = Plateau('Mars', '10 10')

# Resize Plateau
Mars_Plateau.plateau_resize('50 50')

# Initialize 3 Rover for a plateau on Mars
rover1 = Rover(Mars_Plateau, '1 2 N')
rover2 = Rover(Mars_Plateau, '0 0 E')
rover3 = Rover(Mars_Plateau, '10 2 W')

# Move a rover to the next point based on the commands and return the final position and heading.
rover1.navigate("L M L M L M L M M") 

# get_rover_details
rover1.rover_details()

# get plateau details
Mars_Plateau.plateau_details()
```

