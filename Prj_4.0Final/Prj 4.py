import pygame, sys, random
import pygame.mixer

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

pygame.mixer.music.load('Sound/lobdan_03.mp3')    # Loads a song (can only load one song at a time)
pygame.mixer.music.play(-1)    # Plays the song (the -1 makes it loop

_display = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('parcheeeeezzii ludo')
## BG

background = pygame.image.load('Pics/bg.png')
bgSize = background.get_rect()

## Turns for the players, Game conds

turn = 1
game = True
printinstructions = True
winner = 'Player' ## not yet decided

fileNames = []
fileNames.append('Presidents')
fileNames.append('1914')
fileNames.append('1918')
fileNames.append('Austin')

presNames = []          ## create two arrays for presidents
presValues = []

fourteenNames = []      ## create two arrays for 1914
fourteenValues = []

eighteenNames = []      ## create two arrays for 1918
eighteenValues = []

austinMonths = []
austinValues = []

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

################# Location Classes

class PLocation: ## Piece location
    def __init__(loc, xcoor, ycoor,endzone,pos,done,around,color):
        loc.x = xcoor
        loc.y = ycoor
        loc.e = endzone
        loc.pos = -1 ## -1 means not on the game board.
        loc.d = done
        loc.a = False
        loc.c = color
## Red Start pieces
rp1Base = PLocation(551, 131, False, -1, False, False,'red')
rp1 = rp1Base

rp2Base = PLocation(611, 71, False, -1, False, False, 'red')
rp2 = rp2Base

rp3Base = PLocation(671, 131, False, -1, False, False, 'red')
rp3 = rp3Base

rp4Base = PLocation(611, 191, False, -1, False, False, 'red')
rp4 = rp4Base

rpc = PLocation(611, 131, False, -1, False, False, 'red')

## Blue Start pieces
bp1Base = PLocation(551, 611, False, -1, False, False, 'blue')
bp1 = bp1Base

bp2Base = PLocation(611, 551, False, -1, False, False, 'blue')
bp2 = bp2Base

bp3Base = PLocation(671, 611, False, -1, False, False, 'blue')
bp3 = bp3Base

bp4Base = PLocation(611, 671, False, -1, False, False, 'blue')
bp4 = bp4Base

## Yellow Start pieces
yp1Base = PLocation(71, 611, False, -1, False, False, 'yellow')
yp1 = yp1Base

yp2Base = PLocation(131, 551, False, -1, False, False, 'yellow')
yp2 = yp2Base

yp3Base = PLocation(191, 611, False, -1, False, False, 'yellow')
yp3 = yp3Base

yp4Base = PLocation(131, 671, False, -1, False, False, 'yellow')
yp4 = yp4Base

## Green Start pieces
gp1Base = PLocation(71, 131, False, -1, False, False, 'green')
gp1 = gp1Base

gp2Base = PLocation(131, 71, False, -1, False, False, 'green')
gp2 = gp2Base

gp3Base = PLocation(191, 131, False, -1, False, False, 'green')
gp3 = gp3Base

gp4Base = PLocation(131, 191, False, -1, False, False, 'green')
gp4 = gp4Base


##### PIECE CONFIG


# Red
redpiece1 = pygame.image.load('Pics/RED1.png')
rp1X = rp1.x
rp1Y = rp1.y
rp1pos = rp1.pos
redpiece2 = pygame.image.load('Pics/RED1.png')
rp2X = rp2.x
rp2Y = rp2.y
rp2pos = rp2.pos
redpiece3 = pygame.image.load('Pics/RED1.png')
rp3X = rp3.x
rp3Y = rp3.y
rp3pos = rp3.pos
redpiece4 = pygame.image.load('Pics/RED1.png')
rp4X = rp4.x
rp4Y = rp4.y
rp4pos = rp4.pos

redarr = [rp1pos,rp2pos,rp3pos,rp4pos]

# Blue
bluepiece1 = pygame.image.load('Pics/BLUE1.png')
bp1X = bp1.x
bp1Y = bp1.y
bp1pos = bp1.pos
bluepiece2 = pygame.image.load('Pics/BLUE1.png')
bp2X = bp2.x
bp2Y = bp2.y
bp2pos = bp2.pos
bluepiece3 = pygame.image.load('Pics/BLUE1.png')
bp3X = bp3.x
bp3Y = bp3.y
bp3pos = bp3.pos
bluepiece4 = pygame.image.load('Pics/BLUE1.png')
bp4X = bp4.x
bp4Y = bp4.y
bp4pos = bp4.pos

