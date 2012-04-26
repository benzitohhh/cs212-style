import itertools

input = 'ODD+ODD==EVEN'

# how many different chars in string?
chars = set(input)

nChars = len(chars)
digits = range(10)


"""
concepts:
	equations
		original
		filled
	letters
	digits
	assignment
		letter->digits
	evaluation

represntations:
	equations:
		original - string
		filled - string
	letters - 's'
	digits - 3
	assignment
		letter->digits   - table 'd' -> '3'
		                 - can use str.translate
			                 import string
							 table = string.maketrans('ABC', '123')
							 # in the above, A maps to 1, B to 2, C to 3 etc...) 
							 f = 'A+B==C'
							 s = f.translate(table) # gives '1+2==3'
	evaluation - eval function  i.e. eval('1+2==3')

	could also have a valid(f) function

	also might want to use try:
	                       except
	                       blocks
"""