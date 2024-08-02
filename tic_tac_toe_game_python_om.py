def main():
    show_intro()
    board = create_board()
    print_board(board)
    symbol_1, symbol_2 = choose_symbols()
    play_game(board, symbol_1, symbol_2)

def show_intro():
    print("Hello! Welcome to om's Tic Tac Toe game!")
    print("\nRules: Player 1 and player 2, represented by X and O, take turns "
          "marking the spaces in a 3x3 grid. The player who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.")
    input("Press enter to continue.")
    print("\n")

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("---+---+---")
    for row in board:
        print(" | ".join(row))
        print("---+---+---")

def choose_symbols():
    symbol_1 = input("Player 1, do you want to be X or O? ").upper()
    symbol_2 = "O" if symbol_1 == "X" else "X"
    print(f"Player 2, you are {symbol_2}.")
    input("Press enter to continue.")
    print("\n")
    return symbol_1, symbol_2

def play_game(board, symbol_1, symbol_2):
    count = 0
    while count < 9:
        player_symbol = symbol_1 if count % 2 == 0 else symbol_2
        print(f"Player {player_symbol}, it's your turn.")
        row, column = get_move(board)
        board[row][column] = player_symbol
        print_board(board)
        if check_winner(board, player_symbol):
            print(f"Player {player_symbol} wins!")
            return
        count += 1
    print("It's a tie!")

def get_move(board):
    while True:
        row = int(input("Pick a row (0, 1, or 2): "))
        column = int(input("Pick a column (0, 1, or 2): "))
        if 0 <= row <= 2 and 0 <= column <= 2 and board[row][column] == " ":
            return row, column
        print("Invalid move. Try again.")

def check_winner(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):
        return True
    return False

main()
