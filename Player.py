
from Card import Card

from CardDeck import Deck

from Tracker import Tracker

import random

class Player:

    def __init__(self, symbol):  # constructs player with hand,
        self.hand = []
        self.tracker = Tracker()
        self.position = [4, random.randint(0, 11)]
        self.symbol = symbol

    def getSymbol(self):
        return self.symbol

    def getPosition(self):
        return self.position

    def getHand(self):
        return self.hand

    def changePosition(self, x, y):
        self.position = [x, y]

    def rollDice(self):
        return random.randint(1, 7)

    def addCard(self, card):  # adds card to hand
       self.hand.append(card)

    def editTracker(self, type, name, status):  # edits tracker
        self.tracker.edit(type, name, status)

    def checkTracker(self):  # looks at tracker
        self.tracker.look()

    def showHand(self):
        for x in self.hand:
            x.show()

    def accuse(self, deck):  # makes final accusation
        self.checkTracker()
        person = str(input("What suspect is your final accusation?"))
        weapon = str(input("What weapon is your final accusation?"))
        room = str(input("What room is your final accusation?"))

    def guess(self):
        person = str(input("Suspect?"))
        weapon = str(input("Weapon?"))
        #room =


