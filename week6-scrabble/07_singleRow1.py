class anchor(set):
    """An anchor is where a new word can be placed; has a set of allowable letters"""

# The row (that we're trying to model)
#  |A....BE.C...D.|

# Unrestricted anchor (can take any letter)
LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ANY = anchor(LETTERS) 

# Restricted anchors
mnx, moab = anchor('MNX'), anchor('MOAB')

# so our row looks like this...
a_row = row = ['|', 'A', mnx, moab, '.', '.', ANY, 'B', 'E', ANY, 'C', ANY, '.', ANY, 'D', ANY, '|']

# some hand
a_hand = 'ABCEHKN'

def row_plays(hand, row):
	"Return a set of legal plays in row. A row play is an (i, 'WORD') pair."
	results = set()
	# To each allowable prefix, add all suffixes, keeping words

	# this just starts the enumeration at 1 (rather than 0)
	for (i, sq) in enumerate(row[1:-1], 1):

	return results

def legal_prefix(i, row):
	pass



