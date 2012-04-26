"""for statements . the whole truth"""

"""
"for" in Python can interate over not just lists, but any iterable.
For example
	for i in <iterable>:
		print i

Upon running, python iterprets the clause in this order:
	it = iter(<iterable>)
	try:
		while True:
			x = next(it)
			# do stuff
	except StopIteration:
		pass
"""


