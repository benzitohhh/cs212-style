# -----------------
# User Instructions
# 
# Write a function, extend_prefix, nested in find_words,
# that checks to see if the prefix is in WORDS and 
# adds that to results if it is.
#
# If not, your function should check to see if the prefix
# is in PREFIXES, and if it is should recursively add letters
# until the prefix is no longer valid.

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
    
WORDS, PREFIXES = readwordlist('words4k.txt')

def find_words(letters):
    return extend_prefix('', letters, set())

def extend_prefix(pre, letters, results):
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            extend_prefix(pre+L, letters.replace(L, '', 1), results)
    return results

print find_words("ACTIONS")
