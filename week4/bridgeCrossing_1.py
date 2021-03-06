"""

There is a bridge that can only be crossed by max 2
people simultaneously, and they need a flashlight.

But there are 4 people to cross, and only 1 flashlight.

Each person has a different physical ability / fear level,
and so will take a different amount of time to cross.
These times are 1,2,5,10.

represent as tuple

(here, there, t)

here = frozenset {1,2,5,10,'light'}
there = frozenset {}
t = total elapsed time



"""


# -----------------
# User Instructions
# 
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are 
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is 
# '->' for here to there or '<-' for there to here. When only one 
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    here, there, t = state
    if 'light' in here:
    	return dict(
    				# (inner arg is one big generator....)

	    				# state
	    				((here - frozenset([a,b, 'light']),
	    				  there | frozenset([a,b, 'light']),
	    				  t + max(a, b)),
	    				# action
	    				(a,b, '->'))
	    			   for a in here if a is not 'light'
	    			   for b in here if b is not 'light'

	    			# (end of generator)


	    			# NOTE:
	    			#      1. a can equal b
	    			# 			But...... the frozen set will take care of this
	    			# 					i.e. frozenset[a,a,'light'] === frozenset[a,'light']
	    			#
	    			#      2. (a, b) can equal (b, a)   i.e. repetitions
	    			#           But...... dictionary takes care of this
	    			#
	    			#      3. action - representation uncertain
	    			#           i.e. spec said '->'
	    			#                but we are returning (a,b,'->'')
	    			#           But... this uncertainty is "contained", hence ok.

    			   )
    else:
    	return dict(((here | frozenset([a,b, 'light']),
    				  there - frozenset([a,b, 'light']),
    				  t + max(a, b)),
    				  (a, b, '<-'))
    				for a in there if a is not 'light'
    				for b in there if b is not 'light')

def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
    
    return 'tests pass'

print test()