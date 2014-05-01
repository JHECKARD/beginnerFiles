// Jason Heckard
// UCID 84851006
// ICS 62
// Week 8 Project

class Star extends SpaceObject
// just a cute little star in a big wide world of SpaceObjects

{
  int starRed, starGreen, starBlue;

  Star(int x, int y, float starDelay)
  {
    // they have color, location, and motion vectors like other space objects
    super(x, y, starDelay);
    starRed   = 255;
    starGreen = 255;
    starBlue  = 0;
    showMe = true;

    velocity = new PVector(0, 0);
    acceleration = new PVector(0, 0);
  }

  void render()
  {
    stroke(starRed, starGreen, starBlue);
    fill(starRed, starGreen, starBlue);

    location.add(velocity);
    velocity.add(acceleration);
    velocity.limit(0.4);
    // they're smaller and slower than the other space objects

    ellipse(location.x, location.y, 2, 2); 
    // places a white pixel point at the designated coordinate
  }
}

