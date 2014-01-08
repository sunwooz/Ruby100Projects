#fibonnaci sequence
def find_fibo():
	while fibo_list[-1] < input_number:
		new_number = fibo_list[-2] + fibo_list[-1]
		if input_number >= new_number:
			fibo_list.append( new_number )
			find_fibo()
		else:
			return

input_number = int( raw_input("Please input a number: ") )

fibo_list = [0,1]

find_fibo()

print fibo_list

