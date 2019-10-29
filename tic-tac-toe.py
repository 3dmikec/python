import random

# Print out a board, set up as a list, where each index 1-9 corresponds with a number on a number pad.

def display_board(board):
    
    print('\n ',board[7],' | ',board[8],' | ',board[9])
    print('-----------------')
    print(' ',board[4],' | ',board[5],' | ',board[6])
    print('-----------------')
    print(' ',board[1],' | ',board[2],' | ',board[3])
    
# Take in player input and assign their marker as 'X' or 'O'.

def player_input():
    
    while True:
        global player1,player2
        player1 = (input('Player 1: Do you want to be X or O? ').upper())
        if player1 == 'X':
            player2 = 'O'
            print('player 1 = ',player1,'player 2 = ',player2)
            break
        elif player1 == 'O':
            player2 = 'X'
            print('player 1 = ',player1,'player 2 = ',player2)
            break
        else:
            print('\nThat is not a valid choice\n')
            continue

# Take in the board, a marker ('X' or 'O'), a desired position (1-9), and assigns it to the board.

def place_marker(board, marker, position):
    
    board[position] = marker
    
# Take in the board and a marker ('X' or 'O') and then checks to see if that mark has won.

def win_check(board, mark):
    
    winning_combo = [board[1:4],board[4:7],board[7::],board[1::3],board[2::3],board[3::3],board[1::4],board[3:8:2]]
    
    return [mark,mark,mark] in winning_combo

# Randomly decide which player goes first.
    
def choose_first():
    global players_turn
    players_turn = random.randint(1, 2)
    if players_turn == 1:
        return '\nPlayer 1 will go first'
    else:
        return '\nPlayer 2 will go first'
            
# Determines whether a space on the board is freely available.

def space_check(board, position):
    
    return board[position] == ' '

# Checks if the board is full.

def full_board_check(board):
    
    return ' ' not in board

# Asks for a player's next position (1-9) and then checks if it's a free position.

def player_choice(board):

    while True:
        global position
        position = int(input('Choose a position on the board: '))
        
        if position <= 9 and position >= 1 and space_check(board, position):
            break
        else:
            print('\nThat position is not available')
            continue
            
# Asks the player if they want to play again.

def replay():
    
    while True:
        replay = input('\nDo you want to play again? Yes or No? ')
    
        if replay.lower() == 'yes' or replay.lower() == 'no':
            return 'yes' in replay.lower()
        else:
            print('\nThat is not a valid choice\n')
            continue

# Displays a welcome message and an example board corresponding to the numpad.

def welcome():
    
    print('\nWelcome to Tic Tac Toe!\nThe positions on the board correspond to the numbers on your keypad\ne.g.')
    
    board = ['#']+list(range(1,10))
    
    display_board(board)
    
    print('\n\n')
    

# Set up and run the game

while True:
    
    # Display welcome message and example.
    welcome()
    
    # Assign markers to players.
    player_input()
    
    # Informs players who will go first.
    print(choose_first())
    
    # Blank board.
    board = ['#']+[' ']*9
    
    while True:
        
        global players_turn
        
        # Player 1
        if players_turn == 1:
            # Displays the board
            display_board(board)
            print('\nPlayer 1:')
            # Player chooses a position on the board.
            player_choice(board)
            # Marker is placed on the board.
            place_marker(board, player1, position)
            # Checks if player has won. 
            if win_check(board, player1) == True:
                display_board(board)
                print('\nPlayer 1 WINS')
                break
            # Checks if game is tied.
            elif full_board_check(board) == True:
                display_board(board)
                print('\nThe game is a tie')
                break
            # Passes turn to player 2.
            else:
                players_turn = 2
                pass
    
        # Player 2
        else:
            # Displays the board
            display_board(board)
            print('\nPlayer 2:')
            # Player chooses a position on the board.
            player_choice(board)
            # Marker is placed on the board.
            place_marker(board, player2, position)
            # Checks if player has won.
            if win_check(board, player2) == True:
                display_board(board)
                print('\nPlayer 2 WINS')
                break
            # Checks if game is tied.
            elif full_board_check(board) == True:
                display_board(board)
                print('\nThe game is a tie')
                break
            # Passes turn to player 1.
            else:
                players_turn = 1
                continue
        
    # Checks if players want to replay the game.
    if replay() == True:
        continue
    else:
        print('\nGame Over')
        break