bluearr = [bp1pos, bp2pos, bp3pos, bp4pos]

# Yellow
yellowpiece1 = pygame.image.load('Pics/YELLOW1.png')
yp1X = yp1.x
yp1Y = yp1.y
yp1pos = yp1.pos
yellowpiece2 = pygame.image.load('Pics/YELLOW1.png')
yp2X = yp2.x
yp2Y = yp2.y
yp2pos = yp2.pos
yellowpiece3 = pygame.image.load('Pics/YELLOW1.png')
yp3X = yp3.x
yp3Y = yp3.y
yp3pos = yp3.pos
yellowpiece4 = pygame.image.load('Pics/YELLOW1.png')
yp4X = yp4.x
yp4Y = yp4.y
yp4pos = yp4.pos

yellowarr = [yp1pos,yp2pos,yp3pos,yp4pos]


# Green
greenpiece1 = pygame.image.load('Pics/GREEN1.png')
gp1X = gp1.x
gp1Y = gp1.y
gp1pos = gp1.pos
greenpiece2 = pygame.image.load('Pics/GREEN1.png')
gp2X = gp2.x
gp2Y = gp2.y
gp2pos = gp2.pos
greenpiece3 = pygame.image.load('Pics/GREEN1.png')
gp3X = gp3.x
gp3Y = gp3.y
gp3pos = gp3.pos
greenpiece4 = pygame.image.load('Pics/GREEN1.png')
gp4X = gp4.x
gp4Y = gp4.y
gp4pos = gp4.pos


greenarr = [gp1pos,gp2pos,gp3pos,gp4pos]


class TLocation: ## Gameboard spots
    def __init__(loc, xcoor, ycoor, occupied, barricade):
        loc.x = xcoor
        loc.y = ycoor
        loc.o = occupied
        loc.b = barricade
## Main Gameboard
    

s0 = TLocation(431, 131, 0, False)  
s1 = TLocation(431, 191, 0, False)
s2 = TLocation(431, 251, 0, False)
s3 = TLocation(491, 311, 0, False)
s4 = TLocation(551, 311, 0, False)
s5 = TLocation(611, 311, 0, False)
s6 = TLocation(671, 311, 0, False)
s7 = TLocation(731, 311, 0, False)
s8 = TLocation(731, 371, 0, False)
s9 = TLocation(731, 431, 0, False)
s10 = TLocation(611, 431, 0, False)
s11 = TLocation(551, 431, 0, False)
s12 = TLocation(491, 431, 0, False)
s13 = TLocation(431, 491, 0, False)
s14 = TLocation(431, 551, 0, False)
s15 = TLocation(431, 611, 0, False)
s16 = TLocation(431, 671, 0, False)
s17 = TLocation(431, 731, 0, False)
s18 = TLocation(371, 731, 0, False)
s19 = TLocation(311, 731, 0, False)
s20 = TLocation(311, 611, 0, False)
s21 = TLocation(311, 551, 0, False)
s22 = TLocation(311, 491, 0, False)
s23 = TLocation(251, 431, 0, False)
s24 = TLocation(191, 431, 0, False)
s25 = TLocation(131, 431, 0, False)
s26 = TLocation(71, 431, 0, False)
s27 = TLocation(11, 431, 0, False)
s28 = TLocation(11, 371, 0, False)
s29 = TLocation(11, 311, 0, False)
s30 = TLocation(131, 311, 0, False)
s31 = TLocation(191, 311, 0, False)
s32 = TLocation(251, 311, 0, False)
s33 = TLocation(311, 251, 0, False)
s34 = TLocation(311, 191, 0, False)
s35 = TLocation(311, 131, 0, False)
s36 = TLocation(311, 71, 0, False)
s37 = TLocation(311, 11, 0, False)
s38 = TLocation(371, 11, 0, False)
s39 = TLocation(431, 11, 0, False)




## End Zone tiles:



r0 = TLocation(431, 71, 0, False)
r1 = TLocation(371, 71, 0, False)
r2 = TLocation(371, 131, 0, False)
r3 = TLocation(371, 191, 0, False)
r4 = TLocation(371, 251, 0, False)

