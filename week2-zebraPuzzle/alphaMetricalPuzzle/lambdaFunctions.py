'''
	In Python, a lmbda function is an anonymous inline function.

	The syntax is derived from the lambda calculus, a formal mathametical treatment of functions.
'''

#Example lambda function
f = lambda x, y, z : x**x + 3*y + z
#print f(3,6,7)



# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word_ben(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    return word if not word.isupper() else '+'.join(['1' + i*'0' + "*" + word[len(word)-1-i] for i in range(len(word))])

def compile_word(word):
	if word.isupper():
		terms = [('%s*%s' % (10*i, d)) for (i,d) in enumerate(word[::-1])]
		return '(' + '+'.join(terms) + ')'
	else:
		return word

print compile_word("YOU")