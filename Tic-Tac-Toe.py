# To-Do List:
# Display board
# Play a turn
# Make sure that turn was valid
# Check rows/columns/diagonals for a win
# Check for tie
# Switch between players


# Board = a single list with dashes as blank spaces
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# 3 separate print statements will make a 3x3 board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# These are the 3 global variables
winner = None
playing_game = True
# Player 1 will be 'X'
current_player = 'X'


# SOURCE CODE
def play_game():

    # Define global variables
    global winner
    global current_player

    # Display initial board
    display_board()

    # This while loop will continue until the game ends
    while playing_game:

        handle_turn(current_player)

        check_if_win()

        check_if_tie()

        switch_player()

    # If the game has ended, print out the results
    if winner == 'X' or winner == 'O':
        print('Congatulations! ' + winner + ' won!')
    elif winner == None:
        print("It's a Tie!")


def handle_turn(current_player):

    # Initial prompt for player to begin
    position = input('Choose a position from 1-9: ')

    # Make sure player "ONLY" chooses a # 1-9
    while not position.isnumeric():
        print('This is not a valid entry. Please try again...')
        return handle_turn(current_player)
    while int(position) < 1 or int(position) > 9:
        print('This is not a valid entry. Please try again...')
        return handle_turn(current_player)

    # If valid input is entered, convert player's input into integer - 1
    position = int(position) - 1

    # Make sure player doesn't play on a spot that is already taken
    while board[position] != '-':
            print('Position already taken. Please try again...')
            return handle_turn(current_player)

    board[position] = current_player

    # Diplay board again, but with updated player pieces
    display_board()


def check_if_win():

    global winner
    global playing_game

    # Check each row for a possible win
    def check_rows():
        row_1 = board[0] == board[1] == board[2]
        row_2 = board[3] == board[4] == board[5]
        row_3 = board[6] == board[7] == board[8]

        if row_1 == True and board[0] != '-':
            return board[0]
        elif row_2 == True and board[3] != '-':
            return board[3]
        elif row_3 == True and board[6] != '-':
            return board[6]

    # Check each column for a possible win
    def check_columns():
        column_1 = board[0] == board[3] == board[6]
        column_2 = board[1] == board[4] == board[7]
        column_3 = board[2] == board[5] == board[8]

        if column_1 == True and board[0] != '-':
            return board[0]
        elif column_2 == True and board[1] != '-':
            return board[1]
        elif column_3 == True and board[2] != '-':
            return board[2]

    # Check each diagonal for a possible win
    def check_diagonals():
        diagonal_1 = board[0] == board[4] == board[8]
        diagonal_2 = board[2] == board[4] == board[6]

        if diagonal_1 == True and board[0] != '-':
            return board[0]
        elif diagonal_2 == True and board[2] != '-':
            return board[2]

    # Call previous functions to see if they return anything
    check_rows()
    check_columns()
    check_diagonals()

    # If so... assign the result of the function to a variable
    row_win = check_rows()
    column_win = check_columns()
    diagonal_win = check_diagonals()

    # Award that player the win!
    if row_win:
        playing_game = False
        winner = row_win
    elif column_win:
        playing_game = False
        winner = column_win
    elif diagonal_win:
        playing_game = False
        winner = diagonal_win
    else:
        winner = None


# If check_if_win function fails to return anything...
def check_if_tie():

    global playing_game

    if '-' not in board:
        playing_game = False


# If there is neither a win or a tie from the previous move...
def switch_player():

    global current_player

    if current_player == 'X':
        current_player = 'O'
        print("Player O's turn...")
    elif current_player == 'O':
        current_player = 'X'
        print("Player X's turn...")


# Call function (Source Code) that starts the game
play_game()
