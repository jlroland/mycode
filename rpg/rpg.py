#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
import os
# Go trick or treating--find the treats & avoid the tricks! Get 10 pieces of candy, or get the full-size Snickers plus 2 pieces of candy, and return home to win the game.

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    Trick or Treat
    ========
    Commands:
      go [direction]
      knock
    ''')

def showStatus():
    """determine the current status of the player"""
    #print the player's current status
    print('---------------------------')
    print(houses[current_house]['desc'])
    #print the current inventory
    print('Your bag of candy contains : ' + str(candy))
    #print an item if there is one
 #   if "item" in houses[current_house]:
 #     print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
    print(houses_visited)
    print(candy)
    print(sum(candy_tally))


# an inventory, which is initially empty
candy = []
candy_tally = []

# a dictionary linking each house to other houses in the neighborhood
houses = {

            'Home' : {
                  'desc'  : 'You are home.',
                  'south' : 'Straight Across',
                  'east'  : 'East Neighbor',
                  'west'  : 'West Neighbor'
                },
            'East Neighbor' : {
                  'desc'  : 'You are at your next-door neighbor\'s house.',
                  'north' : 'Northeast',
                  'south' : 'Southeast',
                  'west'  : 'Home',
                  'item'  : '1 fun-size Skittles',
                  'count' : 1
                },
            'West Neighbor' : {
                  'desc'  : 'You are at your next-door neighbor\'s house.',
                  'east' : 'Home',
                  'south': 'West Across',
                  'north': 'Northwest',
                  'item' : '2 fun-size M&Ms',
                  'count': 2
                },
            'Straight Across' : {
                  'desc'  : 'You are across the street from your house.',
                  'north' : 'Home',
                  'west'  : 'West Across',
                  'east'  : 'East Across',
                  'item'  : '2 fun-size Kit Kat',
                  'count' : 2
                },
            'East Across' : {
                  'desc'  : 'You\'re in front of a house down the street from your house.',
                  'west' : 'Straight Across',
                  'south': 'Southeast',
                  'north': 'East Neighbor'
               },
            'West Across' : {
                  'desc'  : 'You\'re in front of a house down the street from your house.',
                  'east' : 'Straight Across',
                  'south': 'Southwest',
                  'north': 'West Neighbor'
               },
            'Northwest' : {
                  'desc' : 'You\'re in front of a house a block north of your house.',
                  'east' : 'Northeast',
                  'south': 'West Neighbor'
               },
            'Northeast' : {
                  'desc' : 'You\'re in front of a house a block north of your house.',
                  'west' : 'Northwest',
                  'south': 'East Neighbor',
                  'item' : '1 fun-size Milky Way, 2 Dum-Dums',
                  'count': 3
               },
            'Southwest' : {
                  'desc' : 'You\'re in front of a house a block south of your house.',
                  'east' : 'Southeast',
                  'north': 'West Across',
                  'item' : '2 packs of Bottle Caps',
                  'count': 2
               },
            'Southeast' : {
                  'desc' : 'You\'re in front of a house a block south of your house.',
                  'west' : 'Southwest',
                  'north': 'East Across',
                  'item' : 'full-size Snickers bar',
                  'count': 1
               }
         }

# start the player in the Hall
current_house = 'Home'

# keep track of houses already visited
houses_visited = []

os.system('clear')  #start game with fresh screen
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

    # split allows an input to be separated into action (go , knock) & the rest of the phrase         
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        os.system('clear')
        # check that they are allowed wherever they want to go
        if move[1] in houses[current_house]:
            # set the current house to the new house
            current_house = houses[current_house][move[1]]
        # not allowed to go in that direction
        else:
            print('You can\'t go that way!')

    #if they type 'knock'
    if move[0] == 'knock' :
        os.system('clear')
        # if they try to knock on someone's door more than once
        if current_house == 'Home':
            print('Why are you knocking on your own door? You still have candy to collect.')
        elif current_house in houses_visited:
            print('You already visited this house. No repeats.')
        # if they knock on the door of "the mean guy"
        elif current_house == 'East Across':
            houses_visited.append(current_house)
            if sum(candy_tally) > 0:
                print('This guy prefers tricks over treats. Instead of giving you candy, he takes a piece of yours & slams the door shut.')
                candy.pop()
                candy_tally.pop()
            else:
                print('This guy is not in a giving mood. He tells you to go away & slams the door shut.')
        # if the house is giving out candy
        elif "item" in houses[current_house]:
            # if they visit their teacher's house, they have to earn their candy
            if current_house == 'Northeast':
                teacher = input('Oh, no! You knocked on the door & it\'s your teacher. If you want candy, you have to answer a math question correctly. What is 55 percent of 200?  ')
                if teacher == '110':
                     # add the candy to their bag
                    candy.append(houses[current_house]['item'])
                    candy_tally.append(houses[current_house]['count'])
                    # display a helpful message
                    print(houses[current_house]['item'] + 'has been added to your bag!')
                    # keep track of where they have been
                    houses_visited.append(current_house)
                else:
                    # wrong answer, no candy
                    print('That\'s incorrect--no candy for you.')
                    houses_visited.append(current_house)
            else:
                # add the candy to their bag
                candy.append(houses[current_house]['item'])
                candy_tally.append(houses[current_house]['count'])
                # display a helpful message
                print(houses[current_house]['item'] + ' has been added to your bag!')
                # keep track of where they have been
                houses_visited.append(current_house)
        else:
            # people are not home, or they're pretending they're not
            print('Nobody answers the door. Time to move on.')
    ## Define how a player can win
    if current_house == 'Home' and 'full-size Snickers bar' in candy and sum(candy_tally) >=3 :
        print('You made it home with enough candy... YOU WIN!')
        break
    if current_house == 'Home' and sum(candy_tally) >= 10:
        print('You made it home with enough candy... YOU WIN!')
        break
    ## Define how the game will end if all options are exhaused
        # to be continued
    
