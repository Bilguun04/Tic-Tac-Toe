# Tic Tac Toe Game

board = [' ' for i in range(9)] # initialize the board with empty spaces

def print_board():
    row1 = '|'.join(board[0:3])
    row2 = '|'.join(board[3:6])
    row3 = '|'.join(board[6:9])
    print(row1)
    print('-' * 5)
    print(row2)
    print('-' * 5)
    print(row3)

def player_move(player):
    print(f"It's {player}'s turn.")
    position = int(input('Enter a position from 1-9: ')) - 1
    if board[position] != ' ':
        print('This position is already taken. Please choose another one.')
        player_move(player)
    else:
        board[position] = player
        print_board()

def check_winner():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    return None

def is_board_full():
    return ' ' not in board

print_board()

while True:
    player_move('X')
    if check_winner():
        print(f'{check_winner()} has won the game!')
        break
    elif is_board_full():
        print('The game is a tie!')
        break
    player_move('O')
    if check_winner():
        print(f'{check_winner()} has won the game!')
        break
    elif is_board_full():
        print('The game is a tie!')
        break
