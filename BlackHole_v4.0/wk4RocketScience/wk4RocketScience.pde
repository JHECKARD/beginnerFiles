// Jason Heckard
// UCID 84851006
// ICS 62
// Week 4 Project

Satelite [] fleetSatelites = new Satelite[3]; // creates the 3 satelites

int numStars = int(random(100,500) );
Star[] stars = new Star[numStars]; // creates an array of stars for background 

int planetCount = int(random(6, 15) ); 
BkgdPlanet[] pretty = new BkgdPlanet[planetCount]; // creates an array of 6 to 15 background planets

int solidCount = int(random(4, 8) );
GravityPlanet[] solarSystem = new GravityPlanet[solidCount]; 
// creates an array of 4 to 8 gravity planets

BlackHole bh1 = new BlackHole( int( random(20, 50) ) ); // new class:  Black Hole!  
// Powered by the mouse button (left)
// hold down the mouse button and watch the Black Hole consume the world!

int spaceWidth, spaceHeight;

void setup()
{
  spaceWidth = 1213;
  spaceHeight = 613;
  size(spaceWidth, spaceHeight); // sets the background
  smooth();
  ellipseMode(CORNER);

  for (int starCount = 0; starCount < stars.length; starCount++)
  {
    stars[starCount] = new Star(int(random(spaceWidth)), int(random(spaceHeight) ), 0.00001 );
  } // fills the array of stars in random locations across the background
    // Stars have the slowest response to Black Hole's force pull

  for (int bkgdCount = 0; bkgdCount < pretty.length; bkgdCount++)
  {
    pretty[bkgdCount] = new BkgdPlanet (spaceWidth, spaceHeight, 0.00002);
  } // fills the array of background planets across the background
    // background planets now respond to the Black Hole, once all gravity planets have been consumed

  fleetSatelites[0] = new Satelite (25, 25, 30, 40, 20, spaceWidth, spaceHeight, 0.001);
  fleetSatelites[1] = new Satelite (100, 100, 40, 40, 20, spaceWidth, spaceHeight, 0.001);
  fleetSatelites[2] = new Satelite (425, 225, 50, 20, 20, spaceWidth, spaceHeight, 0.001);
  // creates the three Satelites of different appearance properties

  for (int gravCount = 0; gravCount < solarSystem.length; gravCount++)
  {
    solarSystem[gravCount] = new GravityPlanet( int(random(spaceWidth) ), 
    int(random(spaceHeight) ), int(random(50, 80) ), spaceWidth, spaceHeight, 0.00003);
  } // fills the array of Gravity Planets across the background
}

void draw()
{
  background(10, 10, 75); // sets the background to dark blue

  for (int starRenderCount = 0; starRenderCount < stars.length; starRenderCount++)
  {
    if (stars[starRenderCount] != null)
    {
      stars[starRenderCount].render();
    }
  } // places the stars in the background, giving the deep space appearance

  for (int bkgdRenderCount = 0; bkgdRenderCount < pretty.length; bkgdRenderCount++)
  {
    if (pretty[bkgdRenderCount] != null)
    {
      pretty[bkgdRenderCount].render();
    }
  } // places the background planets in the background, layered on top of the stars

  for (int sateliteCount = 0; sateliteCount < fleetSatelites.length; sateliteCount++)
  {
    if (fleetSatelites[sateliteCount] != null)
    {
      fleetSatelites[sateliteCount].render();
    }
  } // places the satelites that have not been destroyed by blackHole

  for (int gravRenderCount = 0; gravRenderCount < solarSystem.length; 
    gravRenderCount++)
  {
    if (solarSystem[gravRenderCount] != null)
    {
      solarSystem[gravRenderCount].render();
    }
  } // renders the red-bordered Gravity Planets in the background

  bh1.render();
//  setup();

  // Notice that now, all of the class arrays know if a specific element is null!
  // This is because they might get eaten by the Black Hole!
  // And now, Black Hole can consume everything!


  ////////////////////  BEGIN COLLISION DETECTION ALGORITHM    ////////////////////

  // Created collision detection for Satelite fleetSatelites[sateliteCount]
  //  with Gravity planets

  // float d = dist(sat.centerX,sat.centerY,planet.centerX,planet.centerY);
  // if (d < planet.planetplanetSize * 2) {...}
  //
  // float angle = atan2(planet.y-sat.y,planet.x-sat.x);
  // sat.velX += const * cos(angle) / d**2;
  // sat.velY += const * sin(angle) / d**2;

  for (int sateliteCount = 0; sateliteCount < fleetSatelites.length; sateliteCount++)
  {
    if (fleetSatelites[sateliteCount] != null)
    {
      for (int gravCheckCount = 0; gravCheckCount < solarSystem.length; gravCheckCount++)
      { 
        // checks collision detection for each planet in every iteration of draw()
        if (solarSystem[gravCheckCount] != null)
        {
          fleetSatelites[sateliteCount].gravityPush(solarSystem[gravCheckCount]);
        }
      } 
      // New version of collision detection:  made all objects essentially round
    }   
    // Collision detection is now completely vector based!
  }

  for (int sateliteUpdateCount = 0; sateliteUpdateCount < fleetSatelites.length; 
    sateliteUpdateCount++)
  { 
    // The update function checks to update only the objects that have not been eaten!
    if (fleetSatelites[sateliteUpdateCount] != null && 
      fleetSatelites[sateliteUpdateCount].showMe == true)
    {
      fleetSatelites[sateliteUpdateCount].update();
    }
  }

  bh1.update(); // There's our superstar!
  bh1.blackHoleEat(fleetSatelites, solarSystem, pretty, stars); // Watch him go!
  // Black Hole can now consume everything except the very coloring of the background!

    for (int count = 0; count < fleetSatelites.length; count++)
  {
    if (fleetSatelites[count] != null && fleetSatelites[count].showMe == false)
    {
      fleetSatelites[count] = null;
    }
  } // Better check to see that the satelite still exists before updating!

  for (int count = 0; count < solarSystem.length; count++)
  {
    if (solarSystem[count] != null && solarSystem[count].showMe == false)
    {
      solarSystem[count] = null;
    } // and check to see which planets are still there!
  }

  for (int count = 0; count < pretty.length; count++)
  {
    if (pretty[count] != null && pretty[count].showMe == false)
    {
      pretty[count] = null;
    } // background planets are edible too!  We only want to update the non-null planets
  }

  for (int count = 0; count < stars.length; count++)
  {
    if (stars[count] != null && stars[count].showMe == false)
    {
      stars[count] = null;
    } // this part for the stars is just like the rest
  }
}

