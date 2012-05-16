"""
Game theory - decision under certainty, with an opponent

Utility - the value of a state   i.e. U(state)

Quality -   the expected value of taking action a in state s,
            given utility function U
            i.e. average utility given (s, a, U)

Example
*********
Suppose you win $1m on a game show, but they offer you the chance to gamble
it (with a flip of a fair coin) to win $3m.


i.e. in our example, we implement ExpectedUtility(a) as an inner function that in turn calls Quality(s,a,U)


"""

import math

million = 1000000

def Q(state, action, U):
    if action == 'hold':
        return U(state + 1*million)
    if action == 'gamble':
        return U(state + 3*million) * 0.5 + \
                U(state) * 0.5

def actions(state):
    return ['hold', 'gamble']

def identity(x):
    return x

##############################
# Question: Given some state, what is the best action?
# Answer: The one with the highest expected utility.
###############################
def best_action(state, actions, Q, U):
    def EU(action):
        "Expected utility function"
        return Q(state, action, U)
    return max(actions(state), key=EU)

print best_action(100, actions, Q, identity)
print best_action(1000000, actions, Q, math.log10)
print best_action(1000001, actions, Q, math.log10)

print math.log10(1000000)

# This formulation does NOT treat people's perception of money as linear,
# but logarithmic (base10)

# The result is there is a "crossover" point at the state of $1m.
# Here, the optimal action could be either "hold" or "gamble".



