import pygame, sys, random
import pygame.mixer


## AGENDA ##

# Random Starting Location (need random generator that spits out 4 numbers, different ones)
# Program in a win condition
# Get all zones coded into to main game board.
# Balance victory point/capture point gain.
# more friendly interface/print statements
# Program in other 3 players
# Another Data Source

pygame.init()
mainClock = pygame.time.Clock()

movemove = pygame.mixer.Sound('Sound/se_bonus.wav')
move2 = pygame.mixer.Sound('Sound/se_item00.wav')
move3 = pygame.mixer.Sound('Sound/se_damage01.wav')
# Loads the sound effect

## move.play()
## move2.play()
# Plays the sound effect

lastResource = 'temp'
resourceCount = 0

## pygame.mixer.music.load('Sound/lobdan_03.mp3')    # Loads a song (can only load one song at a time)
## pygame.mixer.music.play(-1)    # Plays the song (the -1 makes it loop



_display = pygame.display.set_mode((800, 531), 0, 32)
pygame.display.set_caption('Conquerors of Random Map')
## BG

background = pygame.image.load('Pics/bg2.png')
bgSize = background.get_rect()

## Turns for the players, Game conds

turn = 1
game = True
printinstructions = True
upkeep = True
default = 1
winner = 'Player' ## not yet decided
wincond = 30 ## Change as we like it to be.

fileNames = []
fileNames.append('Presidents')
fileNames.append('1914')
fileNames.append('1918')
fileNames.append('Austin')
fileNames.append('Scientists')

presNames = []          ## create two arrays for presidents
presValues = []

fourteenNames = []      ## create two arrays for 1914
fourteenValues = []

eighteenNames = []      ## create two arrays for 1918
eighteenValues = []

austinMonths = []       ## two arrays for Austin, TX
austinValues = []

scientistNames = []     ## two arrays for Scientists
scientistAges = []

# print(lastResource)

f = open('Pics/presidents.txt')

for line in f:
    parts = line.split(";")
    presNames.append( parts[0])         ## fill in pres names 
    presValues.append( int (parts[1]) )   ## fill in pres values

f.close()

f = open('Pics/inflation1914.txt')

for line in f:
    parts = line.split(";")
    fourteenNames.append( parts[0])         ## fill in 1914 names 
    fourteenValues.append( float (parts[1]) )   ## fill in 1914 values

f.close()

f = open('Pics/inflation1918.txt')

for line in f:
    parts = line.split(";")
    eighteenNames.append( parts[0])         ## fill in 1918 names 
    eighteenValues.append( float (parts[1]) )   ## fill in 1918 values

f = open('Pics/austinTX.txt')

for line in f:
    parts = line.split(";")
    austinMonths.append( parts[0])         ## fill in Austin months 
    austinValues.append( float (parts[1]) )   ## fill in Austin temps

f = open('Pics/scientists.txt')

for line in f:                              ## fill in two arrays for Scientists
    parts = line.split(";")
    scientistNames.append( parts[0])
    scientistAges.append( int (parts[1]) )

################# Location Classes

## Code/stuffs to make flag

## Array of Flags
flags = [] 



def plantFlag(color, xcoor, ycoor):
    image = pygame.image.load(color)
    imagex = xcoor
    imagey = ycoor
    flags.append([image, imagex, imagey])
    
## UPDATE DISHPLAY

def updateDisplay():
     _display.blit(background, bgSize)
     _display.blit(goldpiece,(gold.x, gold.y))
     _display.blit(bluepiece,(blue.x, blue.y))
     _display.blit(blackpiece,(black.x, black.y))
     _display.blit(whitepiece,(white.x, white.y))
     for f in flags:
        _display.blit(f[0],(f[1],f[2]))
     pygame.display.flip()

## Main Gameboard

class zone: ## Gameboard spots
    def __init__(loc, goldxcoor, goldycoor, bluexcoor, blueycoor, blackxcoor, blackycoor, whitexcoor, whiteycoor, captured, needed, victorypoints):
        loc.goldx = goldxcoor
        loc.goldy = goldycoor
        loc.bluex = bluexcoor
        loc.bluey = blueycoor
        loc.blackx = blackxcoor
        loc.blacky = blackycoor
        loc.whitex = whitexcoor
        loc.whitey = whiteycoor
        loc.c = captured
        loc.n = needed
        loc.v = victorypoints


