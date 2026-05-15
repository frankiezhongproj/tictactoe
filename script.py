board = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
player1 = "X"
player2 = "O"
win = False


def display_board(board):
    for x in range(3):
        for y in range(3):
            print(board[x][y], end="|")
        print("")
        print("----------")


def checkMove(spot):
    if spot < 1 or spot > 9:
        return False
    row = (spot - 1) // 3
    col = (spot - 1) % 3
    return str(board[row][col]).isdigit()


def checkWin(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def checkDraw(board):
    for i in range(3):
        for j in range(3):
            if str(board[i][j]).isdigit():
                return False
    return True


while not win:
    display_board(board)
    print("Player 1's turn")
    try:
        spot = int(input("Where would you like to play? "))
    except ValueError:
        spot = -1
    while not checkMove(spot):
        try:
            spot = int(input("Please pick a valid spot! "))
        except ValueError:
            spot = -1
    board[(spot - 1) // 3][(spot - 1) % 3] = player1
    if checkWin(board, player1):
        print("Player 1 wins!")
        win = True
        display_board(board)
        break
    if checkDraw(board):
        display_board(board)
        print("Draw!")
        win = True
        break
    display_board(board)
    print("Player 2's turn")
    try:
        spot = int(input("Where would you like to play? "))
    except ValueError:
        spot = -1
    while not checkMove(spot):
        try:
            spot = int(input("Please pick a valid spot! "))
        except ValueError:
            spot = -1
    board[(spot - 1) // 3][(spot - 1) % 3] = player2
    if checkWin(board, player2):
        print("Player 2 wins!")
        win = True
        display_board(board)
        break




