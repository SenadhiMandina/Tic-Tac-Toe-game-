def creating_board():
    #creating a 3x3 board
    return [[" " for _ in range(3)] for _ in range(3)]

def show_board(board):
    #show the current state
    print("-------------")
    for row in board:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        print("-------------")

def check_winner(board, player):
    #check rows
    for row in board:
        if row.count(player) == 3:
            return True

    #check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def check_draw(board):
    #checks the game is draw
    return all(cell != " " for row in board for cell in row)

def play_game(player1_wins, player2_wins, draws):
    #runs the main game loop for a single game of Tic-Tac-Toe
    board = creating_board()
    current_player = "O"
    player1 = "O"
    player2 = "X"

    while True:
        show_board(board)
        try:
            position = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid move. Enter a number between 1 and 9.")
                continue

            row = position // 3
            col = position % 3

            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    show_board(board)
                    print(f"Player {current_player} wins!")
                    if current_player == player1:
                        player1_wins += 1
                    else:
                        player2_wins += 1
                    return player1_wins, player2_wins, draws
                elif check_draw(board):
                    show_board(board)
                    print("It's a draw!")
                    draws += 1
                    return player1_wins, player2_wins, draws
                else:
                    current_player = player2 if current_player == player1 else player1
            else:
                print("That position is already taken. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")
