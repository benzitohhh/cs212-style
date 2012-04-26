"""In Python, a "translation table" defines a mapping from single characters to single characters.
For example, the following defines a translation table mapping
	A -> 1
	B -> 2
	C -> 3
"""

import string
table = string.maketrans('ABC', '123')

"""To apply this translation to a string:"""
f = 'A+B==C'
s = f.translate(table) # gives '1+2==3'