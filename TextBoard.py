
from Player import Player

class Board:

    def __init__(self):
        self.board = [["k", "k", "k", "k", "b", "b", "b", "b", "c", "c", "c", "c"],
                      ["k", "k", "k", "k", "b", "b", "b", "b", "c", "c", "c", "c"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["d", "d", "d", "d", "l", "l", "l", "l", "s", "s", "s", "s"],
                      ["d", "d", "d", "d", "l", "l", "l", "l", "s", "s", "s", "s"]]

    def printBoard(self):
        for r in self.board:
            for c in r:
                print(c, end=" ")
            print()

    def placePlayer(self, player, x, y):
        self.board[x][y] = player.getSymbol()
        player.changePosition(x , y)

    def checkLegalPlacement(self, x, y):
        if (x > 11 or x < 0):
            return False
        elif (y > 8 or y < 0):
            return False
        else:
            return True

    def enterRoom(self, player):
        y = player.getPosition()[1]
        if (y < 2 or y > 6):
            return (True, self.board[player.getPosition()[0]][y])

    def move(self, player, roll):
        for i in range(1, roll + 1):
            x = player.getPosition()[0]
            y = player.getPosition()[1]
            x2 = x
            y2 = y
            sym = player.getPosition()[1]
            illegal = True
            while(illegal):
                direction = str(input("What direction (D, U, L, R) ?"))
                if (direction != "D" and direction != "U" and direction != "L" and direction != "R"):
                    print("Invalid direction. Try again.")
                    continue
                if (direction == "D"):
                    y2 = y -1
                    legal = self.checkLegalPlacement(x, y2)
                    if (legal == False):
                        print("Oops! Out of bounds. Try again.")
                        continue
                    else:
                        self.board[x][y] = "-"
                        self.board[x][y2] = sym
                        player.changePosition(x, y2)
                        illegal = False
                elif (direction == "U"):
                    y2 = y + 1
                    legal = self.checkLegalPlacement(x, y2)
                    if (legal == False):
                        print("Oops! Out of bounds. Try again.")
                        continue
                    else:
                        self.board[x][y] = "-"
                        self.board[x][y2] = sym
                        player.changePosition(x, y2)
                        illegal = False
                elif(direction == "L"):
                    x2 = x - 1
                    legal = self.checkLegalPlacement(x2, y)
                    if (legal == False):
                        print("Oops! Out of bounds. Try again.")
                        continue
                    else:
                        self.board[x][y] = "-"
                        self.board[x2][y] = sym
                        player.changePosition(x2, y)
                        illegal = False
                else:
                    x2 = x + 1
                    legal = self.checkLegalPlacement(x2, y)
                    if (legal == False):
                        print("Oops! Out of bounds. Try again.")
                        continue
                    else:
                        self.board[x][y] = "-"
                        self.board[x2][y] = sym
                        player.changePosition(x2, y)
                    illegal = False

