# -----------------
# User Instructions
# 
# Write a function, path_cost, which takes a path as input 
# and returns the total cost associated with that path. 
# Remember that paths will obey the convention
# path = [state, (action, total_cost), state, ...] 
#
# If a path is less than length 3, your function should
# return a cost of 0.
import pprint

def path_cost(path):
    """The total cost of a path (which is stored in a tuple
    with the final action."""
    # path = [state, (action, total_cost), state, ... ]
    if len(path) < 3:
        return 0
    else:
        action, total_cost = path[-2]
        return total_cost
        
def bcost(action):
    """Returns the cost (a number) of an action in the
    bridge problem."""
    # An action is an (a, b, arrow) tuple; a and b are 
    # times; arrow is a string. 
    a, b, arrow = action
    return max(a, b)

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a
    (here, there) tuple, where here and there are frozensets
    of people (indicated by their travel times) and/or the light."""
    here, there = state
    if 'light' in here:
        return dict(((here  - frozenset([a,b, 'light']),
                      there | frozenset([a, b, 'light']),
                      ),
                     (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here  | frozenset([a,b, 'light']),
                      therge - frozenset([a, b, 'light']),
                      ),
                     (a, b, '<-'))
                    for a in there if a is not 'light'
                    for b in there if b is not 'light')  
        
def elapsed_time(path):
    return path[-1][2]

def bridge_problem(here):
    "Find the fastest (least elapsed time) path to the goal in the bridge problem."
    here = frozenset(here) | frozenset(['light'])
    explored = set() # set of states we have visited
    # State will be a (peoplelight_here, peoplelight_there, time_elapsed)
    # E.g. ({1, 2, 5, 10, 'light'}, {}, 0)
    frontier = [ [(here, frozenset(), 0)] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        here1, there1, t1 = state1 = path[-1]
        if not here1 or here1 == set(['light']):  ## Check for solution when we pull best path off frontier
            return path
        for (state, action) in bsuccessors(state1).items():
            if state not in explored:
                here, there, t = state
                explored.add(state)
                path2 = path + [action, state]
                # Don't check for solution when we extend a path
                frontier.append(path2)
                frontier.sort(key=elapsed_time)
    return Fail

def path_states(path):
    "Return a list of states in this path."
    return path[0::2]
    
def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]

pprint.pprint(bridge_problem([1,2,5,10]))