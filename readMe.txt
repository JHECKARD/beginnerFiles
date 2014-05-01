
This is a file repository for my undragraduate and gaming projects.  


///// *****     Python Project 4 - Ludo     ***** /////
Prj_4.0Final is a recreation of Ludo / Parcheesi in Python and
 Pygame.  This game was built in Python 3.0.  
It uses a non-standard dice generator that requires knowledge of
 President months of birth and monthly inflation rates for the years 1914 and 1918.  

Limiting resources and abusing knowledge of resources (values 
which have the ability to roll a 6) were required elements of game design.

My role was dice generator programmer and designer for this project.


///// *****     Python Project 5 - Conquest     *****/////
PRJ_5.0 is similar in design to the Ludo / Parcheesi project in 
 Python and Pygame.  This game was built in Python 3.0.  
It uses a non-standard dice generator that requires knowledge of
 President months of birth and monthly inflation rates for the years 1914 and 1918.  Monthly temperatures of Austin, TX and 
birth months of famous scientists were added for this project.  

Instead of the dice roll determining how far the player moves, 
the dice generator grants the player a number of "action points" 
to move around the board.  Zones in the board are stored in a 
1-D array, and the player moves 'left' or 'right' along the 
array, which approximates moving back and forth between 
nearby zones.  Each zone can be Captured for a certain number of 
action points and grants a certain number of Victory Points 
(the number of action points and the number of Victory Points 
may not be the same).  The first player to gain 10 Victory 
Points wins the game.

Limiting resources and abusing knowledge of resources (values which have the ability to roll a 6) were required elements of game design.

My role was dice generator programmer (continued) and win 
condition designer for this project.  


///// *****     Processing Black Hole v 4.0     ***** /////
Black Hole v 4.0 is a class project that was built in Processing 
(www.processing.org, natureofcode.com).  This iteration of the  
project focused on interactivity, and the Black Hole is activated 
by the left mouse button.  

Another element of the project is collision detection.  Collision 
detection happens between the center of the Black Hole and the 
top-left corner of the default satelite.  Collision between the 
Black Hole and planets/stars is based on center-to-center. 
 
(it's not a bug, it's a bonus feature :-) )

Motion of the Black Hole is based on mouse position.  Motion of 
all other ships, planets, and stars uses physics-based vectors 
(the magnitude-type, not the data-storage type) with position, 
velocity, and acceleration.  


///// *****     Processing Black Hole v 8.0     ***** /////
A continuation of the Black Hole project.  

The start screen was generated sideways to be run on Android 
devices.  The height/width requirements for the game to be 
run on an Android device exist inside the code, commented out.  

Added features:  
sound of activating the Black Hole power, and collision with 
objects
a Photoshop-manipulated background image that makes the distant 
stars harder to see
Sprite space ships, using a free sprite sheet found online 
image and sound credits 