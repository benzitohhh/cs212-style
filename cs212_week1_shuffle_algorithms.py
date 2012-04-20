from random import randrange
from collections import defaultdict

def swap(deck, i, j):
	deck[i], deck[j] = deck[j], deck[i]

def pShuffle(deck):
	"O(n), balanced"
	N = len(deck)
	for i in range(N-1):
		swap(deck, i, randrange(i, N))

def badShuffle(deck):
	"O(n^2), biased"
	N = len(deck)
	swapped = [False] * N
	while not all (swapped):
		i, j = randrange(N), randrange(N)
		swapped[i] = swapped[j] = True
		swap(deck, i, j)

def badShuffle2(deck):
	"O(n^2), balanced"
	N = len(deck)
	swapped = [False] * N
	while not all (swapped):
		i, j = randrange(N), randrange(N)
		swapped[i] = True
		swap(deck, i, j)

def badShuffle3(deck):
	"O(n), balanced"
	N = len(deck)
	for i in range(N):
		swap(deck, i, randrange(N))

def test_shuffler(shuffler, deck='abcd', n=10000):
	counts = defaultdict(int)
	for _ in range(n):
		input = list(deck)
		shuffler(inçput)
		counts[''.join(input)] += 1
	e = n*1./factorial(len(deck))  ## expected count - assume unique cards, so just permutations
	ok = all((0.9 <= counts[item]/e <= 1.1) for item in counts)
	name = shuffler.__name__
	print '%s(%s) %s' % (name, deck, ('ok' if ok else '*** BAD ***'))
	print '   ',
	for item, count in sorted(counts.items()):
		print "%s:%4.1f" % (item, count*100./n),
	print

def test_shufflers(shufflers=[pShuffle, badShuffle, badShuffle2, badShuffle3], decks=['abc', 'ab']):
	for deck in decks:
		print
		for f in shufflers:
			test_shuffler(f, deck)

def factorial(n):
	return 1 if (n <= 1) else n*factorial(n-1)

test_shufflers()

