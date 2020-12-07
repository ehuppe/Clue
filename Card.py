
class Card:

    def __init__(self, type, name):  # constructs cards with a type, and a name
        self.type = type  # 1 is person, 2 is weapon, 3 is room
        self.name = name  # name of card

    def getType(self):  # returns type of card
        return self.type

    def getName(self):  # returns name of card
        return self.name

    def show(self):  # shows card
        print(self.name)


