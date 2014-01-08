# binary search on a sorted array of names

surnames = ['Yang', 'Jang', 'Mang', 'Steven', 'Justin', 'Jamus', 'Souffle', 'Andrianna', 'Adaline', 'Catherine', 'Zelda', 'Sierra', 'Sieroo', 'Danyo', 'Daniel']

surnames = sorted(surnames)

target_name = 'Sieroo'

step = 0

def binary_search(name_list, target_name, low=0, high=None):
	if high == None:
		high = len(name_list)
	while low < high:
		middle_index = ( low + high ) / 2
		if name_list[middle_index] == target_name:
			return middle_index
		if is_lower_than_target( name_list[middle_index], target_name ):
			high = middle_index
		else:
			low = middle_index
			high = len(name_list)


def is_lower_than_target(current_name, target_name):
	first_name = sorted( [current_name, target_name] )
	if first_name[0] == target_name:
		return True
	return False


target_index = binary_search(surnames, target_name)

if surnames[target_index] == target_name:
	print 'The index of %s is %s.' % (target_name, target_index)