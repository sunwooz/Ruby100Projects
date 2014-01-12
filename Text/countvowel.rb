# Count Vowels

# 1: Enter a string and the program counts the number of vowels in the text. 

# 2: For added complexity have it report a sum of each vowel found.


# 1

puts 'Enter a string to be counted.'

string_input = gets.chomp.gsub(/\s+/, '')

vowels = 'aiueo'

vowel_count = 0

string_input.each_byte do |character|
	vowels.each_byte do |vowel|
		if character.chr == vowel.chr
			vowel_count += 1
		end
	end
end

puts vowel_count