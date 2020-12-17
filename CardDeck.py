
from Card import Card
import random

class Deck:
    def __init__(self):  # constructor - makes deck with people, weapons, rooms, a full deck, and the murder cards
        self.people = []
        self.weapons = []
        self.rooms = []
        self.cards = []
        self.murderCards = []

    def build(self):  # fills the people, weapons, and rooms decks
        for p in ["Miss Scarlett", "Colonel Mustard", "Mrs. White", "Mr. Green", "Mrs. Peacock", "Professor Plum"]:
            self.people.append(Card(1, p))
        for w in ["Candlestick", "Dagger", "Lead pipe", "Revolver", "Rope", "Wrench"]:
            self.weapons.append(Card(2, w))
        for r in ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Lounge", "Study"]:
            self.rooms.append(Card(3, r))

    def murder(self):  # murder occurs -- picks murder carsd and removes them from the respective decks
        x = random.randint(0, 5)
        self.murderCards.append(self.people.pop(x))
        x = random.randint(0 , 5)
        self.murderCards.append(self.weapons.pop(x))
        x = random.randint(0 ,5)
        self.murderCards.append(self.rooms.pop(x))

    def fullDeck(self):  # constructs full deck without murder cards
        for c in self.people:
            self.cards.append(c)
        for c in self.weapons:
            self.cards.append(c)
        for c in self.rooms:
            self.cards.append(c)

    def shuffle(self):  # shuffles deck
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, 1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def deal(self, players):  # takes a list of players, deals cards to players
        empty = False
        for x in range(0, len(self.cards) - 1):
            for p in players:
                if (len(self.cards) == 0):
                    empty = True
                    break
                else:
                    p.addCard(self.cards.pop(0))
            if (empty):
                break

    def setUpGame(self, players):
        self.build()
        self.murder()
        self.fullDeck()
        self.shuffle()
        self.deal(players)

    def showMurder(self):
        for c in self.murderCards:
            c.show()

    def checkAccusation(self, person, weapon, room):
        if (self.murderCards[0].getName() == person):
            if (self.murderCards[1].getName() == weapon):
                if (self.murderCards[2].getName() == room):
                    print("You won!")
                    return True
        print("You lose!")
        return False




