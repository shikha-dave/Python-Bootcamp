def display_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
current_player = "X"  # Start with Player 1
game_running = True

def get_player_input(current_player, game_running):

    while game_running:
        position = int(input(f"Player {current_player} position from 1-9: "))

        if position < 1 or position > 9:
            print("Invalid position. Please choose a number between 1 and 9.")
            continue

        if board[position - 1] != " ":
            print("Position already taken. Please choose another position.")
            continue

        board[position - 1] = current_player
             
        display_board(board)

        winner = check_winner(board, current_player)
        if winner:
            print(f"Player {winner} wins!")
            game_running = False
            break

        if current_player == "X":
            current_player = "O"        
        else:
            current_player = "X"

        if " " not in board:
            print("Game over! It's a draw.")
            game_running = False

def check_winner(board, current_player):
    # Check rows

    if ((board[0] == board[1] == board[2] == current_player and board[0] != " ") or (board[3] == board[4] == board[5] == current_player and board[3] != " ") or (board[6] == board[7] == board[8] == current_player and board[6] != " ") or (board[0] == board[3] == board[6] == current_player and board[0] != " ") or (board[1] == board[4] == board[7] == current_player and board[1] != " ") or (board[2] == board[5] == board[8] == current_player and board[2] != " ") or (board[0] == board[4] == board[8] == current_player and board[0] != " ") or (board[2] == board[4] == board[6] == current_player and board[2] != " ")):
        return current_player
    else:
        return False

display_board(board)
get_player_input(current_player, game_running)