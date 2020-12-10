
import Card

import CardDeck

import Tracker

import random

class Player:

    def __init__(self):  # constructs player with hand,
        self.hand = []
        self.tracker = Tracker()
        self.position[]

    def addCard(self, card):  # adds card to hand
       self.hand.append(card)

    def editTracker(self, type, name, status):  # edits tracker
        self.tracker.edit(type, name, status)

    def checkTracker(self):  # looks at tracker
        self.tracker.look()

    def guess(self, person, weapon, room):  # makes a guess
        pass

    def accuse(self, deck):  # makes final accusation
        self.checkTracker()
        person = str(input("What suspect is your final accusation?"))
        weapon = str(input("What weapon is your final accusation?"))
        room = str(input("What room is your final accusation?"))

    def guess(self):
        person = str(input("Suspect?"))
        weapon = str(input("Weapon?"))
        room =