rf = TLocation(375, 350, 0, False)


b0 = TLocation(671, 431, 0, False)
b1 = TLocation(671, 371, 0, False)
b2 = TLocation(611, 371, 0, False)
b3 = TLocation(551, 371, 0, False)
b4 = TLocation(491, 371, 0, False)

bf = TLocation(450, 400, 0, False)

y0 = TLocation(311, 671, 0, False)
y1 = TLocation(371, 671, 0, False)
y2 = TLocation(371, 611, 0, False)
y3 = TLocation(371, 551, 0, False)
y4 = TLocation(371, 491, 0, False)

yf = TLocation(400, 450, 0, False)

g0 = TLocation(71, 311, 0, False)
g1 = TLocation(71, 371, 0, False)
g2 = TLocation(71+60, 371, 0, False)
g3 = TLocation(71+60+60, 371, 0, False)
g4 = TLocation(71+60+60+60, 371, 0, False)

gf = TLocation(350, 400, 0, False)

RGB = [r0,r1,r2,r3,r4,rf]
BGB = [b0,b1,b2,b3,b4,bf]
YGB = [y0,y1,y2,y3,y4,yf]
GGB = [g0,g1,g2,g3,g4,gf]


MGB1 = [s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,r0,r1,r2,r3,r4,rf]
MGB2 = [s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,b0,b1,b2,b3,b4,bf]
MGB3 = [s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,y0,y1,y2,y3,y4,yf]
MGB4 = [s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,g0,g1,g2,g3,g4,gf]


##### Move method

class MovePiece:
    x = 0

def randIndex():
    return random.randint(0,11)

def rollMove():
    global lastResource
    global resourceCount
    movemove.play()
    print('Choose how to determine dice roll for your piece.')
    print('Birth month of Presidents, Inflation from the year 1914,')
    print('Inflation from the year 1918, or average monthly temperatures of Austin, TX.')
    print('Accepted inputs are : Presidents, 1914, 1918, Austin')
    ## print(lastResource)
    ## print(resourceCount)

    file = input( ' : ' )
    print('file equals')
    print(file)
    print('lastResource equals')
    print(lastResource)
    print('file == lastResource')
    print(file == lastResource)

    if (file == lastResource):
        resourceCount += 1
        print(lastResource)
        print(resourceCount)

    while(resourceCount >=2):
        print('That resource is being abused.  You are required to choose a different resource.')
        print(lastResource)
        print('  is the resource that is not permitted.')
        file = input('Choose how to determine your dice roll: ' )

        if (file != lastResource):
            resourceCount = 0

    while file not in fileNames:

        move2.play()
        print('That is not a valid option for dice roll. Choose an input from Presidents, 1914, 1918.')
        file = input( ' : ' )

    if(file == 'Presidents'):
        print('Input one of the following Presidents : ')
        print(' Washington, Obama, Arthur, Bush, Monroe, Cleveland, ')
        print('Buren, Coolidge, Harding, Fillmore, Kennedy, Taft ')
        print('Spelling and capitalization must be exact. ')
        ask = input( ' : ' )

        lastResource = 'Presidents'
        print(lastResource)

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
            print('Your dice roll is 0. Your turn is over.')
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
        return finalRoll

    if (file == '1914'):
        print('Input the abbrevition for a month : ')
        print(' Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec ')
        ask = input( ' : ' )

        lastResource = '1914'

        while ask not in fourteenNames:
            print('That is not a valid month.  Try again.  Remember, only the first three letters.')
            ask = input ( ' : ' )
    
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
        return finalRoll

    if (file == '1918'):
        print('Input the abbrevition for a month : ')
        print(' Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec ')
        ask = input( ' : ' )

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
        return finalRoll

    if (file == 'Austin'):

        print('Input the abbrevition for a month : ')
        print(' Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec ')
        ask = input( ' : ' )

        lastResource = 'Austin'

        while ask not in austinMonths:
            print('You did not enter a valid month.  Try again.' )
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
        return finalRoll

# Example - move the red piece from home to s0.


