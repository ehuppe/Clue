from Player import Player
from Card import Card
from CardDeck import Deck
from TextBoard import Board

player1 = Player("*")
player2 = Player("+")
player3 = Player("#")
player4 = Player("@")
players = [player1, player2, player3, player4]

deck = Deck()
deck.setUpGame(players)

board = Board()
board.printBoard()

for x in players:
    print(x.getSymbol())
    x.showHand()




