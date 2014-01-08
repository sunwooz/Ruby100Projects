# Correctly sort a list of strings in order using ASCII

def convert_to_dictionary(the_list):
	dictionary = {}
	for word in len( range(the_list) ):
		i = 0
		key = ''
		value = ''
		while i < len(word):
			if is_letter(word[i]):
				key += word[i]
			else:
				value += word[i]
			i += 1
		if dictionary_has_array(dictionary, key):
			dictionary[key].append(int(value))
		else:
			dictionary[key] = []
			dictionary[key].append(int(value))
	return dictionary

def dictionary_has_array(dictionary, key):
	try:
		if type( dictionary[key] ) == type([]):
			return True
	except:
		return False

def is_letter(character):
	try:
		int(character)
		return False
	except:
		return True

def sort_dictionary(dictionary):
	my_list = []
	sorted_keys = sorted( dictionary.keys() )

	for key in sorted_keys:
		for value in sorted( dictionary[key] ):
			my_list.append(key + str(value))

	return my_list


my_list = ['cat1', 'cat40', 'cat4', 'dog5', 'dog16']
dictionary_data = convert_to_dictionary(my_list)
print sort_dictionary( dictionary_data )
