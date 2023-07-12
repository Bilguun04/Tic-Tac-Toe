import random

board = [' ' for x in range(9)]

def print_board():
    row1 = "|".join(board[:3])
    row2 = "|".join(board[3:6])
    row3 = "|".join(board[6:])
    print()
    print(row1)
    print("-+-+-")
    print(row2)
    print("-+-+-")
    print(row3)
    print()

def player_move(icon, choice):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is taken!")

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

class Bot():
    def __init__(self):
        pass
    def move(self, choice, icon = 'X'):
        choice = random.randint(1, 9)
        player_move(icon, choice)

print("Who do you want to play with?")
print("a. Both")
print("b. 2 players")
user_input = input("a or b?\n")

while user_input == 'b':
    print_board()
    choice = int(input("Enter your move (1-9): ").strip())
    player_move("X", choice)
    print_board()
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    choice = int(input("Enter your move (1-9): ").strip())
    player_move("O", choice)
    if is_victory("O"):
        print("O wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break

while user_input == 'a':
    print_board()
    choice = int(input("Enter your move (1-9): ").strip())
    player_move('X', choice)
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    bot_input = 1
    if board[bot_input] != 'O':
        bot_input = random.randint(1, 9)-1
    player_move('O', bot_input)
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    print_board()