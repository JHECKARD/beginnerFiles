// Jason Heckard
// UCID 84851006
// ICS 62
// Week 4 Project

class BkgdPlanet extends SpaceObject
// notice that there's a new parent class in town: the SpaceObject!
// Inheritance for the win!
{
  int bkgdSize;

  BkgdPlanet(int spaceWidth, int spaceHeight, float bkgdDelay)
  {
    super( (int(random( spaceWidth) ) ), (int(random( spaceHeight) ) ), bkgdDelay ); 
    // top left corner location of the ellipse is randomly generated

    bkgdSize = int(random(10, 40) ); // random bkgdPlanetSize of background 

    spaceObjectRadius = bkgdSize / 2;
    spaceObjectWidth = spaceObjectHeight = bkgdSize;
    // planet, bkgdPlanetSize 10 to 40 

    objRed = int(random(255));
    objGreen = int(random(255));
    objBlue = int(random(255)); 
    // randomly generates the three RGB values of the planet

    areaWidth = spaceWidth;
    areaHeight = spaceHeight;
    // inputs size of space for the bkgd planets

    centerX = xLeft + bkgdSize / 2;
    centerY = yTop + bkgdSize / 2;
    // calculates the centerpoint of the original planet

    location = new PVector(centerX, centerY);
    velocity = new PVector(0, 0);
    acceleration = new PVector(0, 0);
    // background planets have motion vectors!

    showMe = true; // check it out!  each planet gets a boolean to see if it exists!
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
    // bkgd planets move when pulled toward the Black Hole!

    if (location.x > areaWidth) 
      // wraps the planet motion back around, giving an open-ended space feel
    {
      location.x = 0;
    }

    else if (location.x  + bkgdSize < 0)
    {
      location.x = areaWidth;
    }

    if (location.y > areaHeight) 
      // wraps the planet motion back around, giving an open-ended space feel!
    {
      location.y = 0;
    }

    else if (location.y < 0 - bkgdSize)
    {
      location.y = areaHeight;
    }
  }
}

