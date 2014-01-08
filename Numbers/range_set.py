# combine the range of numbers without repetitions

list_pair = [(20, 300000),(1, 2), (3, 9), (10, 14), (5, 13), (3, 5), (17, 19)]

def combine_list_to_set(list_pair):
	final_set = set()
	for i in range( len( list_pair ) ):
		for item in range( list_pair[i][0], list_pair[i][1]+1 ):
			final_set.add(item)

	return sorted( final_set )

def list_of_tuples( sorted_list, first_number=0, last_number=None ):
	final_pairs = []
	first_number = sorted_list[0]

	for i in range( len( sorted_list ) ):
		if i == len(sorted_list) - 1:
			final_pairs.append((first_number, sorted_list[i]))
		elif sorted_list[i+1] != sorted_list[i]+1:
			last_number = sorted_list[i]
			final_pairs.append((first_number, last_number))
			first_number = sorted_list[i+1]

	return final_pairs



sorted_list = combine_list_to_set(list_pair)

print list_of_tuples( sorted_list )

