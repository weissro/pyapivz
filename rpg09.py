#!/usr/bin/python3

def showInstructions():
    print('''
            RPG Game
            --------
            Commands:
            go [direction]
            get [item]

    ''')

def showStatus():
    #print the player's current status
    print('----------------------------')
    print(f"You are in the {currentRoom}.")
    #print the current inventory
    directions = list(rooms[currentRoom].keys())
    if 'item' in directions:
        directions.remove('item')
    print(f"From this place you can move {directions}")
    print("Inventory: " + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]['item'])
    print("----------------------------")

    # an inventory which is initially empty

inventory = []

rooms = {
            'Hall' : {
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'skeletonkey',
                },
            'Kitchen' : {
                'north' : 'Hall',
                'item' : 'chickenleg'
                },
            'Dining Room' : {
                'west' : 'Hall',
                'south': 'Garden',
                'item' : 'monster'
                },
            'Garden' : {
                'north': 'Dining Room'
                }
           }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:
    showStatus()
    move = '' 
    while move == '':
        move = input(">")

    move = move.lower().split()

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way, moron!")

    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(f"You just picked up {move[1]}!")
            del rooms[currentRoom]['item']

        else: 
            print("You cannot pick that up, you weakling!")
    
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if 'chickenleg' in inventory:
            inventory.remove('chickenleg')
            del rooms[currentRoom]['item']
            print('The monster named Col. Harland Sanders has taken your fried chicken!')
        else:
            print('The ravenous Col. Sanders demands a sacrifice! And that sacrifice is YOU!!')
            break;

    if currentRoom == 'Garden' and 'skeletonkey' in inventory:
        print("You escaped the house! Unlock the gate and you win!")
        break
