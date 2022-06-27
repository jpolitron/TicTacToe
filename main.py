'''
Intro: ask the player for their names and ask if the first player what they wouldl ike to be
ask first player where they would like it
print  board every move
ask next player
keep track of score
print winner
ask if thye wpou;d play again
'''
import random
from IPython.display import clear_output
'''
Write a function that can print out a board.
Set up your board as a list,
where each index 1-9 corresponds with a number on a number pad,
so you get a 3 by 3 board representation.
'''
def display_board(board):
    print("[{},{},{}]\n".format(board[7], board[8], board[9]))
    print("[{},{},{}]\n".format(board[4], board[5], board[6]))
    print("[{},{},{}]\n".format(board[1], board[2], board[3]))
'''
Write a function that can take in a player input and assign their marker as 'X' or 'O'.
Think about using while loops to continually ask until you get a correct answer.
'''
def player_input():
    marker = ''
    marker = input('Player 1: Do you want to be X or O? ').upper()
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
'''
Write a function that takes in the board list object,
a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
'''
def place_marker(board, marker, position):
    board[position] = marker
'''
Write a function that takes in a board and a mark (X or O)
 and then checks to see if that mark has won.
'''
def win_check(board, mark):
    return (((board[7]==board[8] and board[8]==board[9]) or #across 1-3
    (board[4]==board[5] and board[5]==board[6]) or
    (board[1]==board[2] and board[2]==board[3]) or
    (board[7]==board[4] and board[4]==board[1]) or #vertical 1-3
    (board[8]==board[5] and board[5]==board[2]) or
    (board[4]==board[6] and board[6]==board[3]) or
    (board[1]==board[5] and board[5]==board[9]) or #diagnal 1-2
    (board[7]==board[5] and board[5]==board[3])))
'''
Write a function that uses the random module to randomly decide which player goes first.
You may want to lookup random.randint() Return a string of which player went first.
'''
def chose_first():


test_board = ['#','X','O','X','O','X','O','X','O','X']
place_marker(test_board,'$',8)
print(display_board(test_board))
print(win_check(test_board,'X'))