## Each zone has 4 locations - one for each player. When they move to a spot, it will call that specific x/y coordinate.
    

z0 = zone(29, 254, 50, 254, 29, 271, 38, 274, False, 3, 1)
z1 = zone(62, 204, 85, 211, 70, 230, 95, 235, False, 3, 1)
z2 = zone(85, 288, 92, 290, 85, 295, 82, 300, False, 3, 1)
z3 = zone(142, 117, 144, 138, 142, 126, 152, 118, False, 2, 2)
z4 = zone(157, 161, 180, 190, 147, 203, 165, 210, False, 4, 3)
z5 = zone(158, 255, 111, 338, 135, 286, 111, 350, False, 3, 2)
z6 = zone(125, 338, 134, 347, 135, 342, 160, 370, False, 2, 2)
z7 = zone(178, 148, 187, 157, 190, 170, 205, 190, False, 3, 2)
z8 = zone(170, 234, 189, 222, 202, 218, 201, 225, False, 3, 2)
z9 = zone(193, 262, 178, 282, 193, 307, 204, 282, False, 4, 3)
z10 = zone(153, 306, 140, 323, 161, 337, 187, 348, False, 5, 3)
z11 = zone(127, 388, 133, 395, 122, 403, 110, 410, False, 3, 3)
z12 = zone(150, 430, 151, 430, 150, 431, 151, 431, False, 1, 1)
z13 = zone(195, 432, 227, 439, 197, 471, 210, 472, False, 4, 4)
z14 = zone(227, 84, 244, 85, 236, 95, 240, 87, False, 2, 2)
z15 = zone(272, 105, 274, 105, 272, 107, 274, 107, False, 14, 10)
z16 = zone(260, 143, 261, 160, 268, 177, 270, 195, False, 4, 3)
z17 = zone(288, 193, 189, 193, 288, 194, 289, 294, False, 1, 1)
z18 = zone(256, 212, 324, 198, 260, 243, 310, 232, False, 5, 4)
z19 = zone(298, 255, 292, 263, 296, 270, 300, 260, False, 3, 2)
z20 = zone(271, 265, 278, 275, 264, 284, 281, 295, False, 3, 3)
z21 = zone(255, 337, 275, 340, 300, 345, 280, 360, False, 4, 3)
z22 = zone(244, 357, 240, 370, 230, 380, 247, 374, False, 3, 2)
z23 = zone(220, 400, 230, 400, 220, 410, 230, 410, False, 2, 2)
z24 = zone(250, 390, 270, 387, 255, 400, 270, 400, False, 4, 3)
z25 = zone(249, 421, 279, 419, 254, 430, 260, 420, False, 3, 3)
z26 = zone(300, 400, 310, 410, 288, 434, 300, 434, False, 4, 3)
z27 = zone(234, 464, 300, 452, 254, 484, 300, 482, False, 5, 4)
z28 = zone(296, 108, 291, 126, 273, 130, 287, 155, False, 4, 3)
z29 = zone(302, 136, 305, 136, 302, 139, 305, 139, False, 2, 1)
z30 = zone(310, 162, 313, 163, 310, 168, 313, 168, False, 7, 5)

MGB = [z0, z1, z2, z3, z4, z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19,z20,z21,z22,z23,z24,z25,z26,z27,z28,z29,z30]

class Player: ## Piece location
    def __init__(player, xcoor, ycoor, color, move, actionpoints, victorypoints, zones, position):
        player.x = xcoor
        player.y = ycoor
        player.c = color
        player.m = move
        player.ap = actionpoints
        player.vp = victorypoints
        player.z = zones
        player.pos = position ## Randomly generate a number, and move the player to that spot in array.



#### RANDOMLY PLACED POSITIONS ####

goldpos = random.randint(0,29)
bluepos = random.randint(0,29)
blackpos = random.randint(0,29)
whitepos = random.randint(0,29)

        

