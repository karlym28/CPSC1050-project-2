class Room:
    def __init__(self, description, interactions):
        self.description = description
        self.interactions = interactions
    def display_interactions(self):
        print('Would you like to investivate anything? Your options are:')
        for i in self.interactions:
            print(i)
        print(f'\nEnter "i" to open inventory')
        print(f'If you do not want to investigate anything in this room, enter "leave"')


class LockedRoom(Room):
    def __init__(self, description, interactions, locked, locked_description):
        super().__init__(description, interactions)
        self.locked = True
        self.locked_description = locked_description

    def print_description(self):
        if self.locked == True:
            print(self.locked_description)
        else:
            print(self.description)

class Player:
    def __init__(self):
        self.inventory = []
    
    def display_inventory(self):
        print(f'\n')
        for i in self.inventory:
            print (i)

class Results:
    def __init__(self, file):
        self.rooms_entered = 0
        self.times_interact = 0
        self.main_door_wrong = 0
        self.basement_wrong = 0
        self.attic_wrong = 0
        self.file = file

    def add_rooms_entered(self):
        self.rooms_entered += 1

    def add_times_interact(self):
        self.times_interact += 1
    
    def add_main_door_wrong(self):
        self.main_door_wrong += 1
    
    def add_basement_wrong(self):
        self.basement_wrong += 1

    def add_attic_wrong(self):
        self.attic_wrong += 1

    def make_file(self):
        with open(self.file, 'w') as wompwomp:
            wompwomp.write(f'Rooms entered: {self.rooms_entered}\n')
            wompwomp.write(f'Items investigated: {self.times_interact}\n')
            wompwomp.write(f'Wrong main door guesses: {self.main_door_wrong}\n')
            wompwomp.write(f'Wrong basement guesses: {self.basement_wrong}\n')
            wompwomp.write(f'Wrong attic guesses: {self.attic_wrong}\n')

    def print_file(self):
        with open(self.file) as caffeine:
            for line in caffeine:
                print(line)



        




