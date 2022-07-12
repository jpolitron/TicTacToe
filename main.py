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
    clear_output()
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
    return (((board[7]==mark and board[8] == mark and board[9] == mark) or #across 1-3
    (board[4]== mark and board[5] == mark and board[6] == mark) or
    (board[1]== mark and board[2] == mark and board[3] == mark) or
    (board[7]== mark and board[4] ==mark and board[1] == mark) or #vertical 1-3
    (board[8]== mark and board[5] == mark and board[2] == mark) or
    (board[9]== mark and board[6] == mark and board[3] == mark) or
    (board[1]== mark and board[5] == mark and board[9]==mark) or #diagnal 1-2
    (board[7]== mark and board[5]== mark and board[3] == mark)))
'''
Write a function that uses the random module to randomly decide which player goes first.
You may want to lookup random.randint() Return a string of which player went first.
'''
def choose_first():
     if random.randint(0, 1) == 0:
        return 'Player 2'
     else:
        return 'Player 1'

'''
Write a function that returns a boolean indicating
whether a space on the board is freely available.
'''
def space_check(board, position):
    return board[position] == ' '

'''
Write a function that checks if the board is full and returns a boolean value.
True if full, False otherwise.
'''
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

'''
Write a function that asks for a player's next position (as a number 1-9) and
then uses the function from step 6 to check if it's a free position.
 If it is, then return the position for later use.
'''
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9,10] or not space_check(board,position):
        position = int(input("Choose your next position (1-9): "))
        if space_check(board,position) == False:
            print("Sorry this space has been taken")

    return position


'''
Write a function that asks the player if they want to play again
 and returns a boolean True if they do want to play again.
'''
def replay():
    choice = input("Would you like to play again ? Enter Y for yes N for n: ").upper()
    if choice == 'Y':
        return True
    else:
        return False


print("Welcome to Tic Tac Toe!")

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            print("Player {} its your turn".format(turn))
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            print("Player {} its your turn".format(turn))
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
