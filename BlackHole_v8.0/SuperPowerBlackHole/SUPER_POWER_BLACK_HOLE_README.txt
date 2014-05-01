Jason Heckard
UCID 84851006
ICS 62

Super Power Black Hole

Star is a class that is a tiny ellipse.  Super Power Black Hole creates an array of Stars that are randomly scattered across the background.  They are the last objects to be consumed by Black Hole, and add the least to its size. 

There are also Background Planets.  This is a layer of far-off planets  of random colors.  They can be consumed by the Black Hole.

The Satelites are the original moving objects.  They are the first space objects to be consumed by Black Hole.  They are repulsed by the gravity field of Gravity-Planets.

The Ships also exist in the next layer, and they move and fly around as well.  They are sprites, unlike the other images generated for the game.  They are repulsed by gravity field, and they are also the first objects to be consumed by Black Hole. 

Next are the Gravity-Planets.  These are red-bordered planets of randomly generated colors and sizes that have a repulsion-gravity field around them.  Their job is to push the Satelites and Ships away.  Ideally, this would prevent any collisions between the other Space Objects and the Gravity-Planets. They are the third set of space objects consumed by the Black HOle (after Satelites and Ships).

The Black Hole exists on top, set above the other space objects.  While mousePressed continues to stay true, BlackHole will pull all of the Satelites and Ships toward it and consume them!  As the Black Hole consumes Satelites, it becomes bigger, and able to consume more space objects faster!
When there are no more moving Space Objects, Black Hole will pull on the very planets who are close enough to push away the satelites!  Black Hole will attract the planets, slowly, so that it can be guided to consume all of the gravity planets!  As it consumes planets, they also add to its size, allowing the Black HOle to consume even more space obejcts!
After the Gravtiy Planets have been consumed, Black Hole still hungers!  It consumes the Background planets, then finally the very stars that light up the night sky!  Background planets and stars continue to make the black hole larger and stronger still!  When all is done, all that remains is a super massive black hole.  

Should a satelite approach the planet at an exact 45-degree angle, it will be deflected to exactly the same angle.

A Satelite is an object consisting of two rectangles (the solar panels), an ellipse (the body), and an orange internal rectangle (the control panel).  Satelite construction is formula-based, so creating multiple Satelites of different appearances could be done by passing in the origin point and size of the Satelite and the size of the solar panels.  This is used to construct a large group of randomly-generated Satelites.

A Ship is a Sprite who has the same motion properties as Satelites.  It uses pixel-based images to show that the flame of the rocket is burning.  Other than that, Ship has all of the same motion and collion properties as Satelites.

Space Objects also have three vectors assigned to them, location, velocity, and acceleration.  Interaction with the outer boundary of the background and by the repulsion fields of the Gravity-Planets is managed by manipulating the values of the acceleration vectors for each Satelite.  Pushing objects around is a generic method that belongs to the parent class SpaceObject, so any object could potentially be used to push around any other object!  This could get brutal.
Satelites and Ships also have a rotate() and translate() inside their render() class so that they are always pointing in the direction of motion.  Satelites and Ships use their angle of rotation to point in the direction of motion.

The Black Hole follows around the mouse.  It appears as a harmless dark spot at first, but by holding down the mouse button it becomes a fearsome black hole that increases the acceleration of nearby objects toward it!  It attempts to consume all the satelites and Ships first, then it takes on the rest of the galaxy!  Watch out universe, Black Hole is here!
See how Black HOle's rings rotate to show its power!

Vector-based trajectory reversal worked out pretty well.  The satelites rarely touch the planets.  Objects accelerate toward the Black Hole while mousePressed, but they still have to overcome the power of the surrounding planets. 

I'm happy with it!
