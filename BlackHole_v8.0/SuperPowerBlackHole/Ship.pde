// Jason Heckard
// UCID 84851006
// ICS 62
// Week 8 Project

class Ship extends SpaceObject
{
  PImage shipSprite;
  PImage[]spaceShip;
  
  // loads the sprite sheet of space ships
  // loads the array of images that are each phase of the space ship

  int shipIndex;
  int shipSize;
  float rotation;
  // local variables of the space ship:  size, index in the array of sprites, and angle of rotation

  Ship(int shipLeft, int shipTop, int areaWide, int areaTall, float shipDelay)
  {
    super(shipLeft, shipTop, shipDelay);
    // super class constructor
    
    areaWidth = areaWide;
    areaHeight = areaTall;
    shipSize = spaceObjectWidth = spaceObjectHeight = int(random(30,41) );
    // set sizes not set by the constructor
    // the space ship sprite is scaled to a randomly generated size, 30-40 pixels height/width

    shipSprite =  loadImage("ship2c.png");
    spaceShip = new PImage[4];
    // set the values of the images

    for (int c = 0; c < spaceShip.length; c++)
    {
      spaceShip[c] = shipSprite.get(72 * c, 0, 71, 72);
    }
    // loads the images into the array.  each base space ship is 72 x 72

    location = new PVector(shipLeft, shipTop);
    velocity = new PVector( int(random (-3,3) ) , int(random (-3,3) ) );
    acceleration = new PVector(0, 0);
    // space ship vectors
    
    showMe = true;
    // boolean to show if the space ship should be rendered and updated 
  }

  void render()
  {
    rotation = velocity.heading2D();

    pushMatrix();
    translate(location.x, location.y);
    rotate(rotation + HALF_PI);
    // rotates the space ship in the direction of travel 

    imageMode(CENTER);
    // renders the space ship on the center of its location

    image(spaceShip[shipIndex], 0, 0, shipSize, shipSize);
    // show the image of the ship in the array to show animation

    if (frameCount % 10 == 0)
    {
      shipIndex++;
      if (shipIndex > 3)
      {
        shipIndex = 0;
      }
    }
    // use frame count rate to determine how fast to update the images of the space ship sprite
    
    popMatrix();
  }
  
  void update()
  {
    if ( location.x > areaWidth ) 
    {                                               
      location.x = 0;
    } 
    // right side of background respawn

    else if (location.x < 0 )
    {
      location.x = areaWidth;
    } 
    // sateliteLeft side of background respawn

    if (location.y > areaHeight )
    {
      location.y = 0;
    } 
    // bottom of background respawn

    else if (location.y < 0 )
    {
      location.y = areaHeight;
    } 
    // sateliteTop of background respawn

    location.add(velocity);
    velocity.add(acceleration); 
    velocity.limit(5);
    // updating location and speed all the time, with a speed limit of 5
  }
}

