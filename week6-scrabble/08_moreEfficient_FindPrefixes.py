def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters

def readwordlist(filename):
    file = open(filename)
    text = file.read().upper()
    wordset = set(word for word in text.splitlines())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset
    
def find_words(letters):
    return extend_prefix('', letters, set())

def extend_prefix(pre, letters, results):
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            extend_prefix(pre+L, letters.replace(L, '', 1), results)
    return results

def row_plays(hand, row):
	"Return a set of legal plays in row. A row play is an (i, 'WORD') pair."
	results = set()
	# To each allowable prefix, add all suffixes, keeping words
	# this just starts the enumeration at 1 (rather than 0)
	for (i, sq) in enumerate(row[1:-1], 1):
        if isinstance(sq, anchor):
            pre, maxsize = legal_prefix(i, row)
            if pre: ## add to the letters already on the board
                start = i - len(pre)
                add_suffixes(hand, pre, start, results, anchored=False)
            else: ## Empty to left: go through the set of all possible prefixes 
                for pre n find_prefixes(hand):
                    if len(pre) <= maxsize:
                        start = i - len(pre)
                        add_suffixes(removed(hand, pre), pre, start, row, results, anchored=False)
	return results

def legal_prefix(i, row):
	pass
	
def addSuffixes(hand, pre, start, row, results, anchored=True):
    """Add all possible suffixes, and accumulate (start, word) pairs in results"""
    i = start + len(pre)
    if pre in WORDS and anchored and not is_letter(row[i]):
        results.add((start, pre))
    if pre in PREFIXES:
        sq = row[i]
        if is_letter(sq):
            add_suffixes(hand, pre+sq, start, row, results)
        elif is_empty(sq):
            possibilities = sq if isinstance(sq, anchor) else ANY
            for L in hand:
                if L in possibilities:
                    add_suffixes(hand.replace(L, '', 1), pre+L, start, row, )
    return results

class anchor(set):
    """An anchor is where a new word can be placed; has a set of allowable letters"""
    pass

WORDS, PREFIXES = readwordlist('words4k.txt')

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




