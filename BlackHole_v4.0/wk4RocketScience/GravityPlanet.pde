// Jason Heckard
// UCID 84851006
// ICS 62
// Week 4 Project

class GravityPlanet extends SpaceObject
// looky looky, more SpaceObjects!
{
  int gravSize;

  GravityPlanet(int xLoc, int yLoc, int planetSize, int spaceWidth, int spaceHeight, float gravDelay)
  {
    super(xLoc, yLoc, planetSize, planetSize, gravDelay);

    spaceObjectRadius = (planetSize / 2);
    spaceObjectWidth = spaceObjectHeight = gravSize = planetSize;

    objRed = int(random(255) );
    objGreen = int(random(255) );
    objBlue = int(random(255) ); // randomly determine the RGB color of each 
    // Gravity Planet

    centerX = xLeft + (planetSize / 2); 
    centerY = yTop + (planetSize / 2); 
    // centerX and centerY are calculated before the location vector

    // translate(xLoc, yLoc);
    location = new PVector(centerX, centerY); // location goes off of centerX and centerY!
    velocity = new PVector(0, 0);
    acceleration = new PVector(0, 0);
    // Gravity Planets can move!

    showMe = true; // there's that "have I been eaten yet?" value
  }

  void render()
  {
    stroke(220, 0, 0);
    strokeWeight(2); // sets the planetRed border for each Gravity Planet
    fill(objRed, objGreen, objBlue);
    ellipse(location.x, location.y, gravSize, gravSize); // holy cow!  planets can move now!
    strokeWeight(1);   // produces the ellipse for each Gravity Planet of 
    // randomly generated
    location.add(velocity);
    velocity.add(acceleration);
    velocity.limit(1.2);
    // println("   planet location x " + this.location.x + "  planet location y " + 
    //   this.location.y);
    // color and gravSize

    if (location.x > areaWidth) 
      // wraps the planet motion back around, giving an open-ended space feel
    {
      location.x = 0;
    }

    else if (location.x  + gravSize < 0)
    {
      location.x = areaWidth;
    }

    if (location.y > areaHeight) 
      // wraps the planet motion back around, giving an open-ended space feel!
    {
      location.y = 0;
    }

    else if (location.y < 0 - gravSize)
    {
      location.y = areaHeight;
    }
  }
}

