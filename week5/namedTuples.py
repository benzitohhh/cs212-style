from collections import namedtuple
State = namedtuple('state', 'p me you pending')
s = State(1,2,3,4)
s.me
s.you
s.pending


"""

positives - explicit

negatives - more verbose, may be unfamiliar to some programmers
             i.e. could do the same with classes, but would be even more verbose
"""
