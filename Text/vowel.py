#Find the number of vowels in a sentence

#Version 1: Counts how many vowels in a sentence

vowels = "aiueo"

my_sentence = raw_input("Please input a sentence: ")

def count_vowels(sentence):
	count = 0
	for letter in sentence:
		if letter in vowels:
			count += 1
	return count

def print_vowel_number(count):
	if count == 1:
		print "There is one vowel in this sentence"
	if count == 0:
		print "There are no vowels in this sentence"
	if count > 1:
		print "There are %s vowels in this sentence" % (count)

vowel_count = count_vowels(my_sentence)

print_vowel_number(vowel_count)



#Version 2: Counts how many of each vowel in a sentence

for vowel in vowels:
	a = 0
	for letter in my_sentence:
		if letter == vowel:
			a += 1
	if a == 1:
		print "There is one %s" % (vowel)
	if a == 0:
		print "There are no %s's" % (vowel)
	if a > 1:
		print "There are %s %s's" % (a, vowel)

