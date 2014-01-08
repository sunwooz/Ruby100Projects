# Find Cost of Tile to Cover W x H Floor - Calculate
# the total cost of tile it would take to cover a floor
# plan of width and height, using a cost entered by the user.

# Use input as the input can be integer and float
import math

while True:

	width = input("Width of floor in feet: ")
	height = input("Height of floor in feet: ")


	cost_of_floor_per_square_foot = input("Cost of floor per square foot: ")

	square_feet = width * height

	print cost_of_floor_per_square_foot * square_feet