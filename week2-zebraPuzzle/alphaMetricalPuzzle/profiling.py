"""
To profile in python....
	python -m cProfile <filename.py>


LAW OF DIMINISHING RETURNS
 in all productive processes, adding more of one
 factor of production, while holding all others
 constant, will at some point yield lower
 per-unit returns


In our programme, 63% of time is spent in
eval(), so we should focus on this to improve
efficiency.

But.... eval() is a core python function,
hence we can not modify it.

So we have 2 options:
- fewer calls
- easier calls


For easier calls...
divide and conquer? In our case, this probably won't work

For fewer calls...
- one big equation?
- (avoid repetions, avoid continuing if we find invalid) fill in one digit at time? If that works, then do the next digit
- eval formula once as a function with paramaters
  (avoids duplication of the parse process of eval)
   ........... this last idea might work
   ............ although we'll need to define
   .............function as a lambda function


LAMBDA FUNCTIONS



"""