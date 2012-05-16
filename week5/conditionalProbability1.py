# Suppose we are looking at households that have children.
# 
# We might want to know things like:
# 
# given that a household has total 2 children and at least one boy,
# what is the probability they have 2 boys
# 
# i.e.   p(2 boys | at least one boy, total 2 children)
# 
# i.e.  answer is 1/3
# 
# To model this, we will use th following concept inventory:
# 
# random variable  -  ie. first child born, so could be 'b' or 'g'
# 
# sample space
# 
# events   
#          - collections of sample points
#          i.e. event of having 2 boys
#          - represent as collection or predicte   
# 
# sample points - represent as strings i.e. 'bg', 'bb' etc..

import itertools
from fractions import Fraction
import textwrap

sex = 'BG' # random variable (or at least the set of all possible values for the random variable)

def product(*variables):
    """Helper fuction - returns the cartesian product (as a str)
    of the possibilities for each variable."""
    return map(''.join, itertools.product(*variables))

two_kids = product(sex, sex)
# i.e. ['BB', 'BG', 'GB', 'GG'] 

one_boy = [s for s in two_kids if 'B' in s]
# i.e. ['BB', 'BG', 'GB']

def two_boys(s):
    """predicate - returns True when count of boys is 2"""
    return s.count('B') == 2
    
def condP(predicate, event):
    """Conditional probability: P(predicate(s) | s in event)
    The proportion of states in event for which predicate is true."""
    pred = [s for s in event if predicate(s)]
    return Fraction(len(pred), len(event))

oneBoyGivenTwoBoys = condP(two_boys, one_boy)
# i.e. 1/3


# Now a more complicated question....
# Out of all families with two kids with at least one born on a Tuesday,
# what is the probability of two boys?

day = 'SMTWtFs' # another random variable (or at least the set of possible values for the random variable)
two_kids_bday = product(sex, day, sex, day) # event

boy_tuesday = [s for s in two_kids_bday if 'BT' in s] # "predicate" as a collection

answer = condP(two_boys, boy_tuesday)
# i.e. 13/27


# So why is this so? let's write a function to investigate...

boy_anyday = [s for s in two_kids_bday if 'B' in s] # predicate as a "collection"

month = 'JFMAmjLaSOND'

two_kids_bmonth = product(sex, month, sex, month)

boy_december = [s for s in two_kids_bmonth if 'BD' in s]


def report(verbose=False, predicate=two_boys, predname='2 boys',
            cases = [('2 kids', two_kids),
                     ('2 kids born any day', two_kids_bday),
                     ('at least 1 boy born any day', boy_anyday),
                     ('at least 1 boy born on Tuesday', boy_tuesday),
                     ('at least 1 boy born in December', boy_december)]):
    for (name, event) in cases:
        print 'P(%s | %s) = %s' % (predname, name, condP(predicate, event))
        if verbose:
            print 'Reason:\n"%s" has %d elements:\n%s' % (
                name, len(event), textwrap.fill(' '.join(event), 85))
            good = [s for s in event if predicate(s)]
            print ' of those, %d are "%s":\n%s\n\n' % (
                len(good), predname, textwrap.fill(' '. join(good), 85))

report(verbose=True)