while game:

 ## Displays
 _display.blit(background, bgSize)
 _display.blit(redpiece1,(rp1X, rp1Y))
 _display.blit(redpiece2,(rp2X, rp2Y))
 _display.blit(redpiece3,(rp3X, rp3Y))
 _display.blit(redpiece4,(rp4X, rp4Y))
 _display.blit(bluepiece1,(bp1X, bp1Y))
 _display.blit(bluepiece2,(bp2X, bp2Y))
 _display.blit(bluepiece3,(bp3X, bp3Y))
 _display.blit(bluepiece4,(bp4X, bp4Y))
 _display.blit(yellowpiece1,(yp1X, yp1Y))
 _display.blit(yellowpiece2,(yp2X, yp2Y))
 _display.blit(yellowpiece3,(yp3X, yp3Y))
 _display.blit(yellowpiece4,(yp4X, yp4Y))
 _display.blit(greenpiece1,(gp1X, gp1Y))
 _display.blit(greenpiece2,(gp2X, gp2Y))
 _display.blit(greenpiece3,(gp3X, gp3Y))
 _display.blit(greenpiece4,(gp4X, gp4Y))
 
  
 pygame.display.flip()
 mainClock.tick(32)

 for event in pygame.event.get():
    if game == False:
        turn = 5
     
    if turn == 1 and printinstructions:
        movemove.play()
        print('Red Player turn to roll the dice')
        r = MovePiece()
        r.move = rollMove()
        #(int)(input('Red Player, please enter a value:')) ## make your selection. ## Put any other values and it will break the code.
        print('Red player turn - press up to move first piece, press down to move second piece, right to move 3rd, left to move 4th')
        printinstructions = False
    if turn == 2 and printinstructions:
        movemove.play()
        print('Blue Player turn to roll the dice')
        r = MovePiece()
        r.move = rollMove()
        # (int)(input('Blue Player, please enter a value:')) ## make your selection. ## Put any other values and it will break the code.
        print('Blue player turn - press up to move first piece, press down to move second piece, right to move 3rd, left to move 4th')
        printinstructions = False
    if turn == 3 and printinstructions:
        movemove.play()
        print('Yellow Player turn to roll the dice')
        r = MovePiece()
        r.move = rollMove()
        # (int)(input('Yellow Player, please enter a value:')) ## make your selection. ## Put any other values and it will break the code.
        print('Yellow player turn - press up to move first piece, press down to move second piece, right to move 3rd, left to move 4th')
        printinstructions = False
    if turn == 4 and printinstructions:
        movemove.play()
        print('Green Player turn to roll the dice')
        r = MovePiece()
        r.move = rollMove()
        # (int)(input('Green Player, please enter a value:')) ## make your selection. ## Put any other values and it will break the code.
        print('Green player turn - press up to move first piece, press down to move second piece, right to move 3rd, left to move 4th')
        printinstructions = False
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if turn == 5:
        move3.play()
        pygame.mixer.music.load('Sound/aost01.mp3')    # Loads a song (can only load one song at a time)
        pygame.mixer.music.play(-1)    # Plays the song (the -1 makes it loop
        print('Game is over.')
        print (winner)
        
    

##### Red TURN
   ##############################################

    if turn == 1 and event.type == pygame.KEYDOWN:
        print ('Turn =')
        print (turn)
