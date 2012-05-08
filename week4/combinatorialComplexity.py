

"""

Combinatorial optimization problems are...

problems that involve searching for a sequence (or "path") of actions that lead to a particular state.
At each step, there are a number of actions available (the branching factor).
Hence the state space is exponential, although we can not be sure how large.

Such problems are often called "Search". Perhaps a better term would be "Exploration".

An algorithm "explores" the space by expanding nodes. It can be thought of as many people simultaneously exploring
paths simultaneously.

We keep track of the current paths we are exploring in a queue called "frontier".
And to avoid repeation, we keep track of previously explored states in a set called "explored".

We want an algorithm that terminates, and that does so in a reasonable time.


""




