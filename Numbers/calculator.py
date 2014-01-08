#simple calculator to do basic operations

def get_user_input():
	first_number = raw_input( "Please enter the first number:" )
	operation = raw_input( "Please enter the operation:" )
	second_number = raw_input( "Please enter the second number:" )
	result = perform_math(int(first_number), operation, int(second_number) )
	print first_number + " " + operation + " " + second_number + " = " + str( result )

def perform_math(first, oper, second):
	if oper == "+":
		return first + second
	if oper == "-":
		return first - second
	if oper == "/":
		return first / second
	if oper == "*" or oper == "x":
		return first * second
	if oper == "%":
		return first % second

while True:
	get_user_input()