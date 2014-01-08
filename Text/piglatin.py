#pig latin

original = raw_input("Please input some text: ")

split_text = original.split()
pig_latin_list = []
vowels = "aieuo"

def pigify():
	for i in split_text:
		first_letter = i[0]
		rest_letters = i[1:len(i)+1:1]
		#If word starts with a vowel, leave it alone and add -ay
		if first_letter in vowels:
			pig_latin_list.append( i + '-ay')
		else:
			pig_latin_list.append(rest_letters + '-' + first_letter + 'ay')

def combine_text():
	finished_text = ""
	for i in range(0, len(pig_latin_list)):
		finished_text += pig_latin_list[i]
		finished_text += " "

	print finished_text

pigify()
combine_text()