## Gold Player Variables
gold = Player(MGB[goldpos].goldx, MGB[goldpos].goldy, 'gold', True, 0, 0, 0, goldpos)
gold.pos = goldpos
# Gold Pictures
goldpiece = pygame.image.load('Pics/gold.png')
goldflag = 'Pics/goldf.png'
## Blue Player Variables
blue = Player(MGB[bluepos].bluex, MGB[bluepos].bluex, 'blue', True, 0, 0, 0, bluepos)
blue.pos = bluepos
# Blue Pictures
bluepiece = pygame.image.load('Pics/blue.png')
blueflag = 'Pics/bluef.png'
## Black Player Variables
black = Player(MGB[blackpos].blackx, MGB[blackpos].blacky, 'black', True, 0, 0, 0, blackpos)
black.pos = blackpos
# Blacks
blackpiece = pygame.image.load('Pics/black.png')
blackflag = 'Pics/blackf.png'
## White Player Variables
white = Player(MGB[whitepos].whitex, MGB[whitepos].whitey, 'white', True, 0, 0, 0, whitepos)
white.pos = whitepos
# Whites
whitepiece = pygame.image.load('Pics/white.png')
whiteflag = 'Pics/whitef.png'






##### Move method

class MovePiece:
    x = 0


def randIndex():
    return random.randint(0,11)

