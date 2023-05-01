#!/usr/bin/python3
import images
import os
import time
import random

# Replace RPG starter project with this code when new instructions are live
images.title()
time.sleep(5)
os.system("clear")

steel_count = 0
iron_count = 0
tin_count = 0
pewter_count = 0


def showInstructions():
    # print a main menu and the commands
    print('''
Mistborn (A Brandon Sanderson fan-fiction Text-Based RPG)
========
Commands:
  go [direction]
  get [item]
  burn [metal that was ingested]: one word command
  push [if steel burned]
  pull [if iron burned]
  boost [if pewter burned]: one word command
  drink [from an item]
  back [to go back to previous room]
''')


def backstory():
    print("""For a thousand years the ash fell and no flowers bloomed. For a thousand years the Skaa slaved in misery and lived in fear. For a thousand years the Lord Ruler, the "Sliver of Infinity," reigned with absolute power and ultimate terror, divinely invincible. Then, when hope was so long lost that not even its memory remained, a terribly scarred, heart-broken half-Skaa rediscovered it in the depths of the Lord Ruler's most hellish prison. Kelsier "snapped" and found in himself the powers of a Mistborn. A brilliant thief and natural leader, he turned his talents to the ultimate caper, with the Lord Ruler himself as the mark.

Kelsier recruited the underworld's elite, the smartest and most trustworthy allomancers, each of whom shares one of his many powers, and all of whom relish a high-stakes challenge. Only then does he reveal his ultimate dream, not just the greatest heist in history, but the downfall of the divine despot.

But even with the best criminal crew ever assembled, Kel's plan looks more like the ultimate long shot, until luck brings a ragged girl named Vin into his life. 


You are Vin, and find yourself locked away after a mission gone horribly wrong. You wake up in a cell.

"I need to get out."  
""")

    input("Press Enter to continue...")


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print(rooms[currentRoom]['description'])
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("Type help if you need instructions again.")
    print("---------------------------")


# an inventory, which is initially empty
inventory = []
metals = ['steel', 'iron', 'pewter']
# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
rooms = {

    'Cell': {
        'description': 'Thick steel bars block your exit to the south.\nThrough the bars is a sleeping guard and beyond him is a staircase leading up.\nIn your cell is a bucket to do your business in, and a straw mat.\nStarving you might be on your captor\'s agenda but they did leave you a cup of water.',
        'exits': {
            'south': 'Guard\'s Room'},
        'item': 'cup',
        'locked': True,
        'metal': 'bars',
        'clear': True
    },
    'Guard\'s Room': {
        'description': 'A simple desk for a guard to set his dinner, stairs leading up, and the guard occupy the room.\n A key ring hangs on the guard\'s belt.',
        'exits': {
            'north': 'Cell',
            'up': 'Stairs'
        },
        'person': 'guard',
        'item': 'keys',
        'metal': 'keys',
        'locked': False,
        'clear': False
    },
    'Stairs': {
        'description': 'A single guard carries a tray of food down the stairs, and you catch them unaware.\nA bag hangs from the belt of the guard. \nYou need to keep going up.',
        'exits': {
            'up': 'Hall',
            'down': 'Guard\'s Room'},

        'item': 'coins',
        'person': 'guard',
        'metal': 'coins',
        'clear': False,
        'locked': False,
    },
    'Hall': {
        'description': 'An empty hallway running east to west.\n You see bright lights illuminating the end of the hall to the east.\nThe west is dimly lit by slow burning candles.\n With two guards taken care of below, you are aware it\'s not going to be easy to escape.',
        'exits': {
            'east': 'Grand Hall',
            'west': 'Guard Tower',
            'down': 'Stairs'
        },
        'clear': True,
        'locked': False
    },
    'Grand Hall': {
        'description': 'A gleaming crystal chandelier hangs in the middle of the Grand Hall, but that is not the first thing you notice.\n50 of the top noblemen and women of Luthadel and surrounding Scadriel cities.\nBarring the doors to the keep are four Obligators, spikes piercing their eyes, and yes, they notice you.',
        'death': 'obligator',
        'clear': False,
        'locked': False,
    },
    'Guard Tower': {
        'description': 'A wooden door blocks the way into the tower.\nIf I can get to a window up high, I can escape.',
        'exits': {
            'up': 'Landing',
            'east': 'Hall'},
        'clear': True,
        'locked': True
    },
    'Landing': {
        'description': 'Halfway up the tower a door opens up to a landing. \nThe room\'s furniture is arranged in an office style and at a desk is large, bald beast of a man. He looks up in shock. Clearly he was not expecting you to be out of your cell. He calls over to you as he readies himself to subdue you. "You should have stayed in the cell.\nNow, the pain you feel will leave you wishing you were dead. When I\'m through with you, the Obligators downstairs will be happy to take you to the Ministry of Steel. \nThey\'ll start with spikes driven through your wrists, and then work their way up.\n\nNow! Feel the pain, you little half-breed!"',
        'exits': {
            'up': 'Tower Window',
            'down': 'Landing'},
        'metal': 'vial',
        'item': 'vial',
        'person': 'Captain of the Guard',
        'clear': False
    },
    'Tower Window': {
        'description': 'The city of Luthadel sprawls outward with torches illuminating the street corners and the mists crawling to fill the night air.',
        'clear': True

    }
}

