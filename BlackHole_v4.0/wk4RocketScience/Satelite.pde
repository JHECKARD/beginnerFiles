// Jason Heckard
// UCID 84851006
// ICS 62
// Week 4 Project

class Satelite extends SpaceObject
// calling master SpaceObject everywhere!

// Chapter 3 of Nature of Code :  Pointing in the Direction of Motion!!
// learned how to have satelites point in the direction of motion from the book
{
  int bodyWidth, bodyHeight, finWidth;

  Satelite(int sateliteLeft, int sateliteTop, int wide, int tall, int finSize, 
  int spaceWidth, int spaceHeight, float sateDelay)
  {
    super(sateliteLeft, sateliteTop, wide, tall, sateDelay); 
    xLeft = sateliteLeft;
    yTop = sateliteTop;
    spaceObjectWidth = wide;
    spaceObjectHeight = tall;

    areaWidth = spaceWidth;
    areaHeight = spaceHeight;

    finWidth = finSize;
    bodyWidth = wide;
    bodyHeight = tall;

    showMe = true; // there's the new "am I still alive?" value!

    spaceObjectWidth = bodyWidth + 2* finWidth; 
    // saves total areaWidth of the satelite for later use

    location = new PVector(xLeft, yTop); 
    // sets the initial values of the location vector
    
    velocity = new PVector( (random(-3, 3) ), (random(-3, 3) ) );
    acceleration = new PVector(0, 0, 0);
    // sets the random initial value of the trajectory of the Satelite

    centerX = location.x + (spaceObjectWidth / 2); // getting CenterX from location this time!
    centerY = location.y + (spaceObjectHeight / 2);
  }

  void render()
  {
    stroke(255, 255, 255);
    
    // LEARNED POINTING IN DIRECTION OF MOTION FROM NATURE OF CODE CH 3.4
    // A LOT OF THIS CODE IS DIRECTLY COPIED BUT CUSTOMIZED TO FIT THE NEEDS OF THE SATELITES
    // NO sPACEoBJECTS WERE HARMED DURING THE ROTATION OF THESE OBJECTS
    
    float rotation = velocity.heading2D();
    
//    angle = atan2(velocity.y, velocity.x);
    pushMatrix();
    translate(centerX, centerY);
    rotate(rotation + HALF_PI);

    fill (200, 0, 0);
    triangle(2* finWidth / 3, (11 * bodyHeight / 10), finWidth + bodyWidth / 5, bodyHeight / 2, 
    finWidth + bodyWidth / 5,(11 * bodyHeight / 10 ) ); 
    // red triangle sateliteLeft rocket

    triangle( (finWidth + bodyWidth + ( finWidth / 3) ), (11 * bodyHeight / 10),finWidth + 
    (4 * bodyWidth / 5), bodyHeight / 2, finWidth + (4* bodyWidth / 5), (11* bodyHeight / 10) );  
    // red triangle right rocket

    fill (100, 100, 100); 
    rect(0,0, finWidth, bodyHeight);  

    line(finWidth / 2, 0, finWidth / 2, bodyHeight);
    line(0, bodyHeight / 3, finWidth, bodyHeight / 3);
    line(0, 2* bodyHeight / 3, finWidth, 2* bodyHeight / 3);
    // creates the sateliteLeft solor panel

    ellipse(finWidth, 0, bodyWidth, bodyHeight); 
    // circular body in the middle

    rect (finWidth + bodyWidth, 0, finWidth, bodyHeight); 

    line(finWidth + bodyWidth + finWidth / 2, 0, finWidth + bodyWidth + finWidth / 2, bodyHeight);
    line(finWidth + bodyWidth, bodyHeight / 3, 2* finWidth + bodyWidth, bodyHeight / 3);
    line(finWidth + bodyWidth, 2* bodyHeight / 3, 2* finWidth + bodyWidth, 2* bodyHeight / 3);
    // right solar panel

    fill (220, 100, 0);
    rect(finWidth + bodyWidth / 5, bodyHeight / 7, bodyHeight / 3, bodyWidth / 5);
    // orange rectangular control panel
    
    popMatrix();
  }

  void update()
  {
    if ( location.x > areaWidth + spaceObjectWidth) 
    // got rid of the pong ball rebound.
    {                                               
      // made outer space feel open ended!
      location.x = 0;
    } // right side of background respawn

    else if (location.x < 0 - spaceObjectWidth)
    {
      location.x = areaWidth;
    } // sateliteLeft side of background respawn

    if (location.y > areaHeight + spaceObjectHeight)
    {
      location.y = 0;
    } // bottom of background respawn

    else if (location.y < 0 - spaceObjectHeight)
    {
      location.y = areaHeight;
    } // sateliteTop of background respawn

    location.add(velocity);
    velocity.add(acceleration); // updating location and speed all the time!
    velocity.limit(5);
    
    centerX = location.x + (spaceObjectWidth / 2);
    centerY = location.y + (spaceObjectHeight / 2);
    
  }
}

