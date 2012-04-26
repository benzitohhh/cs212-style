# *args notation

# A way of packing/unpacking arguments, with repsect to functions

# They can appear at two places:
# 1. function definition
# 2. function argument

def something(fn, *args):
	fn(*args)


# In a function definition, *args is bound to a tuple (arg0, arg1, arg2, ..)

# In a function  argument, the tuple is unpacked, and seperate variables applied to each argument of function


