import doctest
from waterPouring import *

class Test: """
>>> successors(0, 0, 4, 9)
{(0, 9): 'fill Y', (0, 0): 'empty Y', (4, 0): 'fill X'}

>>> def num_actions(triplet): X, Y, goal = triplet; return len(pour_problem(X, Y, goal)) 

>>> max([(X, Y, goal) for X in range(1, 10) for Y in range(1, 10)
...                   for goal in range(1, max(X, Y))], key=num_actions)
(7, 9, 8)
"""

print doctest.testmod()

