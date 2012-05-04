"""
Sometimes it is easier to
express ideas a particular language.

We can then convert that to a form the
computer can understand.

For example, the below shows a definition
of a grammar. We could have immediately
defined it as a datastructure of a
dictionary of tuples of lists of strings.

But... it is much easier, more readable
and less error-prone, to define it in a our
own DSL.

We can then easily convert it to python.
"""


def split(text, sep=None, maxsplit=-1):
    "Like str.split applied to text, but strips whitespace from each piece."
    return [t.strip() for t in text.strip().split(sep, maxsplit) if t]

def grammar(description):
    """Convert a description to a grammar"""
    G = {}
    for line in split(description, '\n'):
        lhs, rhs = split(line, ' => ', 1)
        alternatives = split(rhs, ' | ')
        G[lhs] = tuple(map(split, alternatives))
    return G

G = grammar(r"""
Exp     =>  Term [+-] Exp | Term
Term    =>  Factor [*/] Term | Factor
Factor  =>  Funcall | Var | Num | [(] Exp [)]
Funcall =>  Var [(] Exps [)]
Exps    =>  Exp [,] Exps | Exp
Var     =>  [a-zA-Z_]\w*
Num     =>  [-+]?[0-9]+([.][0-9]*)?
""")

print G