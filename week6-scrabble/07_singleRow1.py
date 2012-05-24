class anchor(set):
    """An anchor is where a new word can be placed; has a set of allowable letters"""

# Unrestricted anchor (can take any letter)
LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ANY = anchor(LETTERS) 

# Restricted anchors
mnx, moab = anchor('MNX'), anchor('MOAB')

# so our row looks like this...
a_row = row = ['|', 'A', mnx, moab, '.', '.', ANY, 'B', 'E', ANY, 'C', ANY, '.', ANY, 'D', ]

# A hand
a_hand = 'ABCEHKN'

# The row (that we're trying to model)
#  |A....BE.C...D.|