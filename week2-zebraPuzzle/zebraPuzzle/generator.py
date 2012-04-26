
# some function
def sq(x):
	print "sq called", x
	return x * x

# generator
g = (sq(x) for x in range(10) if x%2 == 0)

# to use the generator....
m = [i for i in g]
print m  # [0, 4, 16, 36, 64]

"""
Generators have the following advantages over list comprehensions:
1. Stop early - whereas list comps must complete everything
2. Easier to edit
3. Less indentation
"""