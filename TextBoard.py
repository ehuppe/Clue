
from Player import Player
import random

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

    def setUpGame(self, players):
        for player in players:
            row = player.getPosition()[0]
            col = player.getPosition()[1]
            if (self.board[row][col] == "-"):
                self.placePlayer(player, row, col)
            else:
                while (self.board[row][col] != "-"):
                    newCol = random.randint(0, 11)
                    if (self.board[row][newCol] == "-"):
                        self.placePlayer(player, row, newCol)

    def placePlayer(self, player, row, col):
        self.board[row][col] = player.getSymbol()
        player.changePosition(row , col)

    def checkLegalPlacement(self, row, col):
        if (col > 11 or col < 0):
            return False
        elif (row > 8 or row < 0):
            return False
        elif (self.board[row][col] != "-"):
            return False
        else:
            return True

    def inRoom(self, player):
        row = player.getPosition()[0]
        if (row < 2 or row > 6):
            return True
        else:
            return False

    def move(self, player, roll):
        print("You rolled a " + str(roll))
        guess = False
        for i in range(0, roll):
            run = True
            while(run):
                direction = str(input("What direction (D, U, L, R)?"))
                if (direction != "D" and direction != "U" and direction != "L" and direction != "R"):
                    print("Invalid direction. Try again.")
                    continue
                row = player.getPosition()[0]
                col = player.getPosition()[1]
                if (direction == "D"):
                    if (self.checkLegalPlacement((row + 1), col) == False):
                        print("Oops! Out of bounds. Try again.")
                        continue
                    else:
                        self.board[row][col] = "-"
                        self.placePlayer(player, (row + 1), col)
                        run = False
                elif (direction == "U"):
                    if (self.checkLegalPlacement((row - 1), col) == False):
                        print("Oops! Out of bounds. Try again.")
                        continue
                    else:
                        self.board[row][col] = "-"
                        self.placePlayer(player, (row - 1), col)
                        run = False
                elif (direction == "L"):
                    if (self.checkLegalPlacement(row, (col - 1)) == False):
                        print("Oops! Out of bounds. Try again.")
                        continue
                    else:
                        self.board[row][col] = "-"
                        self.placePlayer(player, row, (col - 1))
                        run = False
                else:
                    if (self.checkLegalPlacement(row, (col + 1)) == False):
                        print("Oops! Out of bounds. Try again.")
                        continue
                    else:
                        self.board[row][col] = "-"
                        self.placePlayer(player, row, (col + 1))
                        run = False
                self.printBoard()
                if (self.inRoom(player) == True):
                    guess = True
            if (guess == True):
                player.guess()
                break



