#Implementing Bubble Sort

import random

number = int( raw_input("How many numbers would you like to bubble sort?: ") )

number_range = range(number)

random.shuffle( number_range )

print number_range

def bubble_sort():
	isSorted = False
	while isSorted == False:
		isSorted = True
		for i in range(0, len(number_range)-1):
			first_number = number_range[i]
			second_number = number_range[i+1]
			if first_number > second_number:
				isSorted = False
				number_range[i], number_range[i+1] = number_range[i+1], number_range[i]

bubble_sort()
print number_range
