import random


def printboard():
    j = 0
    print("\n\n\n\n\n")
    while j < 9:
        for i in range(3):
            print(board[j], end=' | ')
            j += 1
        print('\b\b')
    print("\n")


def mark(t, s):
    board[s] = t


def checkwin():
    for m in range(3):
        if board[m] == board[m + 3] == board[m + 6]:
            return True
    for m in [0, 3, 6]:
        if board[m] == board[m + 1] == board[m + 2]:
            return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True

    return False


board = []
movemade = [69]
player1wontoss = False
win = False
for i in range(1, 10):
    board.append(str(i))
printboard()
player1name = input("Player 1 enter your name: ")
player2name = input("Player 2 enter your name: ")
run = True
toss = input(f"{player1name} please chose (H/T): ")
tossres = random.randint(1, 2)
if tossres == 1:
    print("\nHEADS!!\n")
else:
    print("\nTAILS!!\n")

if tossres == 1 and (toss == "H" or toss == "h"):
    player1wontoss = True
    p1 = input(f"{player1name} choose your token : ")
    p2 = input(f"{player2name} choose tour token : ")
elif tossres == 2 and (toss == "T" or toss == "t"):
    player1wontoss = True
    p1 = input(f"{player1name} choose tour token : ")
    p2 = input(f"{player2name} choose tour token : ")
else:
    p2 = input(f"{player2name} choose tour token : ")
    p1 = input(f"{player1name} choose tour token : ")

while run:

    printboard()
    newmove = False

    if player1wontoss:
        while not newmove:
            sq = int(input(f"{player1name} enter square you want to mark: "))
            sq -= 1
            for c in range(len(movemade)):
                if movemade[c] == sq:
                    newmove = False
                    break
                else:
                    newmove = True
            if newmove:
                movemade.append(sq)
                mark(p1, sq)
                player1wontoss = False
    else:
        while not newmove:
            sq = int(input(f"{player2name} enter square you want to mark: "))
            sq -= 1
            for c in range(len(movemade)):
                if movemade[c] == sq:
                    newmove = False
                    break
                else:
                    newmove = True
            if newmove:
                movemade.append(sq)
                mark(p2, sq)
                player1wontoss = True

    win = checkwin()
    if win or len(movemade) == 10:
        run = False

printboard()
if not win:
    print("DRAW!!")
else:
    if player1wontoss:
        print(f"{player2name} WON!!")
    else:
        print(f"{player1name} WON!!")