## RED PIECE 1        
        if event.key == pygame.K_UP:
          print('Red Player, 1st Piece attemping to move')
          print(rp1.d)
          move = r.move ## Die roll
          mover2 = rp1pos + move ## Die roll + current position
          print(mover2)
          if mover2 > 45:
              mover2 = 45
          

          if (rp1.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if rp1pos < 45 and rp1.d == False:
              rp1pos = mover2
              print(rp1pos)
          ## First, check conds.
              if MGB1[rp1pos].o == False and MGB1[rp1pos].b == False: ## 
                  rp1X = MGB1[rp1pos].x ## Change x and y values.
                  rp1Y = MGB1[rp1pos].y

                  # print('refreshing display')
                  _display.blit(redpiece1,(rp1X, rp1Y)) ## Refresh Display
                  turn = 2
                  printinstructions = True
          if rp1pos == 45 and rp1.d == False:
              print('Red Piece #1 completed!')
              rp1.d = True
              turn = 2
              printinstructions = True
              if rp1.d and rp2.d and rp3.d and rp4.d: ## END GAME
                  print('RED PLAYER WINS!!')
                  game = False
                  winner = 'Red Player'


## RED PIECE 2         
        if event.key == pygame.K_DOWN:
          print('Red Player, 2st Piece attemping to move')
          # print(rp2.d)
          move = r.move ## Die roll
          mover2 = rp2pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          

          if (rp2.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp2pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if rp2pos < 45 and rp2.d == False:
              rp2pos = mover2
              # print(rp2pos)
          ## First, check conds.
              if MGB2[rp2pos].o == False and MGB2[rp2pos].b == False: ## 
                  rp2X = MGB1[rp2pos].x ## Change x and y values.
                  rp2Y = MGB1[rp2pos].y

                  # print('refreshing display')
                  _display.blit(redpiece2,(rp2X, rp2Y)) ## Refresh Display
                  turn = 2
                  printinstructions = True
          if rp2pos == 45 and rp2.d == False:
              print('Red Piece #2 completed!')
              rp2.d = True
              turn = 2
              printinstructions = True
              if rp1.d and rp2.d and rp3.d and rp4.d: ## END GAME ## DO NOT CHANGE FOR RED
                  print('RED PLAYER WINS!!')
                  game = False
                  winner = 'Red Player'

## RED PIECE 3

              
        if event.key == pygame.K_RIGHT:
          print('Red Player, 3rd Piece attemping to move')
          # print(rp3.d)
          move = r.move ## Die roll
          mover2 = rp3pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          

          if (rp3.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp2pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if rp3pos < 45 and rp3.d == False:
              rp3pos = mover2
              # print(rp3pos)
          ## First, check conds.
              if MGB1[rp3pos].o == False and MGB1[rp3pos].b == False: ## 
                  rp3X = MGB1[rp3pos].x ## Change x and y values.
                  rp3Y = MGB1[rp3pos].y

                  # print('refreshing display')
                  _display.blit(redpiece3,(rp3X, rp3Y)) ## Refresh Display
                  turn = 2
                  printinstructions = True
          if rp3pos == 45 and rp3.d == False:
              print('Red Piece #3 completed!')
              rp3.d = True
              turn = 2
              printinstructions = True
              if rp1.d and rp2.d and rp3.d and rp4.d: ## END GAME ## DO NOT CHANGE FOR RED
                  print('RED PLAYER WINS!!')
                  game = False
                  winner = 'Red Player'

## RED PIECE 4
       

        if event.key == pygame.K_LEFT:
          print('Red Player, 4th Piece attemping to move')
          # print(rp4.d)
          move = r.move ## Die roll
          mover2 = rp4pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          

          if (rp4.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp2pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if rp4pos < 45 and rp4.d == False:
              rp4pos = mover2
              # print(rp4pos)
          ## First, check conds.
              if MGB1[rp4pos].o == False and MGB1[rp4pos].b == False: ## 
                  rp4X = MGB1[rp4pos].x ## Change x and y values.
                  rp4Y = MGB1[rp4pos].y

                  # print('refreshing display')
                  _display.blit(redpiece4,(rp4X, rp4Y)) ## Refresh Display
                  turn = 2
                  printinstructions = True
          if rp4pos == 45 and rp4.d == False:
              print('Red Piece #4 completed!')
              rp4.d = True
              turn = 2
              printinstructions = True
              if rp1.d and rp2.d and rp3.d and rp4.d: ## END GAME ## DO NOT CHANGE FOR RED
                  print('RED PLAYER WINS!!')
                  game = False
                  winner = 'Red Player'


##### Blue Turn
   ##############################################
    elif turn == 2 and event.type == pygame.KEYDOWN:   
## BLUE PIECE 1
      if event.key == pygame.K_UP:
          print('Blue Player, 1st Piece attemping to move')
          # print(bp1.d)
          move = r.move ## Die roll
          mover2 = bp1pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          
          if (bp1.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if bp1pos < 45 and bp1.d == False:
              bp1pos = mover2
              # print(bp1pos)
          ## First, check conds.
              if MGB2[bp1pos].o == False and MGB2[bp1pos].b == False: ## 
                  bp1X = MGB2[bp1pos].x ## Change x and y values.
                  bp1Y = MGB2[bp1pos].y

                  # print('refreshing display')
                  _display.blit(bluepiece1,(bp1X, bp1Y)) ## Refresh Display
                  turn = 3
                  printinstructions = True
          if bp1pos == 45 and bp1.d == False:
              print('Blue Piece #1 completed!')
              bp1.d = True
              turn = 3
              printinstructions = True
              if bp1.d and bp2.d and bp3.d and bp4.d: ## END GAME
                  print('Blue PLAYER WINS!!')
                  game = False
                  winner = 'Blue Player'

## BLUE PIECE 2
      if event.key == pygame.K_DOWN:
          print('Blue Player, 2nd Piece attemping to move')
          # print(bp2.d)
          move = r.move ## Die roll
          mover2 = bp2pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          
          if (bp2.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if bp2pos < 45 and bp2.d == False:
              bp2pos = mover2
              # print(bp2pos)
          ## First, check conds.
              if MGB2[bp2pos].o == False and MGB2[bp2pos].b == False: ## 
                  bp2X = MGB2[bp2pos].x ## Change x and y values.
                  bp2Y = MGB2[bp2pos].y

                  # print('refreshing display')
                  _display.blit(bluepiece2,(bp2X, bp2Y)) ## Refresh Display
                  turn = 3
                  printinstructions = True
          if bp2pos == 45 and bp2.d == False:
              print('Blue Piece #2 completed!')
              bp2.d = True
              turn = 3
              printinstructions = True
              if bp1.d and bp2.d and bp3.d and bp4.d: ## END GAME
                  print('Blue PLAYER WINS!!')
                  game = False
                  winner = 'Blue Player'

## BLUE PIECE 3
      if event.key == pygame.K_RIGHT:
          print('Blue Player, 3rd Piece attemping to move')
          # print(bp3.d)
          move = r.move ## Die roll
          mover2 = bp3pos + move ## Die roll + current position 
          if mover2 > 45:
              mover2 = 45
          
          if (bp3.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if bp3pos < 45 and bp3.d == False:
              bp3pos = mover2
              # print(bp3pos)
          ## First, check conds.
              if MGB2[bp3pos].o == False and MGB2[bp3pos].b == False: ## 
                  bp3X = MGB2[bp3pos].x ## Change x and y values.
                  bp3Y = MGB2[bp3pos].y

                  # print('refreshing display')
                  _display.blit(bluepiece3,(bp3X, bp3Y)) ## Refresh Display
                  turn = 3
                  printinstructions = True
          if bp3pos == 45 and bp3.d == False:
              print('Blue Piece #3 completed!')
              bp3.d = True
              turn = 3
              printinstructions = True
              if bp1.d and bp2.d and bp3.d and bp4.d: ## END GAME
                  print('Blue PLAYER WINS!!')
                  game = False
                  winner = 'Blue Player'


## BLUE PIECE 4
      if event.key == pygame.K_LEFT:
          print('Blue Player, 4th Piece attemping to move')
          # print(bp4.d)
          move = r.move ## Die roll
          mover2 = bp4pos + move ## Die roll + current position 
          if mover2 > 45:
              mover2 = 45
          
          if (bp4.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if bp4pos < 45 and bp4.d == False:
              bp4pos = mover2
              # print(bp4pos)
          ## First, check conds.
              if MGB2[bp4pos].o == False and MGB2[bp4pos].b == False: ## 
                  bp4X = MGB2[bp4pos].x ## Change x and y values.
                  bp4Y = MGB2[bp4pos].y

                  # print('refreshing display')
                  _display.blit(bluepiece4,(bp4X, bp4Y)) ## Refresh Display
                  turn = 3
                  printinstructions = True
          if bp4pos == 45 and bp4.d == False:
              print('Blue Piece #4 completed!')
              bp4.d = True
              turn = 3
              printinstructions = True
              if bp1.d and bp2.d and bp3.d and bp4.d: ## END GAME
                  print('Blue PLAYER WINS!!')
                  game = False
                  winner = 'Blue Player'


##### Yellow Turn
   ##############################################
    elif turn == 3 and event.type == pygame.KEYDOWN:   
## YELLOW PIECE 1
      if event.key == pygame.K_UP:
          print('Yellow Player, 1st Piece attemping to move')
          # print(yp1.d)
          move = r.move ## Die roll
          mover2 = yp1pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          
          if (yp1.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if yp1pos < 45 and yp1.d == False:
              yp1pos = mover2
              # print(yp1pos)
          ## First, check conds.
              if MGB3[yp1pos].o == False and MGB3[yp1pos].b == False: ## 
                  yp1X = MGB3[yp1pos].x ## Change x and y values.
                  yp1Y = MGB3[yp1pos].y

                  # print('refreshing display')
                  _display.blit(yellowpiece1,(yp1X, yp1Y)) ## Refresh Display
                  turn = 4
                  printinstructions = True
          if yp1pos == 45 and yp1.d == False:
              print('Yellow Piece #1 completed!')
              yp1.d = True
              turn = 4
              printinstructions = True
              if yp1.d and yp2.d and yp3.d and yp4.d: ## END GAME
                  print('YELLOW PLAYER WINS!!')
                  game = False
                  winner = 'Yellow Player'
## YELLOW PIECE 2
      if event.key == pygame.K_DOWN:
          print('Yellow Player, 2ND Piece attemping to move')
          # print(yp2.d)
          move = r.move ## Die roll
          mover2 = yp2pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          
          if (yp2.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if yp2pos < 45 and yp2.d == False:
              yp2pos = mover2
              # print(yp2pos)
          ## First, check conds.
              if MGB3[yp2pos].o == False and MGB3[yp2pos].b == False: ## 
                  yp2X = MGB3[yp2pos].x ## Change x and y values.
                  yp2Y = MGB3[yp2pos].y

                  # print('refreshing display')
                  _display.blit(yellowpiece2,(yp2X, yp2Y)) ## Refresh Display
                  turn = 4
                  printinstructions = True
          if yp2pos == 45 and yp2.d == False:
              print('Yellow Piece #2 completed!')
              yp2.d = True
              turn = 4
              printinstructions = True
              if yp1.d and yp2.d and yp3.d and yp4.d: ## END GAME
                  print('YELLOW PLAYER WINS!!')
                  game = False
                  winner = 'Yellow Player'

## YELLOW PIECE 3
      if event.key == pygame.K_RIGHT:
          print('Yellow Player, 3rd Piece attemping to move')
          # print(yp3.d)
          move = r.move ## Die roll
          mover2 = yp3pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          
          if (yp3.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if yp3pos < 45 and yp3.d == False:
              yp3pos = mover2
              # print(yp3pos)
          ## First, check conds.
              if MGB3[yp3pos].o == False and MGB3[yp3pos].b == False: ## 
                  yp3X = MGB3[yp3pos].x ## Change x and y values.
                  yp3Y = MGB3[yp3pos].y

                  # print('refreshing display')
                  _display.blit(yellowpiece3,(yp3X, yp3Y)) ## Refresh Display
                  turn = 4
                  printinstructions = True
          if yp3pos == 45 and yp3.d == False:
              print('Yellow Piece #3 completed!')
              yp3.d = True
              turn = 4
              printinstructions = True
              if yp1.d and yp2.d and yp3.d and yp4.d: ## END GAME
                  print('YELLOW PLAYER WINS!!')
                  game = False
                  winner = 'Yellow Player'


## YELLOW PIECE 4
      if event.key == pygame.K_LEFT:
          print('Yellow Player, 4th Piece attemping to move')
          # print(yp4.d)
          move = r.move ## Die roll
          mover2 = yp4pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          
          if (yp4.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if yp4pos < 45 and yp4.d == False:
              yp4pos = mover2
              # print(yp4pos)
          ## First, check conds.
              if MGB3[yp4pos].o == False and MGB3[yp4pos].b == False: ## 
                  yp4X = MGB3[yp4pos].x ## Change x and y values.
                  yp4Y = MGB3[yp4pos].y

                  # print('refreshing display')
                  _display.blit(yellowpiece4,(yp4X, yp4Y)) ## Refresh Display
                  turn = 4
                  printinstructions = True
          if yp4pos == 45 and yp4.d == False:
              print('Yellow Piece #4 completed!')
              yp4.d = True
              turn = 4
              printinstructions = True
              if yp1.d and yp2.d and yp3.d and yp4.d: ## END GAME
                  print('YELLOW PLAYER WINS!!')
                  game = False
                  winner = 'Yellow Player'


##### Green Turn
   ##############################################
    elif turn == 4 and event.type == pygame.KEYDOWN:   
## GREEN PIECE 1
      if event.key == pygame.K_UP:
          print('Green Player, 1st Piece attemping to move')
          # print(gp1.d)
          move = r.move ## Die roll
          mover2 = gp1pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          
          if (gp1.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if gp1pos < 45 and gp1.d == False:
              gp1pos = mover2
              # print(gp1pos)
          ## First, check conds.
              if MGB4[gp1pos].o == False and MGB4[gp1pos].b == False: ## 
                  gp1X = MGB4[gp1pos].x ## Change x and y values.
                  gp1Y = MGB4[gp1pos].y

                  # print('refreshing display')
                  _display.blit(greenpiece1,(gp1X, gp1Y)) ## Refresh Display
                  turn = 1
                  printinstructions = True
          if gp1pos == 45 and gp1.d == False:
              print('Green Piece #1 completed!')
              gp1.d = True
              turn = 1
              printinstructions = True
              if gp1.d and gp2.d and gp3.d and gp4.d: ## END GAME
                  print('GREEN PLAYER WINS!!')
                  game = False
                  winner = 'Green Player'

## GREEN PIECE 2
      if event.key == pygame.K_DOWN:
          print('Green Player, 2nd Piece attemping to move')
          # print(gp2.d)
          move = r.move ## Die roll
          mover2 = gp2pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          
          if (gp2.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if gp2pos < 45 and gp2.d == False:
              gp2pos = mover2
              # print(gp2pos)
          ## First, check conds.
              if MGB4[gp2pos].o == False and MGB4[gp2pos].b == False: ## 
                  gp2X = MGB4[gp2pos].x ## Change x and y values.
                  gp2Y = MGB4[gp2pos].y

                  # print('refreshing display')
                  _display.blit(greenpiece2,(gp2X, gp2Y)) ## Refresh Display
                  turn = 1
                  printinstructions = True
          if gp2pos == 45 and gp2.d == False:
              print('Green Piece #2 completed!')
              gp2.d = True
              turn = 1
              printinstructions = True
              if gp1.d and gp2.d and gp3.d and gp4.d: ## END GAME
                  print('GREEN PLAYER WINS!!')
                  game = False
                  winner = 'Green Player'

## GREEN PIECE 3
      if event.key == pygame.K_RIGHT:
          print('Green Player, 3RD Piece attemping to move')
          # print(gp3.d)
          move = r.move ## Die roll
          mover2 = gp3pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          
          if (gp3.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if gp3pos < 45 and gp3.d == False:
              gp3pos = mover2
              # print(gp3pos)
          ## First, check conds.
              if MGB4[gp3pos].o == False and MGB4[gp3pos].b == False: ## 
                  gp3X = MGB4[gp3pos].x ## Change x and y values.
                  gp3Y = MGB4[gp3pos].y

                  # print('refreshing display')
                  _display.blit(greenpiece3,(gp3X, gp3Y)) ## Refresh Display
                  turn = 1
                  printinstructions = True
          if gp3pos == 45 and gp3.d == False:
              print('Green Piece #3 completed!')
              gp3.d = True
              turn = 1
              printinstructions = True
              if gp1.d and gp2.d and gp3.d and gp4.d: ## END GAME
                  print('GREEN PLAYER WINS!!')
                  game = False
                  winner = 'Green Player'


## GREEN PIECE 4
      if event.key == pygame.K_LEFT:
          print('Green Player, 4TH Piece attemping to move')
          # print(gp4.d)
          move = r.move ## Die roll
          mover2 = gp4pos + move ## Die roll + current position
          if mover2 > 45:
              mover2 = 45
          
          if (gp4.d):
              print('You cannot move this piece! Choose another piece to move.')


          ## Increment rp1pos by the die roll amount. Save die roll as local var so if it fails, you can return back to original pos.
          if gp4pos < 45 and gp4.d == False:
              gp4pos = mover2
              # print(gp4pos)
          ## First, check conds.
              if MGB4[gp4pos].o == False and MGB4[gp4pos].b == False: ## 
                  gp4X = MGB4[gp4pos].x ## Change x and y values.
                  gp4Y = MGB4[gp4pos].y

                  # print('refreshing display')
                  _display.blit(greenpiece4,(gp4X, gp4Y)) ## Refresh Display
                  turn = 1
                  printinstructions = True
          if gp4pos == 45 and gp4.d == False:
              print('Green Piece #4 completed!')
              gp4.d = True
              turn = 1
              printinstructions = True
              if gp1.d and gp2.d and gp3.d and gp4.d: ## END GAME
                  print('GREEN PLAYER WINS!!')
                  game = False
                  winner = 'Green Player'


##################################################


