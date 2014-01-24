# Fibonacci Sequence – Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

# -> 1 1 2 3 5 8 13

class Fibo

	def initialize
		puts 'Fibo initialized'
		@array_one = []
		@array_two = []
	end

	def to_nth(nth_number)
		@array_one = [1, 1]
		i = 0
		while i < nth_number
			next_number = @array_one[i] + @array_one[i+1]
			@array_one.push(next_number)
			i+=1
		end
		p @array_one
	end

	def to_number(number)
		@array_two = [1, 1]
		current_number = 0
		i = 0
		until current_number < number
			current_number = @array_two[i] + @array_two[i+1]
			@array_two.push(current_number)
			i+=1
		end
		p @array_two
	end

end

fibo = Fibo.new

fibo.to_number(1000)
fibo.to_nth(12)