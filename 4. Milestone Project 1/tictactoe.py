
def display_board(my_list):
    print('\n' * 10)
    for index,row in enumerate(my_list):
        print(' | '.join(row))
        if index < len(my_list)-1:
            print("-" * 9)

def marker_choice():
    """
    :return: (Player 1 marker, Player 2 marker)
    """
    choice = ''
    while choice not in ['X', 'O']:
        choice = input("Choose a marker (X or O): ").upper()
        if choice not in ['X', 'O']:
            print("Oops wrong choice!")
    return ('X', 'O') if choice == 'X' else ('O', 'X')

def place_marker(board, marker, position):
    row = (position-1) // 3
    col = (position-1) % 3
    board[row][col] = marker

def win_check(board, marker):
    for r in range(3):
        if board[r][0] == marker and board[r][1] == marker and board[r][2] == marker:
            return True
    for c in range(3):
        if board[0][c] == marker and board[1][c] == marker and board[2][c] == marker:
            return True
    if board[0][0] == marker and board[1][1] == marker and board[2][2] == marker:
        return True
    if board[0][2] == marker and board[1][1] == marker and board[2][0] == marker:
        return True
    return False

def space_check(board, pos):
    """Return True if the given position (1-9) is free."""
    row = (pos - 1) // 3
    col = (pos - 1) % 3
    return board[row][col] == ' '   # True when it's still a digit (free)

def full_board_check(board):
    """Return True if board is full (no digit positions left)."""
    for row in board:
        for num in row:
            if num == ' ':   # if any cell is still a digit, board is NOT full
                return False
    return True

def position_choice(board):
    """Ask player for a position, validate integer, range, and availability."""
    while True:
        try:
            pos = int(input("Choose a position (1 - 9): "))
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        if pos not in range(1, 10):
            print("Please enter a valid position between 1 and 9.")
            continue

        if not space_check(board, pos):
            print("That position is already taken. Choose another.")
            continue

        return pos

def replay():
    choice = ''
    while choice not in ['Y', 'N']:
        choice = input("Do you want to play again (Y / N): ").upper()
        if choice not in ['Y', 'N']:
            print("Please choose a valid option")
    return True if choice == 'Y' else False

if __name__ == '__main__':
    print("Welcome to Tic Tac Toe")
    while True:
        game_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        player1_marker, player2_marker = marker_choice()
        turn = "Player 1"
        print("Player 1 will go first")
        play_game = input("Ready to play? Y or N: ").upper()
        if play_game == 'Y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                display_board(game_list)
                position = position_choice(game_list)
                place_marker(game_list, player1_marker, position)
                if win_check(game_list, player1_marker):
                    display_board(game_list)
                    print("Player 1 Won!")
                    game_on = False
                else:
                    if full_board_check(game_list):
                        display_board(game_list)
                        print("Game Tie!")
                        game_on = False
                    else:
                        turn = "Player 2"
            else:
                display_board(game_list)
                position = position_choice(game_list)
                place_marker(game_list, player2_marker, position)
                if win_check(game_list, player2_marker):
                    display_board(game_list)
                    print("Player 2 Won!")
                    game_on = False
                else:
                    if full_board_check(game_list):
                        display_board(game_list)
                        print("Game Tie!")
                        game_on = False
                    else:
                        turn = "Player 1"
        if not replay():
            break