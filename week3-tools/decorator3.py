from functools import update_wrapper

# extremely recursive definition!

def decorator(d):
	"Make function d a decorator: d wraps a function fn"
	return lambda fn: update_wrapper(d(fn), fn)

decorator = decorator(decorator)



@decorator
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
    	return x if not args else f(x, n_ary_f(*args))
    return n_ary_f

@n_ary
def seq(x, y):
	return ('seq', x, y)


