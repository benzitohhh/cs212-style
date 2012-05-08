import pprint

def bridge(here):
	here = frozenset(here) | frozenset(['light'])
	explored = set() # set of states we have visited
	# State will be a (people-here, people-there, time-elapsed)
	frontier = [ [(here, frozenset(), 0)] ] # ordered list of paths we have blazed
	if not here:
		return frontier[0]
	while frontier:
		path = frontier.pop(0)
		for (state, action) in bsuccessors(path[-1]).items():
			if state not in explored:
				here, there, t = state
				explored.add(state)
				path2 = path + [action, state]
				if not here:  ## That is, nobody left here
					return path2
				else:
					frontier.append(path2)
					frontier.sort(key=elapsed_time)
	return []

def elapsed_time(path):
	return path[-1][2]

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    here, there, t = state
    if 'light' in here:
    	return dict(((here - frozenset([a,b, 'light']),
	    			  there | frozenset([a,b, 'light']),
	    		      t + max(a, b)),
	    			 (a,b, '->'))
	    		    for a in here if a is not 'light'
	    			for b in here if b is not 'light')
    else:
    	return dict(((here | frozenset([a,b, 'light']),
    				  there - frozenset([a,b, 'light']),
    				  t + max(a, b)),
    				 (a, b, '<-'))
    				for a in there if a is not 'light'
    				for b in there if b is not 'light')

pprint.pprint(bridge([1,2,5,10]))