def rollMove():
    updateDisplay()
    global lastResource
    global resourceCount
    movemove.play()
    print('Choose how to determine your dice roll this turn!')
    print(' Birth month of Presidents, Inflation from the year 1914,')
    print(' Inflation from the year 1918, average monthly temperatures of Austin, TX, ')
    print(' or life length of famous Scientists.')
    print('  Accepted inputs are -> Presidents, 1914, 1918, Austin, Scientists')
    # print(lastResource)
    # print(resourceCount)

    file = input( 'Decide your fate : ' )
    # print('file equals')
    # print(file)
    # print('lastResource equals')
    # print(lastResource)
    # print('file == lastResource')
    # print(file == lastResource)

    if (file == lastResource):
        resourceCount += 1
        # print(lastResource)
        # print(resourceCount)

    while(resourceCount >=2):
        print('That resource is being abused.  You are required to choose a different resource.')
        print(lastResource)
        print('  is the resource that is not permitted.')
        file = input('   Choose how to determine your dice roll: ' )

        if (file != lastResource):
            resourceCount = 0

    while file not in fileNames:

        move2.play()
        print('That is not a valid option for dice roll. ')
        print(' Choose an input from Presidents, 1914, 1918, Austin, or Scientists. ')
        file = input( 'Make a choice : ' )

    if(file == 'Presidents'):
        print('Input one of the following Presidents : ')
        print(' Washington, Obama, Arthur, Bush, Monroe, Cleveland, ')
        print(' Buren, Coolidge, Harding, Fillmore, Kennedy, Taft')
        print('  Spelling and capitalization must be exact. ')
        ask = input( 'Your President choice is : ' )

        lastResource = 'Presidents'
        # print(lastResource)

    # randomIndex = random.randint(0,11)

        if (ask not in presNames):
            print('Input a President please.')
            ask = input( ' : ' )

        if (ask not in presNames):
            print('You have one more chance to correctly name one of the listed Presidents.')
            print(' Washington, Obama, Arthur, Bush, Monroe, Cleveland, ')
            print('Buren, Coolidge, Harding, Fillmore, Kennedy, Taft ')
            print('Spelling and capitalization must be exact. ')
            ask = input( ' : ' )

        if (ask not in presNames):
            print('Your dice roll is 0. ')
            print('')
            finalRoll = 0
    
        for name in presNames:
        # print('in the for loop')
            if name == ask:
            # print(valuesArray)
            # print([name])
            # print(namesArray.index(name))
            # print (valuesArray[namesArray.index(ask)] )
                presRoll = presValues[presNames.index(ask)]
            # print ('printing presRoll : ' )
            # print(presRoll)
                randomRoll = presValues[randIndex()]
            # print (randomRoll)
            # print('presRoll - randomRoll')
            # print(presRoll - randomRoll)
                if ( ((presRoll - randomRoll) == 11) or ((presRoll - randomRoll) == 10)):
                    finalRoll = 6
                if ( ((presRoll - randomRoll) == 9) or ((presRoll - randomRoll) == 8)):
                    finalRoll = 5
                if ( ((presRoll - randomRoll) == 7) or ((presRoll - randomRoll) == 6)):
                    finalRoll = 4
                if ( ((presRoll - randomRoll) == 5) or ((presRoll - randomRoll) == 4)):
                    finalRoll = 3
                if ( ((presRoll - randomRoll) == 3) or ((presRoll - randomRoll) == 2)):
                    finalRoll = 2
                if ( ((presRoll - randomRoll) <= 1)):
                    finalRoll = 1
        print('You rolled a ' )
        print(finalRoll)
        print('')
        return finalRoll

    if (file == '1914'):
        print('Input the abbrevition for a month.')
        print(' Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec ')
        ask = input( 'The month you select is : ' )

        lastResource = '1914'

        while ask not in fourteenNames:
            print('That is not a valid month.  Try again.  Remember, only the first three letters.')
            ask = input (' The month you choose is : ' )
    
        for name in fourteenNames:
            if name == ask:
                monthRoll = fourteenValues[fourteenNames.index(ask)]
            # print('printing monthRoll : ')
            # print(monthRoll)
                randomRoll = fourteenValues[randIndex()]
            # print(randomRoll)
                diceRoll = monthRoll - randomRoll
            # print('monthRoll - randomRoll')
            # print(monthRoll - randomRoll)
                if ( ((monthRoll - randomRoll >= 2.4) )):
                    finalRoll = 6
                if ( ((monthRoll - randomRoll) >= 1.8) and (monthRoll - randomRoll < 2.4)):
                    finalRoll = 5
                if ( ((monthRoll - randomRoll) >= 1.2) and (monthRoll - randomRoll < 1.8)):
                    finalRoll = 4
                if ( ((monthRoll - randomRoll) >= 0.6) and (monthRoll - randomRoll < 1.2)):
                    finalRoll = 3
                if ( ((monthRoll - randomRoll) >= 0.0) and (monthRoll - randomRoll < 0.6)):
                    finalRoll = 2
                if ( (monthRoll - randomRoll < 0.0 )):
                    finalRoll = 1
        print('You rolled a ' )
        print(finalRoll)
        print('')
        return finalRoll

    if (file == '1918'):
        print('  Choose a month.')
        print('Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec ')
        ask = input( ' Your preferred month this dice roll is : ' )

        lastResource = '1918'

        while ask not in eighteenNames:
            print('You did not enter a valid month.  Try again.' )
            ask = input ( ' : ' )

        for name in eighteenNames:
            if name == ask:
                monthRoll = eighteenValues[eighteenNames.index(ask)]
            # print('printing monthRoll : ')
            # print(monthRoll)
                randomRoll = eighteenValues[randIndex()]
            # print(randomRoll)
                diceRoll = monthRoll - randomRoll
            # print('monthRoll - randomRoll')
            # print(monthRoll - randomRoll)
                if ( ((monthRoll - randomRoll >= 5.3) )):
                    finalRoll = 6
                if ( ((monthRoll - randomRoll) >= 4.0) and (monthRoll - randomRoll < 5.3)):
                    finalRoll = 5
                if ( ((monthRoll - randomRoll) >= 2.7) and (monthRoll - randomRoll < 4.0)):
                    finalRoll = 4
                if ( ((monthRoll - randomRoll) >= 1.4) and (monthRoll - randomRoll < 2.7)):
                    finalRoll = 3
                if ( ((monthRoll - randomRoll) >= 0.0) and (monthRoll - randomRoll < 1.4)):
                    finalRoll = 2
                if ( (monthRoll - randomRoll < 0.0 )):
                    finalRoll = 1

        print('You rolled a ' )
        print(finalRoll)
        print('')
        return finalRoll

    if (file == 'Austin'):

        print('Provide a month that will be used for your dice roll.')
        print(' Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec ')
        ask = input( 'You have selected : ' )

        lastResource = 'Austin'

        while ask not in austinMonths:
            print('Please choose one of the twelve months, by 3 letter abbreviation.  Try again.' )
            ask = input ( ' : ' )

        for name in austinMonths:
          if name == ask:
              monthRoll = austinValues[austinMonths.index(ask)]

              randomRoll = austinValues[randIndex()]

              diceRoll = monthRoll - randomRoll

              if ( (monthRoll - randomRoll >= 30) ):
                finalRoll = 6
              if ( (monthRoll - randomRoll >= 24) and (monthRoll - randomRoll) < 30):
                finalRoll = 5
              if ( (monthRoll - randomRoll >= 18) and (monthRoll - randomRoll) < 24):
                finalRoll = 4
              if ( (monthRoll - randomRoll >= 12) and (monthRoll - randomRoll) < 18):
                finalRoll = 3
              if ( (monthRoll - randomRoll >= 6) and (monthRoll - randomRoll) < 12):
                finalRoll = 2
              if ( (monthRoll - randomRoll < 6) ):
                finalRoll = 1

        print('You rolled a ')
        print(finalRoll)
        print('')
        return finalRoll


    if (file == 'Scientists'):
        print('Choose a famous scientist name.')
        print('Newton, Einstein, Darwin, Pasteur, Freud, Galileo, ')
        print('Copernicus, Faraday, Virchow, Boltzmann, Curie, or Gauss')
        ask = input( 'Your Scientist to input is : ' )

        lastResource = 'Scientists'

        while ask not in scientistNames:
            print('Make a selection from one of the listed Scientists to generate a dice roll.  Try again.' )
            ask = input ( ' : ' )

        for name in scientistNames:
            if name == ask:
                monthRoll = scientistAges[scientistNames.index(ask)]
                randomRoll = scientistAges[randIndex()]

                if ( ((monthRoll - randomRoll >= 14) )):
                    finalRoll = 6
                if ( ((monthRoll - randomRoll) >= 11) and (monthRoll - randomRoll < 14)):
                    finalRoll = 5
                if ( ((monthRoll - randomRoll) >= 8) and (monthRoll - randomRoll < 11)):
                    finalRoll = 4
                if ( ((monthRoll - randomRoll) >= 4) and (monthRoll - randomRoll < 8)):
                    finalRoll = 3
                if ( ((monthRoll - randomRoll) >= 0) and (monthRoll - randomRoll < 4)):
                    finalRoll = 2
                if ( (monthRoll - randomRoll < 0 )):
                    finalRoll = 1

        print('You rolled a ' )
        print(finalRoll)
        print('')
        return finalRoll

