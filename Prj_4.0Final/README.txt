// Parcheezi Project
// By Jason Chiu, Jason Heckard, Yessenia Orozco, Natasha Samari, Chris Walker

// Elements used: Limiting Resource, and making a new Resource.


This game is played with 4 players.

You advance your pieces by typing in the appropriate input.

You can choose from 4 categories:

Presidents, Inflation Rates by Month for 1914, Inflation rates by Month for 1918, or the AVG monthly Temperatures in Austin

Choose a category by typing in your selection. 

Next, you will be prompted to select one entry from the list of the category you chose.

Choose any one to generate a dice roll between 1 and 6.

From there, you may press the arrow keys to move any one of your pieces. 

To win, you must get all of your pieces around the board!


///


Our algorithm for generating die rolls depends on certain selections.

Some inputs will ONLY generate 1 to 2.

Very few of the inputs have the possibility to generate a 6.

Here is the list:

Presidents that can roll a 6:

Buren, Harding

Presidents that can only roll 1:

Fillmore, Washington

1914 Inflations that can roll 6:

July

1914 Inflations that only roll 1:

March

1918 Inflations that can roll 6:

Nov, Dec

1918 months that only roll a 1 or 2:

April, May, June.

Austin Months that may roll 6:

July, August

Austin Months that always roll 1

Dec, Jan, Feb

**For the values that can roll 6, they will not always roll 6s.

// Known errors:

Some pieces may appear to bug and not move until player's next turn, but they will move after the next command is given.