# start the player in the Hall
currentRoom = 'Cell'
previousRoom = ''
backstory()
showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)
    os.system('clear')

    if move[0] == "back":
        # If the previous room is not empty, go back to the previous room
        if previousRoom:
            currentRoom, previousRoom = previousRoom, currentRoom
            print(f"You go back to {currentRoom}")
        # Otherwise, print an error message and stay in the current room
        else:
            print("You can't go back any further")
    # Check if the player wants to move to a new room
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if 'person' in rooms[currentRoom] and not rooms[currentRoom]['clear']:
            print(
                f"The {rooms[currentRoom]['person']} in the {currentRoom} will not let you get by so easily.")
        else:
            if 'locked' in rooms[currentRoom] and rooms[currentRoom]['locked'] == True:
                print(f"The door is locked. You must find another way or find a key.")
                if 'keys' in inventory:
                        print("You use the keys to unlock the door.")
                        rooms[currentRoom]['locked'] = False
                                       
                # not removing keys because they can be used as a weapon.
                else:
                     print("You do not have the keys. But that won't hold you back for long. Kelsier said even the water we drink has trace metals that might be worth burning.")
                
            elif len(move) > 1 and move[1] in rooms[currentRoom]["exits"]:
                currentRoom = rooms[currentRoom]["exits"][move[1]]
            else:
                print("You can't go that way!")

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        # otherwise, if the item isn't there to get
        if rooms[currentRoom]['clear'] == False:
            print(
                f"The {rooms[currentRoom]['person']} in the {currentRoom} will not let you get the {rooms[currentRoom]['item']} so easily")

        elif "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' taken!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    # if user forgets the commands
    if move[0] == 'help':
        showInstructions()

    if move[0] == 'drink':

        if 'cup' in inventory:
            inventory.remove('cup')
            inventory += metals
            print("You sense a pool of power within.")
        elif 'vial' in inventory:
            inventory.remove('vial')
            inventory += metals
            print("You sense a pool of power within.")
        else:
            print("You don\'t have anything to drink!")

    if move[0] == 'burn':
        metalchoice = input("Which metal will you burn?\n")

        if 'steel' in inventory and metalchoice == 'steel':
            print("You can feel that the metal around pulses, and blue lines shoot out from you to each metal object in the room. You can now push metal away from you.")
            steel_count = 3
            print(
                f"Blue lines extend to objects in the room. You can push the {rooms[currentRoom]['metal']}.")
        elif 'iron' in inventory and metalchoice == 'iron':
            print("You can feel that the metal around pulses, and blue lines shoot out from you to each metal object in the room. You can now pull metal to you.")
            iron_count = 3
            print(
                f"Blue lines extend to objects in the room. You can pull the {rooms[currentRoom]['metal']}.")
        elif 'pewter' in inventory and metalchoice == 'pewter':
            print("You feel your body tighten with strength. You feel like you can take a hit from a hammer, break bones with your bare hands, or balance atop a lightpost. You can now boost your physical prowess.")
            pewter_count = 3
        # Tin is not useful in my scenario so I'm removing it. Could be used in future iterations if more stealth is desired.
        # elif metalchoice == 'tin':
        #     print(
        #         "Your senses heighten. You can hear, see, smell, taste, and feel beyond even the most adept.")
        #     tin_count = 3
        else:
            print("You have not ingested any metals. Find some. Your fate depends on it!")
    # Allomancy actions
    if move[0] == 'push':
        steel_count - 1
        if 'coins' in inventory and move[1] and steel_count > 0:
            print(
                f"A nifty little Kelsier taught you. You push the {move[1]} with ferocious velocity. The {rooms[currentRoom]['person']} is torn to shreds.")
            rooms[currentRoom]['clear'] = True
            rooms[currentRoom]['item'] = move[1]
            rooms[currentRoom]['description'] = 'Any threats have been neutralized. You need to move before anyone checks this room.'
            inventory.remove('coins')
        elif 'keys' in inventory and move[1] and steel_count > 0:
            bodypart = ['head', 'chest', 'leg', 'throat']
            randpart = random.choice(bodypart)
            print(
                f" The keys blur with such speed they cut through any living thing. The {rooms[currentRoom]['person']} has key-sized hole through their {randpart}.")
            rooms[currentRoom]['clear'] = True
            inventory.remove('keys')
            rooms[currentRoom]['item'] = move[1]
            rooms[currentRoom]['description'] = 'Any threats have been neutralized. You need to move before anyone checks this room.'
        elif 'metal' in rooms[currentRoom] and move[0] == 'push' and steel_count > 0:
            print(
                f"Blue lines illuminate {rooms[currentRoom]['metal']}. You push! The {rooms[currentRoom]['metal']} bursts forward and sends you back into the wall behind you.")
            if rooms[currentRoom]['locked'] == True and rooms[currentRoom]['metal'] == 'bars':
                rooms[currentRoom]['locked'] = False
                print(
                    "You have created your own key. The guard wakes with a start and lunges toward you.")
            elif 'exits' in rooms[currentRoom] and move[1] in rooms[currentRoom]['exits']:
                previousRoom = currentRoom
                currentRoom = rooms[currentRoom]['exits'][move[1]]
                print(f"You enter the {currentRoom}.")
            else:
                print("You can't go that way!")
        else:
            print("You need more steel. Find some!\n(You might try to burn the metal if you have it in your inventory.)")
    if move[0] == 'pull':
        iron_count - 1
        if 'coins' in rooms[currentRoom] and move[1] and iron_count > 0:
            print(
                f"You pull the bag of coins to your hand. These might be useful.")
            inventory += ['item']['coins']
            del rooms[currentRoom]['item']
        elif 'metal' in rooms[currentRoom] and move[0] == 'pull' and iron_count > 0:
            if rooms[currentRoom]['metal'] == rooms[currentRoom]['item']:
                print(
                    f"You pocket the {rooms[currentRoom]['item']}, and think of devious ways to use it.")
                inventory.append(rooms[currentRoom]['item'])
                del rooms[currentRoom]['item']
            elif rooms[currentRoom]['locked'] == True and rooms[currentRoom]['metal'] == 'bars':
                rooms[currentRoom]['locked'] = False
                print(
                    f"Blue lines illuminate {rooms[currentRoom]['metal']}. You pull! The {rooms[currentRoom]['metal']} breaks free of the hinges and comes straight toward you You dodge just in time, and raise a clatter.")
                print(
                    "You have created your own key. The guard wakes with a start and lunges toward you.")
            elif 'exits' in rooms[currentRoom] and move[1] in rooms[currentRoom]['exits']:
                previousRoom = currentRoom
                currentRoom = rooms[currentRoom]['exits'][move[1]]
                print(f"You enter the {currentRoom}.")
            else:
                print("You can't go that way!")
            # Trying to pull multiple metals to you.
            # if rooms[currentRoom]['metal'] == move[1]:
            #     print(f"You pull {move[1]} to you.")
            #     if rooms[currentRoom]['metal'] == 'belt buckle':
            #         print(
            #             f"The rooms {[currentRoom]['person']}'s pants drop to their ankles, giving you a laugh.")
            #     elif rooms[currentRoom]['metal'] == 'dagger' or 'spear':
            #         print(
            #             f"You take the rooms{[currentRoom]['person']}'s crude weapon. You toss it aside and laugh at their look of utter defeat.")
        else:
            print("You need more iron. Find some!\n(You might try to burn the metal if you have it in your inventory.)")
    if move[0] == 'boost':
        pewter_count - 1
        if 'person' in rooms[currentRoom] and pewter_count > 0:
            get_wrecked = ['jugular', 'skull', 'limbs']
            pewterdeath = random.choice(get_wrecked)
            rooms[currentRoom]['clear'] = True
            rooms[currentRoom]['description'] = 'Any threats have been neutralized. You need to move before anyone checks this room.'
            if pewterdeath == 'jugular':
                print(
                    f" The {rooms[currentRoom]['person']} gasps when they see the 'little girl' in front of them shirk off any blows that would have maimed any average person.\n You laugh under your breath and send a quick jab to their throat, causing them to splutter, gasping for their last breaths.")
            elif pewterdeath == 'skull':
                print(
                    f" You flip over the {rooms[currentRoom]['person']} and smashing their skull with a pewter enhanced fist.\n Good night, tough guy.")
            else:
                print(
                    f"A series of blows from kicks and jabs to the {rooms[currentRoom]['person']} limbs leave them broken but still breathing.\n You slap the {rooms[currentRoom]['person']} which put them to sleep. Life is more than they deserve.")

        else:
            print("You need more pewter. Find some!\n(You might try to burn the metal if you have it in your inventory.)")

    # Define how a player can win
    if currentRoom == 'Tower Window' and 'steel' in inventory and 'coins' in inventory:
        print('You leap out of the window, like Kelsier taught you, tossing a coin down below. You push off the coin, sending you skyward, and soar out into the mists... YOU WIN!')
        images.ending()
        break
    elif currentRoom == 'Tower Window' and 'steel' in inventory and 'keys' in inventory:
        print('You leap out of the window, like Kelsier taught you, tossing the cell\'s keys towards the cobblestone streets below. Keys were indeed a means to escape. You trace the blue lines in your sight and steel push out into the mists... YOU WIN!')
        images.ending()
        break

    # If a player enters a room with a obligators
    elif rooms.get(currentRoom, {}).get('death') == 'obligator':
        print('An Obligator found you and easily detains you. You are but a flea compared to the Lord Ruler and his Obligators... GAME OVER!')
        images.obligator()
        break


print("If you enjoyed the story so far, check out the series Mistborn by Brandon Sanderson.")
