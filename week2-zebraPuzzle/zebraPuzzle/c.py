"""
Zebra Puzzle
1 There are five houses.

2 The Englishman lives in the red house.

3 The Spaniard owns the dog.

4 Coffee is drunk in the green house.

5 The Ukrainian drinks tea.

6 The green house is immediately to the right of the ivory house.

7 The Old Gold smoker owns snails.

8 Kools are smoked in the yellow house.

9 Milk is drunk in the middle house.

10 The Norwegian lives in the first house.

11 The man who smokes Chesterfields lives in the house next to the man with the fox.

12 Kools are smoked in a house next to the house where the horse is kept.

13 The Lucky Strike smoker drinks orange juice.

14 The Japanese smokes Parliaments.

15 The Norwegian lives next to the blue house.

Who drinks water? Who owns the zebra?

Each house is painted a different color, and their inhabitants are of different nationalities, own different pets, drink different beverages and smoke different brands of American cigarettes.
"""

import itertools

def imright(h1, h2):
	"House h1 is immediately right of h2 if h1-h2 == 1."
	return h1-h2 == 1

def nextto(h1, h2):
	"Two houses are next to each other if they differ by 1."
	return abs(h1-h2) == 1

def zebra_puzzle():
	"Return a tuple (WATER, ZEBRA)"
	houses = [first, _, middle, _, _] = [1,2,3,4,5]
	orderings = list(itertools.permutations(houses))
	return next((WATER, ZEBRA)
		for (red, green, ivory, yellow, blue) in orderings
		if imright(green, ivory)			# 6
		for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
		if Englishman is red 				# 2
		if Norwegian is first				# 10
		if nextto(Norwegian, blue)          # 15
		for (coffee, tea, milk, oj, WATER) in orderings
		if coffee is green					# 4
		if Ukranian is tea					# 5
		if milk is middle					# 9
		for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
		if Kools is yellow					# 8
		if LuckyStrike is oj				# 13
		if Japanese is Parliaments			# 14
		for (dog, snails, fox, horse, ZEBRA) in orderings
		if Spaniard is dog					# 3
		if OldGold is snails				# 7
		if nextto(Chesterfields, fox)		# 11
		if nextto(Kools, horse)				# 12
		)

print zebra_puzzle()
