def printBoard(board):
    print("-" * (len(board) * 3))
    for i in range(len(board)):
        print("|", end='')
        for j in range(len(board[0])):
            print("%c|" % (board[i][j]), end='')
        print()
        print("-" * (len(board) * 3))


def createBoard():
    return [[' ' for i in range(7)] for i in range(5)]


def getChoiceFromMenu():
    print("Please, select the column you want to place your piece in (from 1 to 7): ", end='')
    choice = input()
    while (not choice.isdigit()) and not (1 <= int(choice) <= 7):
        print("Please, use only digit from 1 to 7.")
        print("Choice: ", end='')
        choice = input()
    return choice


def placePieceInBoard(board, choice):
    return None


def gameLoop(board, player1, player2):
    input = 0
    player = True
    while input == 0:
        if player == True:
            print(player1, "turn.\n")
            choice = getChoiceFromMenu()
            placePieceInBoard(board, choice)
        else:
            print(player2, "turn.\n")
            choice = getChoiceFromMenu()
            placePieceInBoard(board, choice)
        player = not player


def getPlayerNames(playerNumber):
    print("Please, input name for the", playerNumber, "player: ", end='')
    name = input()
    while not name.isalpha():
        print("Please, use only alphabetical characters for the name.")
        print("Enter name for the", playerNumber, "player: ", end='')
        name = input()
    print()
    return name


if __name__ == "__main__":
    print("Welcome to connect four! \n\n")
    player1 = getPlayerNames("first")
    player2 = getPlayerNames("second")
    board = createBoard()
    printBoard(board)