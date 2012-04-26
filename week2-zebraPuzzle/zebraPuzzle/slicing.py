"""slicing in pyhon accepts a third "stride" argument
"""

L = range(10)
print L[::2] # [0, 2, 4, 6, 8]
print L[1::2] # [1, 3, 5, 7, 9]
print L[::-1] # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]