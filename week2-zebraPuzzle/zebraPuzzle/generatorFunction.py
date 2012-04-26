######################
# list comprehension #
######################
g = [i for i in range(1001)]
# g is a list
print g


######################
# generator object   #
######################
g = (i for i in range(1001)) # generator objects are defined with round brackets (not square - that's a list comprehension)
# accesss with next(), or for
for v in g:
	print v


"""
Generators have the following advantages over list comprehensions:
1. Stop early - whereas list comps must complete everything
2. Easier to edit
3. Less indentation
"""



######################
# generator functions #
######################
"""
Generator functions contain a yield.
They allow us to make very large or even infinite lists
"""
def ints(start, end=None):
	"""
	This generator returns all the positive integers
	"""
	i = start
	while i <= end or end is None:
		yield i
		i = i+1
g = ints(0, end=None)
print g.next()
print g.next()


def all_ints():
	"""
	This generator function returns all the integers
	i.e. 0, +1, -1, 2, -2, 3, -3, 4, -4, ....
	"""
	yield 0
	for i in ints(1): # accesses another generator funation using for
		yield -i
		yield i
g = all_ints()
for i in range(10):
	print g.next()