# Example - move the red piece from home to s0.


while game:

 pygame.display.flip()
 mainClock.tick(32)
 updateDisplay()

 for event in pygame.event.get():
    if gold.vp == wincond or blue.vp == wincond or black.vp == wincond or white.vp == wincond:
         turn == 5
         print('Game over!')

    if turn == 1 and printinstructions:
        updateDisplay()
        movemove.play()
        print('')
        print('Gold Knight, make your move.')
        print('')
        r = MovePiece()
        r.move = rollMove()
        gold.ap = gold.ap + r.move ## adds your dice roll to your points.
        print ('Number of action points to spend: ')
        print (gold.ap)
        print('Use the Left/Right Arrow keys to move to adjacent zones on the Map.')
        print('Or press C to Capture the zone you are currently in.')
        print('')
        printinstructions = False
        ## Update Gold Knight's upkeep.
        if upkeep:
            gold.ap = gold.ap + default + (gold.z) ## Increase gold player's action points by the default amount + 2 for each zone they control.
            upkeep = False ## Sets upkeep to false to make sure it won't be triggered again, even by accident. Re-enable this at the very start of player 1's turn.
    if turn == 2 and printinstructions:
        updateDisplay()
        movemove.play()
        print('')
        print('Blue Knight, it is your turn.')
        print('')
        r = MovePiece()
        r.move = rollMove()
        blue.ap = blue.ap + r.move ## adds your dice roll to your points.
        print ('Number of action points to spend: ')
        print (blue.ap)
        print('Use the Left/Right Arrow keys to move to adjacent zones on the Map.')
        print('Or press C to Capture the zone you are currently in.')
        print('')
        printinstructions = False
        ## Update Blue Knight's upkeep.
        if upkeep:
            blue.ap = blue.ap + default + (blue.z) ## Increase gold player's action points by the default amount + 2 for each zone they control.
            upkeep = False ## Sets upkeep to false to make sure it won't be triggered again, even by accident. Re-enable this at the very start of player 1's turn.
    if turn == 3 and printinstructions:
        updateDisplay()
        movemove.play()
        print('')
        print('Black Knight, this is your time to act.')
        print('')
        r = MovePiece()
        r.move = rollMove()
        black.ap = black.ap + r.move ## adds your dice roll to your points.
        print ('Number of action points to spend: ')
        print (black.ap)
        print('Use the Left/Right Arrow keys to move to adjacent zones.')
        print('Or press C to Capture the zone you are currently in.')
        print('')
        printinstructions = False
        ## Update Black Knight's upkeep.
        if upkeep:
            black.ap = black.ap + default + (black.z) ## Increase gold player's action points by the default amount + 2 for each zone they control.
            upkeep = False ## Sets upkeep to false to make sure it won't be triggered again, even by accident. Re-enable this at the very start of player 1's turn.
    if turn == 4 and printinstructions:
        updateDisplay()
        movemove.play()
        print('')
        print('White Knight, now is your chance.')
        print('')
        r = MovePiece()
        r.move = rollMove()
        white.ap = white.ap + r.move ## adds your dice roll to your points.
        print ('Number of action points to spend: ')
        print (white.ap)
        print('Use the Left/Right Arrow keys to move to adjacent zones.')
        print('Or press C to Capture the zone you are currently in.')
        print('')
        printinstructions = False
        ## Update White Knight's upkeep.
        if upkeep:
            white.ap = white.ap + default + (white.z) ## Increase gold player's action points by the default amount + 2 for each zone they control.
            upkeep = False ## Sets upkeep to false to make sure it won't be triggered again, even by accident. Re-enable this at the very start of player 1's turn.
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if turn == 5:
        move3.play()
        pygame.mixer.music.load('Sound/aost01.mp3')    # Loads a song (can only load one song at a time)
        pygame.mixer.music.play(-1)    # Plays the song (the -1 makes it loop
        print('Game Over!  The victor has been decided.')
        print (winner)
        turn == 6
    if turn == 6:
        print('Thanks for playing!')
        


