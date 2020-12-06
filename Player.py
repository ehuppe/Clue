
import Card

import CardDeck

import random

class Player:
    def __init__(self):
        self.hand = []

    def drawCard(self, card):
       self.hand.append(card)

