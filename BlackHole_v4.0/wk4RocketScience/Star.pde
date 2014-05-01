// Jason Heckard
// UCID 84851006
// ICS 62
// Week 4 Project

class Star extends SpaceObject
// just a cute little star in a big wide world of SpaceObjects

{
  int starColor;

  Star(int x, int y, float starDelay)
  {
    super(x, y, starDelay);
    starColor = 255;
    showMe = true;

    location = new PVector(x, y);
    velocity = new PVector(0, 0);
    acceleration = new PVector(0, 0);
    // Stars can move too!
  }

  void render()
  {
    stroke(starColor, starColor, starColor);

    location.add(velocity);
    velocity.add(acceleration);
    velocity.limit(0.4);
    // they're smaller and slower than the other space objects

    point(location.x, location.y); 
    // places a white pixel point at the designated coordinate
  }
}

