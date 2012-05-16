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

U = identity

##############################
# Question: Given some state, what is the best action?
# Answer: The one with the highest expected utility.
###############################
def best_action(state):
    def EU(action):
        "Expected utility function"
        return Q(state, action, U)
    return max(actions(state), key=EU)

print best_action(0)

# But... in this formulation,
# the optimal statregy is ALWAYS to gamble.

# Effectively, it assumes that $3m is 3 times better than $1m

# But of course, for most people, that is not true.
# Going from $0 to $1m is a big big jump. $1m to 3m is much smaller.
# (even though arithmetically this is not the case)

# This does not mean that people are irrational.

# Instead it shows that to people, the value of money
# is not a linear function.

