Jason Heckard
UCID 84851006
ICS 62
Week 4 Project: Transformation and Vectors

Week 4 additions:  
1) getting the week 3 failed constructors to work
2) Made the number of Stars random, 100-400
3) implemented location and motion vectors for all classes. Completed the black hole pull - now it really swallows the entire galaxy!
4) Satelites have been designed so that they (typically) rotate to point in the direction of travel. The red triangles protruding from the bottom are supposed to be the rockets, I hope that is more clear now. 
Learned this from Nature of Code CH 3.4 examples.  Took the base code, manipulated it to fit my needs, implemented the version of the code that works best.
5) Black Hole - the "force" stripes of the Black HOle rotate in place.  It has a value 0-359 that cycles through and rotates the "active" black Hole in place
6) Black HOle size is no longer a fixed value. The more it consumes, the larger it gets!
7) Game Over screen and final 'score' - Every space object has a point value based on its size. Once every object in the galaxy is eaten, the user gets to see the end screen and their score!


My project starts by generating a dark blue background.

Star is a class that is a white one-pixel point.  My program creates an array of Stars (randomly sized) that are randomly scattered across the background.  This gives the project a nice deep-space background.  They are the last objects to be consumed by Black Hole, and add the least to its size.

The third layer is the Background Planets.  This is a layer of far-off planets  of random colors designed to appear as planets in the far-off distance.  They can be consumed by the Black Hole in the third phase.

The Satelites exist in the fourth layer, and they are the moving objects.  They are the first space objects to be consumed by Black Hole.

The fifth layer are the Gravity-Planets.  These are red-bordered planetsof randomly generated colors and sizes that have a repulsion-gravity field around them.  Their job is to push the Satelites away.  Ideally, this would prevent any collisions between the Satelites and the Gravity-Planets. They are the second set of tiems to be consumed by the Black HOle.

(WK 4 REVISED) WEEK 3 ADDITION:  A new front layer object exists, the BlackHole!  While mousePressed continues to stay true, BlackHole will pull all of the Satelites toward it and consume them!  As the Black Hole consumes Satelites, it becomes bigger, and able to consume more space objects faster!
When there are no more satelites, Black Hole will pull on the very planets who are strong enough to push away the satelites!  Black Hole will attract the planets, slowly, so that it can be guided with the mouse to consume all of the gravity planets!  As it consumes planets, they also add to its size, allowing the Black HOle to consume even more space obejcts!
After the Gravtiy Planets have been consumed, Black Hole still hungers!  It consumes the Background planets, then finally the very stars that light up the night sky!  Background planets and stars continue to make the black hole larger and stronger still!  When all is done, all that remains is a super massive black hole.  
The Black Hole update() if (mousePressed) now includes a translate() and rotate().  This allows the glowing rings that represent the power of the Black Hole to slowly rotate around the ever-growing Black HOle.

Each Gravity-Planet has a round-shaped hitbox that is used to determine when to change the Satelite trajectory.  Each planet's hitbox is approximately 5 times the radius of the planet!  The planet will push away any of the satelites that come near it.  Should a satelite approach the planet at an exact 45-degree angle, it will be deflected to exactly the same angle.

A Satelite is an object consisting of two rectangles (the solar panels), an ellipse (the body), and an orange internal rectangle (the control panel).  Satelite construction is formula-based, so creating multiple Satelites of different appearances could be done by passing in the origin point and size of the Satelite and the size of the solar panels.  This could be used to construct a large group of randomly-generated Satelites.

(WK 4 REVISED) Satelites also have three vectors assigned to them, location, velocity, and acceleration.  Interaction with the outer boundary of the background and by the repulsion fields of the Gravity-Planets is managed by manipulating the values of the acceleration vectors for each Satelite.  Pushing objects around is a generic method that belongs to the parent class SpaceObject now, so any object could potentially be used to push around any other object!  This could get brutal.
Satelites now have a rotate() and translate() inside their render() class so that they are always pointing in the direction of motion.

(WK 4 REVISED) There is a Black Hole now that follows around the mouse!  It appears as a harmless dark spot at first, but by holding down the mouse button it becomes a fearsome black hole that increases the acceleration of nearby objects toward it!  It attempts to consume all the satelites first, then it takes on the rest of the galaxy!  Watch out universe, Black Hole is here!
See how Black HOle's rings rotate to show its power!

(WK 4 REVISED) Vector-based trajectory reversal worked out pretty well.  The satelites rarely if ever touch the planets.  Objects accelerate toward the black hole while mousePressed, but they still have to overcome the power of the surrounding planets.  Satelites also use their angle of rotation to point in the direction of motion.

I'm happy with it!
