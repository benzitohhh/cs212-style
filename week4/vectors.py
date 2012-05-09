a = (1,3,5)
b = (4,6,8)

def add(X, Y):
	return tuple(x+y for x,y in zip(X, Y))

def sub(X, Y):
	return tuple(x-y for x,y in zip(X, Y))

print sub(a, b)