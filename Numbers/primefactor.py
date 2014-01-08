#prime factorization
#looks for factors of input number, then looks for primes in the list of factors

the_number = int( raw_input("Enter a number ") )

def find_factors(number):
	factor_list = []
	#primes haves to be greater than one, but this method looks for all factors
	for n in range(-number, number+1):
		if n == 0: continue
		if number % n == 0 or n == number:
			factor_list.append(n)
	print "Factors: "
	print factor_list
	return factor_list

def find_primes_in_list(factor_list):
	prime_list = []
	for i in factor_list:
		if i < 2: continue
		if i == 2:
			prime_list.append(i)
			continue
		for n in range(2, i):
			if i % n == 0:
				break
			if n == i-1:
				prime_list.append(i)
			if i % n != 0:
				continue
	print "Primes: "
	print prime_list


find_primes_in_list( find_factors(the_number) )