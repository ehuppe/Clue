
class Tracker:

    def __init__(self):  # construct tracker with dictionaries for each type of card
        self.people = {"Miss Scarlett": "?",
                       "Colonel Mustard": "?",
                       "Mrs. White": "?",
                       "Mr. Green": "?",
                       "Mrs. Peacock": "?",
                       "Professor Plum": "?"}
        self.weapons = {"Candlestick": "?",
                        "Dagger": "?",
                        "Lead pipe": "?",
                        "Revolver": "?",
                        "Rope": "?",
                        "Wrench": "?"}
        self.rooms = {"Kitchen": "?",
                      "Ballroom": "?",
                      "Conservatory": "?",
                      "Dining Room": "?",
                      "Lounge": "?",
                      "Study": "?"}

    def look(self):  # prints tracker
        print(self.people)
        print(self.weapons)
        print(self.rooms)

    def edit(self, type, name, status):  # edits tracker
        if (type == "p"):
            self.people[name] = status
        elif (type == "w"):
            self.weapons[name] = status
        else:
            self.room[name] = status

