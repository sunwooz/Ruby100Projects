# Check if Palindrome - Checks if the string entered
# by the user is a palindrome. That is that it reads
# the same forwards as backwards like "racecar"


input_text = raw_input("Type in one word. ")

if input_text[::-1] == input_text:
	print "This word is a palindromic word."
else:
	print "This word is not a palindromic word."
