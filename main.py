from Player import Player
from CardDeck import Deck
from TextBoard import Board

player1 = Player("1")
player2 = Player("2")
player3 = Player("3")
player4 = Player("4")
players = [player1, player2, player3, player4]

deck = Deck()
deck.setUpGame(players)

for x in players:
    for y in x.getHand():
        x.editTracker(y.getType(), y.getName(), "X")

board = Board()
board.setUpGame(players)
board.printBoard()
deck.showMurder()

run = True
while(run):
    for player in players:
        print("Player " + player.getSymbol() + "'s turn!")
        game = board.move(players, player, player.rollDice(), deck)
        if (game == True):
            run = False
            break






