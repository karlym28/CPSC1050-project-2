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
    
    #infinite loop, program ends when exit() is called
    while x == True:
        #rooms displayed
        interact = ''
        print('Choose a room to explore:')
        for i in room_list:
            print(i)
        
        #user input a room and is checked for valid input
        current_room = input().strip().lower()
        while current_room not in room_list:
            print('Please enter valid room')
            current_room = input().strip().lower()
        current_room_object = house[current_room]
        
        #runs if user want to enter main door
        if current_room == 'main door':
            #prints main door locked description and resets attempt
            current_room_object.print_description()
            attempt = ''

        #If main door is locked, this runs
            if current_room_object.locked == True:
                #runs until user enter "n" for attempt
                while attempt != 'n':
                    #gets users input and checks, repeates until users input is valid
                    print('Would you like to unlock the door?(enter y or n)')
                    print('or "i" if you want to open inventory')
                    attempt = input().lower().strip()

                    while attempt not in ['y', 'n', 'i']:
                        print(f'\nPlease enter valid input')
                        attempt = input().lower().strip()

                    #is user enter "i", prints inventory
                    if attempt == 'i':
                        track.display_inventory()

                    #if user enters y, gets users guess for main door code
                    if attempt == 'y':
                        print('Please enter the code, it should be 5 digits long')
                        code = input().lower().strip()

                    #if code is correct runs
                        if code == '73952':
                            #prints main door unlocked description and ask if user wants to view results
                            current_room_object.locked = False
                            current_room_object.print_description()
                            print(f'\nWould you like to view your results? (y or n)')
                            view_results = input().lower().strip()

                            #runs until user enters valid input
                            while view_results not in ['y', 'n']:
                                print(f'\nPlease enter valid input')
                                view_results = input().lower().strip()

                            #if user enters 'y', writes in txt file and prints the file, exits the program after
                            if view_results == 'y':
                                results.make_file()
                                results.print_file()
                                exit()
                            #if user enters'n', writes in txt file and exits the program
                            else:
                                results.make_file()
                                exit()
                        #if code is incorrect, adds 1 to main_door_wrong_guesses
                        else:
                            print('The door did not unlock')
                            results.add_main_door_wrong()

        #runs if user wants to enter basement     
        elif current_room == 'basement':
            #runs if basement door is locked
            if current_room_object.locked == True:

                #prints basement locked decription and resets the varible attempt
                current_room_object.print_description()
                attempt = ''

                #runs until user enter 'n' for attempt
                while attempt != 'n':
                    #gets users input and checks, repeates until users input is valid
                    print('Would you like to unlock the door?(enter y or n)')
                    print('or "i" if you want to open inventory')
                    attempt = input().lower().strip()
                    while attempt not in ['y', 'n', 'i']:
                        print(f'\nPlease enter valid input')
                        attempt = input().lower().strip()
                    
                    #runs if statement based of users input for attempt
                    if attempt == 'i':
                        track.display_inventory()

                    if attempt == 'y':
                        #gets users guess for code
                        print('Please enter the code, it should be 3 digits long')
                        code = input().lower().strip()

                        #if guess is correct, unlocks door, else add 1 to basement_wrong
                        if code == '861':
                            current_room_object.locked = False
                            print(f'The door unlocked\n')
                            break
                        else:
                            print('That is not the code')
                            results.add_basement_wrong

            #runs if room is unlocked
            if current_room_object.locked == False:
                #adds 1 to rooms entered and prints room description
                results.add_rooms_entered()
                current_room_object.print_description()

                #runs until interact == 'leave
                while interact != 'leave':
                    #displays interactions and gets valid input from user
                    current_room_object.display_interactions()
                    interact = input().lower().strip()
                    while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                        print('Please enter valid input')
                        interact = input().lower().strip()

                    #runs one if statement based of what interact is
                    if interact == 'i':
                        track.display_inventory()

                    #adds one to times_interact and prints interaction dialoge
                    elif interact == 'old desk':
                        results.add_times_interact()
                       
                        print(f'\nThere is not much to it. Just a table really. You notice the wood was once beautiful though.\n')
                    elif interact == 'bedframe':
                        results.add_times_interact()
                        print(f'\nMost of it is broken. Still, you check for any hints but as you suspected, there is nothing.\n')
                    
                    elif interact == 'microwave':
                        results.add_times_interact()
                        
                        #decides what dialouge to print based off if the user found the note or not
                        if '4826' in track.inventory:
                            print(f'\nYou stare at the broken microwave on the floor\n')
                        else:
                            print(f'\nYou decide to smash the microwave because why not. Its a good thing you did because there was a piece of paper in it. It\nhas “4826” written on it')
                            print('4826 added to inventory\n')
                            track.inventory.append('4826')

        #runs if user want to enter attic
        elif current_room == 'attic':
            #runs if room is unlocked
            if current_room_object.locked == True:
                #prints locked room description and resets the varible attempt
                current_room_object.print_description()
                attempt = ''

                #runs until attempt is 'n'
                while attempt != 'n':
                    #ask user for attempt and checks for valid input
                    print('Would you like to unlock the door?(enter y or n)')
                    print('or "i" if you want to open inventory')
                    attempt = input().lower().strip()
                    while attempt not in ['y', 'n', 'i']:
                        print(f'\nPlease enter valid input')
                        attempt = input().lower().strip()

                    #runs if statement based off users input for attempt
                    if attempt == 'i':
                        track.display_inventory()
                    
                    if attempt == 'y':
                        #gets users guess for code
                        print('Please enter the code, it should be 4 digits long')
                        code = input().lower().strip()

                        #if code is correct, unlocks room, else adds 1 to attic_wrong
                        if code == '4826':
                            current_room_object.locked = False
                            print(f'The door is unlocked\n')
                            break
                        else:
                            print(f'That is not the code\n')
                            results.add_attic_wrong

            #runs is attic is unlocked
            if current_room_object.locked == False:
                #prints unlock decription and adds 1 to rooms_entered
                results.add_rooms_entered()
                current_room_object.print_description()

                #runs until interact is 'leave'
                while interact != 'leave':
                    #displays interactions and ask for input, check for valid input
                    current_room_object.display_interactions()
                    interact = input().lower().strip()
                    while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                        print('Please enter valid input')
                        interact = input().lower().strip()

                    #runs one if statement based of what interact is
                    if interact == 'i':
                        track.display_inventory()

                    #adds 1 to times_interact, and prints interaction dialoge
                    elif interact == 'boxes':
                        results.add_times_interact()
                        print(f'\nYou check the boxes and see they are filled with old clothes and miscellaneous items\n')
                    
                    elif interact == 'paintings':
                        #prints dialoge based of if the user found the note
                        results.add_times_interact()
                        if '39' in track.inventory:
                            print(f'\nYou already found this note\n')
                        else:
                            print(f'\nYou search the paintings and find a small piece of paper tucked in between the canvas and frame. It has the number “39” on\nit')
                            print('39 added to inventory\n')
                            track.inventory.append('39')

        #runs if user wants to enter bedroom
        elif current_room == 'bedroom':
            #adds 1 to rooms_entered and prints room decription
            results.add_rooms_entered()
            print(current_room_object.description)

            #runs until interact is 'leave'
            while interact != 'leave':
                #displays interactions and confirms input is valid
                current_room_object.display_interactions()
                interact = input().lower().strip()
                while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                    print(f'\nPlease enter valid input')
                    interact = input().lower().strip()
                
                #runs 1 if statment based of interact
                if interact == 'i':
                    track.display_inventory()
                
                #adds 1 to interaction and prints interaction dialoge
                elif interact == 'mirror':
                    results.add_times_interact()
                    #deciced what dialoge to print based of if user found note
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

        #runs if user wants to enter nursery
        elif current_room == 'nursery':
            #adds 1 to rooms_entered and prints room decription
            results.add_rooms_entered()
            print(current_room_object.description)

            #runs until interact = leave
            while interact != 'leave':
                #displays interaction and gets users input, confirms its valid
                current_room_object.display_interactions()
                interact = input().lower().strip()
                while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                    print(f'\nPlease enter valid input')
                    interact = input().lower().strip()
                
                #runs 1 if statment based off interact
                if interact == 'i':
                    track.display_inventory()
                
                #adds 1 to times_inteeract and prints interaction dialoge
                elif interact == 'crib':
                    results.add_times_interact()
                    print(f'\nThe crib is filled with an absurd amount of stuffed animals. You dig through the collection and find nothing.\n')
                
                elif interact == 'changing table':
                    results.add_times_interact()
                    #prints dialoge based of user found note
                    if '23' in track.inventory:
                        print(f'\nYou already found the note\n')
                    else:
                        print(f'\nYou search the changing table and find a note under the mat. It has “23” written on it.')
                        print('23 added to inventory\n')
                        track.inventory.append('23')

        #runs if user want to enter kitchen
        elif current_room == 'kitchen':
            #prints room desciption and adds 1 to rooms_entered
            results.add_rooms_entered()
            print(current_room_object.description)

            #runs until interact is 'leave'
            while interact != 'leave':
                #prints interactions and get users input, confirms its valid
                current_room_object.display_interactions()
                interact = input().lower().strip()
                while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                    print(f'\nPlease enter valid input')
                    interact = input().lower().strip()

                #runs 1 if statment based off interact
                if interact == 'i':
                    track.display_inventory()

                #prints interaction dialoge and adds 1 to times_interact
                elif interact == 'cabinet':
                    results.add_times_interact()
                    print(f'\nYou search through the cabinet and find nothing but expired sardines.\n')
                
                elif interact == 'oven':
                    results.add_times_interact()
                    print(f'\nYou open the oven to a horrendous smell. It seems there are still remnants of the last meal cooked.\n')
                
                elif interact == 'table':
                    results.add_times_interact()
                    #prints dialoge based off if user found note
                    if '861' in track.inventory:
                        print(f'\nYou already found the note\n')
                    else:
                        print(f'\nYou thoroughly search the table and chairs and find a note taped under a chair. It has “861” written on it.')
                        print('861 added to inventory\n')
                        track.inventory.append('861')

        #runs if user wants to enter living room
        elif current_room == 'living room':
            #prints room description and adds 1 to rooms_entered
            results.add_rooms_entered()
            print(current_room_object.description)

            #runs until interact is leave
            while interact != 'leave':
                #prints interaction and get users input, ensures its valid
                current_room_object.display_interactions()
                interact = input().lower().strip()
                while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                    print(f'\nPlease enter valid input')
                    interact = input().lower().strip()

                #runs 1 if statment based off interact
                if interact == 'i':
                    track.display_inventory()

                #adds 1 to times_interact and prints interaction dialoge
                elif interact == 'couch':
                    results.add_times_interact()
                    print(f'\nThe couch is covered in tears and claw marks. It seems the couch once belonged to a cat owner.\n')
                
                elif interact == 'coffee table':
                    results.add_times_interact()
                    #prints dialoge based off if user found note
                    if '45' in track.inventory:
                        print(f'\nYou already found the note\n')
                    else:
                        print(f'\nThere are two drawers. You open the first one and find nothing. The second, however, contains a note with “45” written on it.')
                        print('45 added to inventory\n')
                        track.inventory.append('45')
                
                elif interact == 'portrait':
                    results.add_times_interact()
                    print(f'\nThe painted family almost seems to be staring at you, watching.\n')

        #runs if user wants to enter study
        elif current_room == 'study':
            #prints room desciption and adds 1 to rooms_entered
            results.add_rooms_entered()
            print(current_room_object.description)

            #runs until interact is leave
            while interact != 'leave':
                #prints interactions and get users input, ensures its valid
                current_room_object.display_interactions()
                interact = input().lower().strip()
                while (interact not in current_room_object.interactions) and (interact != 'i') and (interact != 'leave'):
                    print(f'\nPlease enter valid input')
                    interact = input().lower().strip()

                #runs 1 if statment based off interact
                if interact == 'i':
                    track.display_inventory()

                #adds 1 to times_interact and prints interaction dialoge
                elif interact == 'desk':
                    results.add_times_interact()
                    print(f'\nYou open the desk drawer and are blessed with the site of hundreds of small spiders. You close it immediately.\n')
                
                elif interact == 'file cabinet':
                    results.add_times_interact()
                    #prints dialouge based off if user found note
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


