# In python 3.x, integer division can result in a float (i.e. 3/2 == 1.5)
# While in python 2.x, integer division always results in an int (i.e. 3/2 == 1)
# In order to get the Python 3 behaviour in 2.x, we can import from the future....
from __future__ import division
import string, re, itertools, time

def solve(formula):
	"""Given a formula like 'ODD + EVEN === EVEN',
	fill in digits to solve it.
	Input formula is a string; output is a digit-filled-in string or None."""
	for f in fill_in(formula):
		if valid(f):
			return f
	return None

########################################################################
# Generator function 
#  - using this allows us to seperate the flow of control from the logic
#  - i.e. instead of having to compute all the fill_ins in one go,
#         we can compute them as and when they are required
########################################################################
def fill_in(formula):
	"""General all possible fillins-in of letters in formula with digits."""
	letters = ''.join(set(re.findall(r'[A-Z]', formula)))
	for digits in itertools.permutations('1234567890', len(letters)):
		table = string.maketrans(letters, ''.join(digits))
		yield formula.translate(table)

def valid(f):
    """Formula f is valid iff it has no numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
        # "\b" is a word boundary
        """We need to exclude numbers starting with zero,
        as these are interpretted as base8 (octal). This in
        turn could cause interpretation errors, and exceptions
        (for example 09 is not octal and will throw and exception)"""
    except (ArithmeticError, SyntaxError):
        return False

def solve(formula):
	"""Given a formula like 'ODD + EVEN === EVEN',
	fill in digits to solve it.
	Input formula is a string; output is a digit-filled-in string or None."""
	for f in fill_in(formula):
		if valid(f):
			return f
	return None



######################################################
# ok... now this is the optimized version......
######################################################

def faster_solve(formula):
	"""Given a formula like 'ODD + EVEN === EVEN',
	fill in digits to solve it.
	Input formula is a string; output is a digit-filled-in string or None.
	This version precompiles the formula, only one eval per formula"""
	f, letters = compile_formula(formula)
	for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
		try:
			if f(*digits) is True:
				table = string.maketrans(letters, ''.join(map(str, digits)))
				return formula.translate(table)
		except ArithmeticError:
				pass

def compile_formula(formula, verbose=False):
	"""Compile formula into a function. Also return letters found, as a str,
	in same order as params of function.
	For excample, 'YOU == ME**2' returns
	(lambda Y, M, E, U, O: (U+10*0+100*Y) == (E+10*M)**2), 'YMEUO' """
	letters = ''.join(set(re.findall(r'[A-Z]', formula)))
	params = ', '.join(letters)
	tokens = map(compile_word, re.split('([A-Z]+)', formula))
	body = ''.join(tokens)
	f = 'lambda %s: %s' % (params, body)
	if verbose: print f
	return eval(f), letters

def compile_word(word):
	#Compile a word of uppercase letters as numeric digits.
	#E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
	#Non-uppercase words unchanged: compile_word('+') => '+' '''
	if word.isupper():
		terms = [('%s*%s' % (10*i, d)) for (i,d) in enumerate(word[::-1])]
		return '(' + '+'.join(terms) + ')'
	else:
		return word

#print faster_solve('ODD+ODD==EVEN')


############################################
# ok.... and here's some testing code
############################################



examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()

def test():
	for f in [solve, faster_solve]:
		print
		print f.__name__, ":"
		t0 = time.clock()
		for example in examples:
			print; print 13*' ', example
			print '%6.4f sec:   % s ' % timedcall(f, example)
		print '%6.4f tot. ' % (time.clock()-t0)



def timedcall(fn, *args):
	"Call function with args; return the time and the result"
	t0 = time.clock()
	result = fn(*args)
	t1 = time.clock()
	return t1-t0, result

test()