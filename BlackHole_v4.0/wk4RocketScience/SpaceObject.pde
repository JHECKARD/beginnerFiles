// Jason Heckard
// UCID 84851006
// ICS 62
// Week 4 Project

class SpaceObject // Here is the ultimate parent class for space objects!
{
  int xLeft;
  int xRight;
  int yTop;
  int yBottom;
  float centerX, centerY;
  int spaceObjectRadius;
  int spaceObjectWidth, spaceObjectHeight;
  int areaWidth, areaHeight;
  int objRed, objGreen, objBlue;
  float pullDelay;  
  
  float angle; // determines the angle of rotation of the object, Nature of Code ch 3.3

  PVector location;
  PVector velocity;
  PVector acceleration;

  boolean showMe;
  
  int score;

  SpaceObject(int x, int y, float thisDelay) // a less specific SpaceObject constructor
  {
    xLeft = x;
    yTop = y;
    pullDelay = thisDelay;
    location = new PVector(xLeft, yTop);
  }

  SpaceObject(int x, int y, int objectWidth, int objectHeight, float moveDelay)
  {  
    xLeft = x;
    yTop = y;
    pullDelay = moveDelay;
    spaceObjectWidth = objectWidth;
    spaceObjectHeight = objectHeight;

    if (spaceObjectWidth >= spaceObjectHeight)
    {
      spaceObjectRadius = (spaceObjectWidth / 2);
    }
    else
    {
      spaceObjectRadius = (spaceObjectHeight / 2);
    }

    areaWidth = spaceWidth;
    areaHeight = spaceHeight;

    centerX = x + (spaceObjectWidth / 2);
    centerY = y + (spaceObjectHeight / 2);

    location = new PVector(centerX, centerY);
  }

  public void gravityPush(SpaceObject b) // rewrote collision detection ... with vectors!
  {
    if (dist (this.centerX, this.centerY, b.centerX, b.centerY) < 
      6* b.spaceObjectRadius)
    { // checks distance between centerpoints of this spaceObject and the 
      // target spaceObject
      // treats all spaceObjects as round for collision detection
      this.acceleration.set(0, 0, 0);

      //  Here are my vector-based collision checks that use negative accelerations!
      if ( (this.centerX < b.centerX) && (this.velocity.x > -5) )
      { // accelerate to the left if this spaceObject is to the left of target 
        // and moving to the right
        // while within gravity push range, which is 6*radius of the target
        this.acceleration.add( -0.2, 0, 0 );
      }

      else if ( (this.centerX > b.centerX) && (this.velocity.x < 5) )
      { // accelerate to the right if this spaceObjct is to the right of the target 
        // and moving to the left
        // while within gravity push range
        this.acceleration.add( 0.2, 0, 0 );
      }

      if ( (this.centerY < b.centerY) && (this.velocity.y > -5) )
      { // accelerate to the down if this spaceObject is above the target and 
        // moving down
        // while within range
        this.acceleration.add( 0, -0.2, 0 );
      }

      else if ( (this.centerY > b.centerY) && (this.velocity.y < 5) )
      { // accelerate to the down if this spaceObject is below the target and 
        // moving up
        // while within range
        this.acceleration.add( 0, 0.2, 0 );
      }

      this.velocity.add(acceleration);
      this.location.add(velocity);
    }
  }


}