##################################################

        ## Gold Player


    if turn == 1 and event.type == pygame.KEYDOWN:
        winner = 'Gold Player'
        print ('Turn =')
        print (turn)
        print ('It will take this many action points to capture this space:')
        print (MGB[gold.pos].n)
        print ('Number of action points to spend: ')
        print (gold.ap)
        if gold.ap == 0:
            print('You have no action points left. Press q to end your turn.')
               
        if event.key == pygame.K_LEFT and turn == 1:
            print('Gold player moving to previous zone.')
            if gold.pos == 0 or gold.ap == 0 and turn == 1:
                print('Cannot move any further back.')
            elif turn == 1:
                gold.ap = gold.ap - 1 ## subtract 1 action point.
                gold.pos = gold.pos - 1 ## moves gold player 1 back in the game array.
                gold.x = MGB[gold.pos].goldx
                gold.y = MGB[gold.pos].goldy
                updateDisplay()

                ## Possible addition - move to random location FOR 10 PTS.
                
        if event.key == pygame.K_RIGHT and turn == 1:
            print('Gold player moving to next zone.')
            if gold.pos == 80 or gold.ap == 0:
                print('Cannot move any further fowards.')
            elif turn == 1:
                gold.ap = gold.ap - 1 ## subtract 1 action point.
                gold.pos = gold.pos + 1 ## moves gold player 1 back in the game array.
                gold.x = MGB[gold.pos].goldx
                gold.y = MGB[gold.pos].goldy
                updateDisplay()


            ###### Capture option - press c to capture. ######
        if event.key == pygame.K_c and turn == 1: ## Will only let you capture if you have the required amount of action points.
          print('Gold Player is attempting to capture this zone.')

          if MGB[gold.pos].c == False and gold.ap >= MGB[gold.pos].n and turn == 1:
              MGB[gold.pos].c = True
             ## access gold player's pos on the main game board, and sets it to "captured."
              gold.z = gold.z + 1 ## Increment number of zones by 1.
              gold.ap = gold.ap - MGB[gold.pos].n ## Subtract that many action points it took to capture.
              gold.vp = gold.vp + MGB[gold.pos].v
              
              print('Gold Player has captured this zone.')
              print('Gold Player now has...')
              print(gold.z)
              print('zones under control.')
              plantFlag(goldflag, gold.x, gold.y)
              print('Gold Player now has ')
              print(gold.vp)
              print(' Victory Points.')
              updateDisplay()
                               
                               
          elif turn == 1:
              print('Cannot capture zone. Not enough action points or already captured.')
              print('Required action points:')
              print(MGB[gold.pos].n)
              # print('CAPTURED?')
              # print(MGB[gold.pos].c)
              updateDisplay()                 

        if event.key == pygame.K_q and turn == 1:
            print('Gold player has ended his turn.')
            turn = 2
            print (turn)
            printinstructions = True
            upkeep = True
            updateDisplay()


