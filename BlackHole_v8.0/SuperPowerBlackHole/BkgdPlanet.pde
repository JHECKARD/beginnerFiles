// Jason Heckard
// UCID 84851006
// ICS 62
// Week 8 Project

class BkgdPlanet extends SpaceObject
// bkgd planets can be swallowed by the Black Hole but do not interact with the gravity system
{
  int bkgdSize;

  BkgdPlanet(int spaceWidth, int spaceHeight, float bkgdDelay)
  {
    super( (int(random( spaceWidth) ) ), (int(random( spaceHeight) ) ), bkgdDelay ); 
    // top left corner location of the ellipse is randomly generated

    bkgdSize = int(random(10, 30) ); 
    // random size of background planet

    spaceObjectRadius = bkgdSize / 2;
    spaceObjectWidth = spaceObjectHeight = bkgdSize;
    // planet, bkgdPlanetSize 10 to 40 

    objRed = int(random(20, 255));
    objGreen = int(random(20, 255));
    objBlue = int(random(20, 255)); 
    // randomly generates the three RGB values of the planet

    areaWidth = spaceWidth;
    areaHeight = spaceHeight;
    // inputs size of space for the bkgd planets

    centerX = xLeft + bkgdSize / 2;
    centerY = yTop + bkgdSize / 2;
    // calculates the centerpoint of the planet

    location = new PVector(centerX, centerY);
    // sets the location vector to the center point x and y of the planet

    velocity = new PVector(0, 0);
    acceleration = new PVector(0, 0);
    // background planets have motion vectors
    // these are used for being pulled toward the black hole

    showMe = true; 
    // each planet gets a boolean to see if it exists
  }

  void render()
  {
    stroke(objRed, objGreen, objBlue);
    fill(objRed, objGreen, objBlue); 
    // sets the planet and the outline to the randomly generated color

    ellipse(location.x, location.y, bkgdSize, bkgdSize); 
    // places the ellipse of random bkgdPlanetSize and location on the background

    location.add(velocity);
    velocity.add(acceleration);
    velocity.limit(0.8);
    // bkgd planets move when pulled toward the Black Hole

    if (location.x > areaWidth) 
      // wraps the planet motion back around the sides, giving an open-ended space feel
    {
      location.x = 0;
    }

    else if (location.x  + bkgdSize < 0)
    {
      location.x = areaWidth;
    }

    if (location.y > areaHeight) 
      // wraps the planet motion back around the top and bottom, giving an open-ended space feel
    {
      location.y = 0;
    }

    else if (location.y < 0 - bkgdSize)
    {
      location.y = areaHeight;
    }
  }
}

