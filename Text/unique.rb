#Unique characters - Make sure all characters in string are unique.
require 'set'

my_string = 'abc      def g h i jklmn'

string_wo_spaces = my_string.gsub( /\s+/, "")

string_count = string_wo_spaces.length

string_array = string_wo_spaces.split('')

if string_count == string_array.to_set.length
	puts 'All strings are unique'
else
	puts 'Strings are not unique'
end