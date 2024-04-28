class Room:
    def __init__(self, name, description, interactions):
        self.name = name
        self.description = description
        self.interactions = interactions
    def display_interactions():
        print('Would you like to investivate anything? Your options are:')
        for i in self.interactions:
            print(i)
        print(f'\nIf you do not want to investigate in this room, enter "leave"')
    def print_description():
        print(self.description)

class LockedRoom(Room):
    def __init__(self, name, description, interactions, locked):


