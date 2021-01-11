
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
        for p in ["Miss Scarlett", "Colonel Mustard", "Mrs. White", "Mr. Green", "Mrs. Peacock", "Professor Plum"]:  # fills in people
            self.people.append(Card(1, p))
        for w in ["Candlestick", "Dagger", "Lead pipe", "Revolver", "Rope", "Wrench"]:  # fills in weapons
            self.weapons.append(Card(2, w))
        for r in ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Lounge", "Study"]:  # fills in rooms
            self.rooms.append(Card(3, r))

    def murder(self):  # murder occurs -- picks murder cards and removes them from the respective decks
        x = random.randint(0, 5)
        self.murderCards.append(self.people.pop(x))
        x = random.randint(0 , 5)
        self.murderCards.append(self.weapons.pop(x))
        x = random.randint(0 ,5)
        self.murderCards.append(self.rooms.pop(x))

    def fullDeck(self):  # constructs full deck without murder cards
        for c in self.people:  # adds people
            self.cards.append(c)
        for c in self.weapons:  # adds weapons
            self.cards.append(c)
        for c in self.rooms:  # adds rooms
            self.cards.append(c)

    def shuffle(self):  # shuffles deck
        for i in range(len(self.cards) - 1, 0, -1):  # shuffles deck
            r = random.randint(0, 1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def deal(self, players):  # takes a list of players, deals cards to players
        empty = False
        for x in range(0, len(self.cards) - 1):  # deals all the cards
            for p in players:  # deals to each player
                if (len(self.cards) == 0):  # if no cards left
                    empty = True
                    break
                else:
                    p.addCard(self.cards.pop(0))
            if (empty):  # when deck is empty
                break

    def setUpGame(self, players): # combines all necessary methods to set up the game
        self.build()
        self.murder()
        self.fullDeck()
        self.shuffle()
        self.deal(players)

    def showMurder(self): # shows murder cards -- for editing purposes
        for c in self.murderCards:  # shows cards in murder
            c.show()

    def checkAccusation(self, person, weapon, room): # checks if a player's accusation is correct
        if (self.murderCards[0].getName() == person):  # if person is correct
            if (self.murderCards[1].getName() == weapon):  # if weapon is correct
                if (self.murderCards[2].getName() == room):  # if room is correct
                    print("You won!")
                    return True
        print("You lose!")
        return False




