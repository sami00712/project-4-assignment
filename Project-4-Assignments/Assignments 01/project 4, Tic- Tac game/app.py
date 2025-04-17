import os
import time

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

won = False
turns = 9
input_index = {
    "1": (0, 0), "2": (0, 1), "3": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "7": (2, 0), "8": (2, 1), "9": (2, 2)
}


def print_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("____________")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("____________")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")


def winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None


while not won and turns > 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_board(board)
    mark = 'X' if turns % 2 == 1 else 'O'
    user_input = input(f"Player {mark}, choose (1-9): ")

    if user_input not in input_index:
        print("❌ Invalid input! Choose between 1-9.")
        time.sleep(1)
        continue

    row, col = input_index[user_input]

    if board[row][col] == " ":
        board[row][col] = mark
        turns -= 1
        winner_mark = winner(board)
        if winner_mark:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(board)
            print(f"\n🎉 Congratulations! Player {winner_mark} wins! 🎉")
            won = True
    else:
        print("❌ Space is already filled, please choose another!")
        time.sleep(1)

if not won:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_board(board)
    print("\n🤝 It's a draw!")


    