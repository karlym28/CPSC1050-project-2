from proj_2_files import classes


def main():
    #sets varibles
    results = classes.Results('results.txt')
    start = ''
    x = True
    track = classes.Player()
    interact = ''
    room_list = ['bedroom', 'nursery', 'kitchen', 'living room', 'study', 'attic', 'basement', 'main door']
    current_room = ''
    attempt = ''
    code = ''
    view_results = ''
    house = {'bedroom': classes.Room(f'\nYou walk into a bedroom dusted with cobwebs. It seems that whoever decorated did not like furniture, as there is only a \ndresser, mirror, and bed.\n', ['mirror', 'dresser', 'bed']),
    'nursery': classes.Room('\nYou walk into a small animal-themed room containing a crib and changing table.\n', ['crib', 'changing table']),
    'kitchen': classes.Room(f'\nYou walk into a scarcely furnished kitchen. Though the room is small, it feels very spacious. There is plenty of storage\nin the cabinets and a small table with chairs to eat at. However, there is only an oven, no microwave, which is odd.\n', ['cabinet', 'oven', 'table']),
    'living room': classes.Room(f'\nYou enter a very decorated living room filled with dead plants. The TV seems to be stuck playing static. There is also a\ncouch, coffee table, and a family portrait hanging above the TV.\n', ['couch', 'coffee table', 'portrait']),
    'study': classes.Room(f'\nYou enter the study and see a desk, file cabinet, and printer.\n', ['desk', 'file cabinet', 'printer']),
    'attic': classes.LockedRoom(f"\nYou step into the attic and see it's filled with boxes and paintings.\n", ['boxes', 'paintings'], True, f'\nYou walk up to a door at the top of some steps. The door is locked, but it seems like it can be unlocked with a code 4\nnumbers long.\n'),
    'basement': classes.LockedRoom(f"\nYou enter the basement and see it's filled with old furniture. There is a desk, bedframe, and microwave.\n", ['old desk', 'bedframe', 'microwave'], True, f'\nYou descend a flight of steps and find yourself at a locked door. It can be unlocked with a code 3 digits long.\n'),
    'main door': classes.LockedRoom(f'\nYou unlock the door and step out into the sunlight. Before you can enjoy the happiness of freedom, you are shot dead.\nGame Over.', [], True, f'\nYou walk up to the door, longing to escape. It can be unlocked with a five-digit code.\n')}

    #intro to game
    print('Welcome to Code Your Way Out!')
    print('The objective of the game is to find all the notes and unlock doors to escape.')
    print('You can reveal a list of the notes found by enter "i" when asked about investigating or unlocking a door.')
    while start == '':
        print('Enter any key to start')
        start = input()
    print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print(f'You wake up and find yourself on the floor of an old house. Your not sure what happened but you know you need to start\nexploring if you want to make it out')
    
    while x == True:
        #rooms displayed
        interact = ''
        print('Choose a room to explore:')
        for i in room_list:
            print(i)
        
        #user pics a room
        current_room = input().strip().lower()
        while current_room not in room_list:
            print('Please enter valid room')
            current_room = input().strip().lower()
        current_room_object = house[current_room]
        
        #room description
        if current_room == 'main door':
            current_room_object.print_description()
            attempt = ''
            if current_room_object.locked == True:
                while attempt != 'n':
                    print('Would you like to unlock the door?(enter y or n)')
                    print('or "i" if you want to open inventory')
                    attempt = input().lower().strip()
                    while attempt not in ['y', 'n', 'i']:
                        print(f'\nPlease enter valid input')
                        attempt = input().lower().strip()
                    if attempt == 'i':
                        track.display_inventory()
                    if attempt == 'y':
                        print('Please enter the code, it should be 5 digits long')
                        code = input().lower().strip()
                        if code == '73952':
                            current_room_object.locked = False
                            current_room_object.print_description()
                            print(f'\nWould you like to view your results? (y or n)')
                            view_results = input().lower().strip()
                            while view_results not in ['y', 'n']:
                                print(f'\nPlease enter valid input')
                                view_results = input().lower().strip()
                            if view_results == 'y':
                                results.make_file()
                                results.print_file()
                                exit()
                            else:
                                results.make_file()
                                exit()

                        else:
                            print('The door did not unlock')
                            results.add_main_door_wrong()
                     
        elif current_room == 'basement':
            if current_room_object.locked == True:
                current_room_object.print_description()
                attempt = ''
                while attempt != 'n':
                    print('Would you like to unlock the door?(enter y or n)')
                    print('or "i" if you want to open inventory')
                    attempt = input().lower().strip()
                    while attempt not in ['y', 'n', 'i']:
                        print(f'\nPlease enter valid input')
                        attempt = input().lower().strip()
                    if attempt == 'i':
                        track.display_inventory()
                    if attempt == 'y':
                        print('Please enter the code, it should be 3 digits long')
                        code = input().lower().strip()
                        if code == '861':
                            current_room_object.locked = False
                            print(f'The door unlocked\n')
                            break
                        else:
                            print('That is not the code')
                            results.add_basement_wrong
            if current_room_object.locked == False:
                results.add_rooms_entered()
                current_room_object.print_description()
                while interact != 'leave':
                    current_room_object.display_interactions()
                    interact = input().lower().strip()
                    while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                        print('Please enter valid input')
                        interact = input().lower().strip()
                    if interact == 'i':
                        track.display_inventory()
                    elif interact == 'old desk':
                        results.add_times_interact()
                        print(f'\nThere is not much to it. Just a table really. You notice the wood was once beautiful though.\n')
                    elif interact == 'bedframe':
                        results.add_times_interact()
                        print(f'\nMost of it is broken. Still, you check for any hints but as you suspected, there is nothing.\n')
                    elif interact == 'microwave':
                        results.add_times_interact()
                        if '4826' in track.inventory:
                            print(f'\nYou stare at the broken microwave on the floor\n')
                        else:
                            print(f'\nYou decide to smash the microwave because why not. Its a good thing you did because there was a piece of paper in it. It\nhas “4826” written on it')
                            print('4826 added to inventory\n')
                            track.inventory.append('4826')

        elif current_room == 'attic':
            if current_room_object.locked == True:
                current_room_object.print_description()
                attempt = ''
                while attempt != 'n':
                    print('Would you like to unlock the door?(enter y or n)')
                    print('or "i" if you want to open inventory')
                    attempt = input().lower().strip()
                    while attempt not in ['y', 'n', 'i']:
                        print(f'\nPlease enter valid input')
                        attempt = input().lower().strip()
                    if attempt == 'i':
                        track.display_inventory()
                    if attempt == 'y':
                        print('Please enter the code, it should be 4 digits long')
                        code = input().lower().strip()
                        if code == '4826':
                            current_room_object.locked = False
                            print(f'The door is unlocked\n')
                            break
                        else:
                            print(f'That is not the code\n')
                            results.add_attic_wrong
            if current_room_object.locked == False:
                results.add_rooms_entered()
                current_room_object.print_description()
                while interact != 'leave':
                    current_room_object.display_interactions()
                    interact = input().lower().strip()
                    while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                        print('Please enter valid input')
                        interact = input().lower().strip()
                    if interact == 'i':
                        track.display_inventory()
                    elif interact == 'boxes':
                        results.add_times_interact()
                        print(f'\nYou check the boxes and see they are filled with old clothes and miscellaneous items\n')
                    elif interact == 'paintings':
                        results.add_times_interact()
                        if '39' in track.inventory:
                            print(f'\nYou already found this note\n')
                        else:
                            print(f'\nYou search the paintings and find a small piece of paper tucked in between the canvas and frame. It has the number “39” on\nit')
                            print('39 added to inventory\n')
                            track.inventory.append('39')

        elif current_room == 'bedroom':
            results.add_rooms_entered()
            print(current_room_object.description)
            while interact != 'leave':
                current_room_object.display_interactions()
                interact = input().lower().strip()
                while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                    print(f'\nPlease enter valid input')
                    interact = input().lower().strip()
                if interact == 'i':
                    track.display_inventory()
                if interact == 'mirror':
                    results.add_times_interact()
                    if '17' in track.inventory:
                        print(f'\nYou already found the note\n')
                    else:
                        print(f'\nAs you inspect the mirror a bug crawls on you, causing you to jump and knock the mirror over, revealing a note taped to the \nback. You pick up the note and read it. It has the number “17” on it.\n')
                        print('17 added to inventory\n')
                        track.inventory.append('17')
                elif interact == 'dresser':
                    results.add_times_interact()
                    print(f'\nYou open the drawer revealing an old picture of a family. Two parents and a baby. It gives you an uneasy feeling because all the eyes are cut out.\n')
                elif interact == 'bed':
                    results.add_times_interact()
                    print(f"\nAs you walk up to the tattered bed, you decide it's best left alone.\n")

        elif current_room == 'nursery':
            results.add_rooms_entered()
            print(current_room_object.description)
            while interact != 'leave':
                current_room_object.display_interactions()
                interact = input().lower().strip()
                while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                    print(f'\nPlease enter valid input')
                    interact = input().lower().strip()
                if interact == 'i':
                    track.display_inventory()
                elif interact == 'crib':
                    results.add_times_interact()
                    print(f'\nThe crib is filled with an absurd amount of stuffed animals. You dig through the collection and find nothing.\n')
                elif interact == 'changing table':
                    results.add_times_interact()
                    if '23' in track.inventory:
                        print(f'\nYou already found the note\n')
                    else:
                        print(f'\nYou search the changing table and find a note under the mat. It has “23” written on it.')
                        print('23 added to inventory\n')
                        track.inventory.append('23')

        elif current_room == 'kitchen':
            results.add_rooms_entered()
            print(current_room_object.description)
            while interact != 'leave':
                current_room_object.display_interactions()
                interact = input().lower().strip()
                while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                    print(f'\nPlease enter valid input')
                    interact = input().lower().strip()
                if interact == 'i':
                    track.display_inventory()
                elif interact == 'cabinet':
                    results.add_times_interact()
                    print(f'\nYou search through the cabinet and find nothing but expired sardines.\n')
                elif interact == 'oven':
                    results.add_times_interact()
                    print(f'\nYou open the oven to a horrendous smell. It seems there are still remnants of the last meal cooked.\n')
                elif interact == 'table':
                    results.add_times_interact()
                    if '861' in track.inventory:
                        print(f'\nYou already found the note\n')
                    else:
                        print(f'\nYou thoroughly search the table and chairs and find a note taped under a chair. It has “861” written on it.')
                        print('861 added to inventory\n')
                        track.inventory.append('861')

        elif current_room == 'living room':
            results.add_rooms_entered()
            print(current_room_object.description)
            while interact != 'leave':
                current_room_object.display_interactions()
                interact = input().lower().strip()
                while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                    print(f'\nPlease enter valid input')
                    interact = input().lower().strip()
                if interact == 'i':
                    track.display_inventory()
                elif interact == 'couch':
                    results.add_times_interact()
                    print(f'\nThe couch is covered in tears and claw marks. It seems the couch once belonged to a cat owner.\n')
                elif interact == 'coffee table':
                    results.add_times_interact()
                    if '45' in track.inventory:
                        print(f'\nYou already found the note\n')
                    else:
                        print(f'\nThere are two drawers. You open the first one and find nothing. The second, however, contains a note with “45” written on it.')
                        print('45 added to inventory\n')
                        track.inventory.append('45')
                elif interact == 'portrait':
                    results.add_times_interact()
                    print(f'\nThe painted family almost seems to be staring at you, watching.\n')

        elif current_room == 'study':
            results.add_rooms_entered()
            print(current_room_object.description)
            while interact != 'leave':
                current_room_object.display_interactions()
                interact = input().lower().strip()
                while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                    print(f'\nPlease enter valid input')
                    interact = input().lower().strip()
                if interact == 'i':
                    track.display_inventory()
                elif interact == 'desk':
                    results.add_times_interact()
                    print(f'\nYou open the desk drawer and are blessed with the site of hundreds of small spiders. You close it immediately.\n')
                elif interact == 'file cabinet':
                    results.add_times_interact()
                    if '52' in track.inventory:
                        print(f'\nYou already found this item\n')
                    else:
                        print(f'\nYou open all the drawers and find nothing. You check the top of the cabinet and find “52” written on a small piece of\npaper.')
                        print('52 added to inventory\n')
                        track.inventory.append('52')
                elif interact == 'printer':
                    results.add_times_interact()
                    print(f'\nYou check the printer only to find some coloring sheets that were printed a long time ago.\n')

    

if __name__ == '__main__':
    main()


