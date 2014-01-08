

word = 'abcdefgh'

def isUniqueString(word):
	dictionary = {}
	#remove white space of word
	if len(word) > 256:
		print 'Not unique'
		return False
	for letter in word:
		if letter in dictionary:
			print 'Not unique'
			return dictionary
		else:
			dictionary[letter] = True
	print 'Unique'
	return dictionary

print isUniqueString(word)