##################################################

        ## Blue Player


    elif turn == 2 and event.type == pygame.KEYDOWN:
        winner = 'Blue Knight'
        print ('Turn =')
        print (turn)
        print ('It will take this many action points to capture this space:')
        print (MGB[blue.pos].n)
        print ('Number of action points to spend: ')
        print (blue.ap)
        if blue.ap == 0 and turn == 2:
            print('You have no action points left. Press q to end your turn.')
               
        if event.key == pygame.K_LEFT and turn == 2:
            print('Blue player moving to previous zone.')
            if blue.pos == 0 or blue.ap == 0:
                print('Cannot move any further back.')
            elif turn == 2:
                blue.ap = blue.ap - 1 ## subtract 1 action point.
                blue.pos = blue.pos - 1 ## moves blue player 1 back in the game array.
                blue.x = MGB[blue.pos].bluex
                blue.y = MGB[blue.pos].bluey
                updateDisplay()

                ## Possible addition - move to random location FOR 10 PTS.
                
        if event.key == pygame.K_RIGHT and turn == 2:
            print('Blue player moving to next zone.')
            if blue.pos == 80 or blue.ap == 0 and turn == 2:
                print('Cannot move any further fowards.')
            elif turn == 2:
                blue.ap = blue.ap - 1 ## subtract 1 action point.
                blue.pos = blue.pos + 1 ## moves blue player 1 back in the game array.
                blue.x = MGB[blue.pos].bluex
                blue.y = MGB[blue.pos].bluey
                updateDisplay()


            ###### Capture option - press c to capture. ######
        if event.key == pygame.K_c and turn == 2: ## Will only let you capture if you have the required amount of action points.
          print('Blue Player is attempting to capture this zone.')

          if MGB[blue.pos].c == False and blue.ap >= MGB[blue.pos].n and turn == 2:
              MGB[blue.pos].c = True
             ## access blue player's pos on the main game board, and sets it to "captured."
              blue.z = blue.z + 1 ## Increment number of zones by 1.
              blue.ap = blue.ap - MGB[blue.pos].n ## Subtract that many action points it took to capture.
              blue.vp = blue.vp + MGB[blue.pos].v
              
              print('Gold Player has captured this zone.')
              print('Gold Player now has...')
              print(blue.z)
              print('zones under control.')
              plantFlag(blueflag, blue.x, blue.y)
              print('Blue Player now has')
              print(blue.vp)
              print('Victory Points.')
              updateDisplay()
                               
                               
          elif turn == 2:
              print('Cannot capture zone. Not enough action points or already captured.')
              print('Required action points:')
              print(MGB[blue.pos].n)
              # print('CAPTURED?')
              # print(MGB[blue.pos].c)
              updateDisplay()                 

        if event.key == pygame.K_q and turn == 2:
            print('Blue player has ended his turn.')
            turn = 3
            printinstructions = True
            upkeep = True
            updateDisplay()



