
This is a file repository for my undragraduate and gaming projects.  

Prj 4.0Final is a recreation of Ludo / Parcheesi in Python and Pygame.  This game was built in Python 3.0.  
It uses a non-standard dice generator that requires knowledge of President months of birth and monthly inflation rates for the years 1914 and 1918.  
Limiting resources and abusing knowledge of resources (values which have the ability to roll a 6) were required elements of game design.


PRJ 5.0 is a game similar to Prj 4.0Final.  Instead of being a game of Ludo, it now uses a map for War of the Lances (Dungeons and Dragons-theme board game, credited in README).  When a player rolls the dice, they are awarded a certain number of Action Points.  Action Points can be used to move to an adjacent zone (quasi-adjacent; control implementation is that the zones are a 1D array, and the player can move back and forth along the array, representing an almost realistic map travel).  Players can spend action points to capture a zone, planting their flag at that zone.  The first player to capture 10 victory points wins (not all zones are worth the same, and not all zones provide the same Victory Points as their cost to capture).
This game also implements limited resources and abusable knowledge to give better chances for a higher semi-roll.  Average temperatures from the city of Austin, TX across months of a certain year was added as an additional resource for the dice roller.  