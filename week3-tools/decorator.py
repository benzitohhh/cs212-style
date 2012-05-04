# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 

def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
    	return x if not args else f(x, n_ary_f(*args))
    return n_ary_f

def seq(x, y):
	return ('seq', x, y)

seq = n_ary(seq)


#######################
# The above pattern is so common in python, 
# that there is a special notation for it....
#######################

@n_ary
def seq(x, y):
	return ('seq', x, y)






#######################
# But.... if call help(seq),
# .....we get back the documentation for n_ary
# So...... 
#######################

from functools import update_wrapper

def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
    	return x if not args else f(x, n_ary_f(*args))
    update_wrapper(n_ary_f, f)
    return n_ary_f

def seq(x, y):
	return ('seq', x, y)





#######################
# But.... still.... we will need to 
# repeat  the update_wrapper() call for
# every decorating function
# So....
#######################

from functools import update_wrapper

def decorator(d):
	"Make function d a decorator: d wraps a function fn"
	def _d(fn):
		return update_wrapper(d(fn), fn)
	update_wrapper(_d, d)
	return _d 

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