##################################################

        ## Black Player


    elif turn == 3 and event.type == pygame.KEYDOWN:
        winner = 'Black Player'
        print ('Turn =')
        print (turn)
        print ('It will take this many action points to capture this space:')
        print (MGB[black.pos].n)
        print ('Number of action points to spend: ')
        print (black.ap)
        if black.ap == 0:
            print('You have no action points left. Press q to end your turn.')
               
        if event.key == pygame.K_LEFT and turn == 3:
            print('Black player moving to previous zone.')
            if black.pos == 0 or black.ap == 0 and turn == 3:
                print('Cannot move any further back.')
            elif turn == 3:
                black.ap = black.ap - 1 ## subtract 1 action point.
                black.pos = black.pos - 1 ## moves black player 1 back in the game array.
                black.x = MGB[black.pos].blackx
                black.y = MGB[black.pos].blacky
                updateDisplay()

                ## Possible addition - move to random location FOR 10 PTS.
                
        if event.key == pygame.K_RIGHT and turn == 3:
            print('Black player moving to next zone.')
            if black.pos == 80 or black.ap == 0 and turn == 3:
                print('Cannot move any further fowards.')
            elif turn == 3:
                black.ap = black.ap - 1 ## subtract 1 action point.
                black.pos = black.pos + 1 ## moves black player 1 back in the game array.
                black.x = MGB[black.pos].blackx
                black.y = MGB[black.pos].blacky
                updateDisplay()


            ###### Capture option - press c to capture. ######
        if event.key == pygame.K_c and turn == 3: ## Will only let you capture if you have the required amount of action points.
          print('Black Player is attempting to capture this zone.')

          if MGB[black.pos].c == False and black.ap >= MGB[black.pos].n and turn == 3:
              MGB[black.pos].c = True
             ## access black player's pos on the main game board, and sets it to "captured."
              black.z = black.z + 1 ## Increment number of zones by 1.
              black.ap = black.ap - MGB[black.pos].n ## Subtract that many action points it took to capture.
              black.vp = black.vp + MGB[black.pos].v
              
              print('Black Player has captured this zone.')
              print('Black Player now has...')
              print(black.z)
              print('zones under control.')
              plantFlag(blackflag, black.x, black.y)
              print('Black Player now has')
              print(black.vp)
              print('Victory Points.')
              updateDisplay()
                               
                               
          elif turn == 3:
              print('Cannot capture zone. Not enough action points or already captured.')
              print('Required action points:')
              print(MGB[black.pos].n)
              # print('CAPTURED?')
              # print(MGB[black.pos].c)
              updateDisplay()                 

        if event.key == pygame.K_q and turn == 3:
            print('Black player has ended his turn.')
            turn = 4
            print (turn)
            printinstructions = True
            upkeep = True
            updateDisplay()


##################################################

        ## White Player


    elif turn == 4 and event.type == pygame.KEYDOWN:
        winner = 'Black Player'
        print ('Turn =')
        print (turn)
        print ('It will take this many action points to capture this space:')
        print (MGB[white.pos].n)
        print ('Number of action points to spend: ')
        print (white.ap)
        if white.ap == 0:
            print('You have no action points left. Press q to end your turn.')
               
        if event.key == pygame.K_LEFT and turn == 4:
            print('White player moving to previous zone.')
            if white.pos == 0 or white.ap == 0 and turn == 4:
                print('Cannot move any further back.')
            elif turn == 1:
                white.ap = white.ap - 1 ## subtract 1 action point.
                white.pos = white.pos - 1 ## moves white player 1 back in the game array.
                white.x = MGB[white.pos].whitex
                white.y = MGB[white.pos].whitey
                updateDisplay()

                ## Possible addition - move to random location FOR 10 PTS.
                
        if event.key == pygame.K_RIGHT and turn == 4:
            print('White player moving to next zone.')
            if white.pos == 80 or white.ap == 0 and turn == 4:
                print('Cannot move any further fowards.')
            elif turn == 4:
                white.ap = white.ap - 1 ## subtract 1 action point.
                white.pos = white.pos + 1 ## moves white player 1 back in the game array.
                white.x = MGB[white.pos].whitex
                white.y = MGB[white.pos].whitey
                updateDisplay()


            ###### Capture option - press c to capture. ######
        if event.key == pygame.K_c and turn == 4: ## Will only let you capture if you have the required amount of action points.
          print('White Player is attempting to capture this zone.')

          if MGB[white.pos].c == False and white.ap >= MGB[white.pos].n and turn == 4:
              MGB[white.pos].c = True
             ## access white player's pos on the main game board, and sets it to "captured."
              white.z = white.z + 1 ## Increment number of zones by 1.
              white.ap = white.ap - MGB[white.pos].n ## Subtract that many action points it took to capture.
              white.vp = white.vp + MGB[white.pos].v
              
              print('White Player has captured this zone.')
              print('White Player now has...')
              print(white.z)
              print('zones under control.')
              plantFlag(whiteflag, white.x, white.y)
              print('White Player now has')
              print(white.vp)
              print('Victory Points.')
              updateDisplay()
                               
                               
          elif turn == 4:
              print('Cannot capture zone. Not enough action points or already captured.')
              print('Required action points:')
              print(MGB[white.pos].n)
              # print('CAPTURED?')
              # print(MGB[white.pos].c)
              updateDisplay()                 

        if event.key == pygame.K_q and turn == 4:
            print('White player has ended his turn.')
            turn = 1
            print (turn)
            printinstructions = True
            upkeep = True
            updateDisplay()

    

