
import random

class Board:

    def __init__(self): # constructor - includes a board to be played on, as well as a template board
        self.board = [["k", "k", "k", "k", "b", "b", "b", "b", "c", "c", "c", "c"],
                      ["k", "k", "k", "k", "b", "b", "b", "b", "c", "c", "c", "c"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["d", "d", "d", "d", "l", "l", "l", "l", "s", "s", "s", "s"],
                      ["d", "d", "d", "d", "l", "l", "l", "l", "s", "s", "s", "s"]]
        self.boardTemplate = [["k", "k", "k", "k", "b", "b", "b", "b", "c", "c", "c", "c"],
                      ["k", "k", "k", "k", "b", "b", "b", "b", "c", "c", "c", "c"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["d", "d", "d", "d", "l", "l", "l", "l", "s", "s", "s", "s"],
                      ["d", "d", "d", "d", "l", "l", "l", "l", "s", "s", "s", "s"]]

    def printBoard(self): # prints board
        for r in self.board:  # nested loop to print element
            for c in r:
                print(c, end=" ")
            print()

    def setUpGame(self, players): # sets up game, places players on the board
        for player in players:  # places each player
            row = player.getPosition()[0]
            col = player.getPosition()[1]
            if (self.board[row][col] == "-"):  # if space is empty
                self.placePlayer(player, row, col)
            else:
                while (self.board[row][col] != "-"):  # until space is empty
                    newCol = random.randint(0, 11)
                    if (self.board[row][newCol] == "-"):  # if space is empty
                        self.placePlayer(player, row, newCol)

    def placePlayer(self, player, row, col): # places a player at a given position on the board
        self.board[row][col] = player.getSymbol()
        player.changePosition(row , col)

    def checkLegalPlacement(self, row, col): # checks if a players placement is legal (within bounds, open space)
        if (col > 11 or col < 0):  # if out of bounds
            return False
        elif (row > 8 or row < 0):  # if out of bounds
            return False
        elif (self.board[row][col] != "-"):  # if space is filled
            for i in ["k", "b", "c", "d", "l", "s"]:  # if filled with room
                if (self.board[row][col] == i):
                    return True
            return False
        else:
            return True

    def inRoom(self, player): # checks if a player has entered a room
        row = player.getPosition()[0]
        if (row < 2 or row > 6):  # if player in room
            return True
        else:
            return False

    def move(self, players, player, roll, deck): # makes a move (including guesses and possible accusations)
        print("You rolled a " + str(roll))
        guess = False
        for i in range(0, roll):  # loops through roll
            run = True
            while(run):  # running loop
                direction = str(input("What direction (D, U, L, R)?"))
                if (direction != "D" and direction != "U" and direction != "L" and direction != "R"):  # if direction is invalid
                    print("Invalid direction. Try again.")
                    continue
                row = player.getPosition()[0]
                col = player.getPosition()[1]
                if (direction == "D"):  # if down
                    if (self.checkLegalPlacement((row + 1), col) == False):  # if illegal
                        print("Oops! Out of bounds. Try again.")
                        continue
                    else:
                        self.board[row][col] = self.boardTemplate[row][col]
                        self.placePlayer(player, (row + 1), col)
                        run = False
                elif (direction == "U"):  # if up
                    if (self.checkLegalPlacement((row - 1), col) == False):  # if illegal
                        print("Oops! Out of bounds. Try again.")
                        continue
                    else:
                        self.board[row][col] = self.boardTemplate[row][col]
                        self.placePlayer(player, (row - 1), col)
                        run = False
                elif (direction == "L"):  # if left
                    if (self.checkLegalPlacement(row, (col - 1)) == False):  # if illegal
                        print("Oops! Out of bounds. Try again.")
                        continue
                    else:
                        self.board[row][col] = self.boardTemplate[row][col]
                        self.placePlayer(player, row, (col - 1))
                        run = False
                else:  # if right
                    if (self.checkLegalPlacement(row, (col + 1)) == False):  # if illegal
                        print("Oops! Out of bounds. Try again.")
                        continue
                    else:
                        self.board[row][col] = self.boardTemplate[row][col]
                        self.placePlayer(player, row, (col + 1))
                        run = False
                self.printBoard()
                if (self.inRoom(player) == True):  # if player entered a room
                    guess = True
                    break
            if (guess == True):  # if entered room, makes guess
                print("You entered a room! Make a guess.")
                player.guess(players)
                break
        checkTracker = str(input("Would you like to edit your tracker?"))
        if (checkTracker == "yes" or checkTracker == "Yes"):  # if player wants to edit tracker
            player.checkTracker()
            type = str(input("Type? 1 = person, 2 = weapon, 3 = room"))
            name = str(input("What person/weapon/room?"))
            status = str(input("What status?"))
            player.editTracker(type, name, status)
        accuse = str(input("Are you ready to make an accusation?"))
        if (accuse == "yes" or accuse == "Yes"):  # if player is ready to make accusation
            return player.accuse(deck)
        else:
            return False


