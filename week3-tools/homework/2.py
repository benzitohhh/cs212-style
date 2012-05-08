# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the 
# non-negative numbers. The runtime of your program should be 
# proportional to the LOGARITHM of the input. You may want to 
# do some research into binary search and Newton's method to 
# help you out.
#
# This function should return another function which computes the
# inverse of the input function. 
#
# Your inverse function should also take an optional parameter, 
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The 
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is 
# efficient enough. 

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1 

def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""

    def f_1(y, x0=0):
        fx0 = f(x0)

        # base case
        if abs(fx0 - y) < delta:
            return x0

        # approximate derrivative
        d = (f(x0 + delta) - fx0) / delta

        # calculate X1
        x1 = x0 - ((fx0 - y) / d)

        # recurse
        return f_1(y, x1)

    return f_1
    
def square(x): return x*x
sqrt = slow_inverse(square)

def binarySearch(arr, key, imin, imax):
    if imax < imin:
        return -1
    mid = (imax+imin)/2
    # 3 way comparison
    if arr[mid] > key:
        return binarySearch(arr, key, imin, mid-1)
    elif arr[mid] < key:
        return binarySearch(arr, key, mid+1, imax)
    else:
        return mid


g = inverse(square)
print g(400)
# print sqrt(1000000000)