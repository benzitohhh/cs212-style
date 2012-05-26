# -----------------
# User Instructions
# 
# Write the function show that takes a board
# as input and outputs a pretty-printed 
# version of it as shown below.


## Handle complete boards    
    
def a_board():
    return map(list, ['|||||||||||||||||',
                      '|J............I.|',
                      '|A.....BE.C...D.|',
                      '|GUY....F.H...L.|',
                      '|||||||||||||||||'])

def show(board):
    "Print the board."
    for i in board:
        for j in i:
            print j,
        print

show(a_board())
                 
# >>> a_board()
# [['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'], 
#  ['|', 'J', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'I', '.', '|'],
#  ['|', 'A', '.', '.', '.', '.', '.', 'B', 'E', '.', 'C', '.', '.', '.', 'D', '.', '|'],
#  ['|', 'G', 'U', 'Y', '.', '.', '.', '.', 'F', '.', 'H', '.', '.', '.', 'L', '.', '|'], 
#  ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]

# >>> show(a_board())
# | | | | | | | | | | | | | | | | |
# | J . . . . . . . . . . . . I . |
# | A . . . . . B E . C . . . D . |
# | G U Y . . . . F . H . . . L . |
# | | | | | | | | | | | | | | | | |

