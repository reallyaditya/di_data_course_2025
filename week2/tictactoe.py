board = [
    ["1", " | ", "2", " | ", "3"],
    ["-", " + ", "-", " + ", "-"],
    ["4", " | ", "5", " | ", "6"],
    ["-", " + ", "-", " + ", "-"],
    ["7", " | ", "8", " | ", "9"],
]
avaliable_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def display_board():
    """Prints the current state of the board"""
    for i in board:
        print("".join(i))


def player_input(player):
    """Takes player input, updates the board, and checks for a win."""
    position = input(f"Enter {player} at position: ")
    while avaliable_numbers.count(position) == 0:
        position = input("Enter a valid position: ")
    avaliable_numbers.remove(position)
    for row in board:
        try:
            row[row.index(position)] = player
        except ValueError:
            pass
    display_board()
    if check_win():
        print(f"{player} has won the game!")
        return True


def check_win():
    """Checks if there is a win on the board"""
    count_column = []
    # loops through the columns
    for column in range(0, 5, 2):
        # loops through the rows
        for row in range(0, 5, 2):
            # checks if there are 3 in a row
            if board[row].count("x") == 3 or board[row].count("o") == 3:
                return True
            count_column.append(board[row][column])
        # checks if there are 3 in a column
        if count_column.count("x") == 3 or count_column.count("o") == 3:
            return True
        count_column.clear()
    # checks the diagonals
    if board[0][0] == board[2][2] == board[4][4]:
        return True
    if board[0][4] == board[2][2] == board[4][0]:
        return True


def play():
    """Starts and manages the Tic Tac Toe game."""
    display_board()
    win = False
    turns = 0
    while not win:
        if turns > 8:
            print("It's a tie!")
            break
        if turns % 2 == 0:
            win = player_input("x")
        else:
            win = player_input("o")
        turns += 1


# starts the game
play()
