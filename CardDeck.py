
import Card
import random

class Deck:
    def __init__(self):
        self.people = []
        self.weapons = []
        self.rooms = []
        self.cards = []
        self.murder = []

    def build(self):
        for p in ["Miss Scarlett", "Colonel Mustard", "Mrs. White", "Mr. Green", "Mrs. Peacock", "Professor Plum"]:
            self.people.append(Card(1, p))
        for w in ["Candlestick", "Dagger", "Lead pipe", "Revolver", "Rope", "Wrench"]:
            self.weapons.append(Card(2, w))
        for r in ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Lounge", "Study"]:
            self.rooms.append(Card(3, r))

    def murder(self):
        x = random.randint(0, 5)
        self.murder.append(self.people.pop(x))
        x = random.randint(0 , 5)
        self.murder.append(self.weapons.pop(x))
        x = random.randint(0 ,5)
        self.murder.append(self.rooms.pop(x))

    def fullDeck(self):
        for c in self.people:
            self.cards.append(c)
        for c in self.weapons:
            self.cards.append(c)
        for c in self.rooms:
            self.cards.append(c)

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, 1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def deal(self, players):
        for x in len(self.cards):
            for p in len(players):
                players[p].drawCard(self.cards.pop())




