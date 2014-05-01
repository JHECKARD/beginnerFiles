// Jason Heckard
// UCID 84851006
// ICS 62
// Week 8 Project


import ddf.minim.*;
// import the Minim player from Processing

PImage bkgd;
// creates the space for the background image

PImage titleScreen;
// space for the title screen

int numberSatelites = int(random(2, 7) );
Satelite [] fleetSatelites = new Satelite[numberSatelites];
// creates an array of satelites

int numberShips = int(random(2, 7) );
Ship [] fleetShips = new Ship[numberShips];
// an array of sprite ships

int numStars = int(random(100, 201) );
Star[] stars = new Star[numStars]; 
// creates an array of stars  

int planetCount = int(random(6, 19) ); 
BkgdPlanet[] pretty = new BkgdPlanet[planetCount]; 
// creates an array of background planets

int solidCount = int(random(2, 9) );
GravityPlanet[] solarSystem = new GravityPlanet[solidCount];  
// creates an array of gravity planets

BlackHole bh1 = new BlackHole( int( random(20, 36) ) ); 
// the Black Hole!  

Minim minimPlayer;

AudioSample unleash;
AudioSample consume;
AudioPlayer victory;

// featuring 3 different sounds
// a sound that triggers whenever the true nature of the black hole is revealed
// a sound for when the black hole consumes a lesser being
// victory music for consuming the space objects of the galaxy!

int spaceWidth, spaceHeight;
// stores the size of the game space

int gameState = 0;
// a value used to store game state, for loading specific images and properties
// state 0 is title screen and Enter
// state 1 is playing the game

// possible future development:  state 2 for victory screen
// state 3 for game over screen (when available)

boolean showStart;
// a boolean to enable and disable when the start instructions are shown
// used to make the start instructions flash ... classic arcade style!

void setup()
{
  // for use with Android devices
  // spaceWidth = 480;
  // spaceHeight = 800;
  // set to the size of the background image, set for exporting to Android
  
  // for use with standard screen 
  spaceWidth = 880;
  spaceHeight = 640;

  size(spaceWidth, spaceHeight); 
  smooth();
  ellipseMode(CORNER);

  showStart = false;

  if (gameState == 0)
  {
    titleScreen = loadImage("titleScreen.png");
  }
  // gameState 0 will dump resources used for titleScreen once the gameState changes

  if (gameState == 1)
  {
    // gameState 1 -> playing the game

    bkgd = loadImage("backgroundGalaxy1Android.png" );
    // loads the deep space background image

      for (int starCount = 0; starCount < stars.length; starCount++)
    {
      stars[starCount] = new Star(int(random(spaceWidth)), int(random(spaceHeight) ), 0.00005 );
    } 
    // fills the array of stars in random locations across the background
    // Stars have the slowest response to Black Hole's force pull

    for (int bkgdCount = 0; bkgdCount < pretty.length; bkgdCount++)
    {
      pretty[bkgdCount] = new BkgdPlanet (spaceWidth, spaceHeight, 0.00008);
    } 
    // fills the array of background planets across the background
    // background planets respond to the Black Hole, once all gravity planets have been consumed

    for (int satCount = 0; satCount < fleetSatelites.length; satCount++)
    {
      fleetSatelites[satCount] = new Satelite ( int(random(spaceWidth) ), int(random(spaceHeight) ), 
      int (random(15, 35) ), int (random(15, 35) ), int (random(10, 20) ), spaceWidth, spaceHeight, 0.001);
    }
    // creates the random group of Satelites 
    // satelites respond to the black hole pull more than the other space objects

    for (int shipCount = 0; shipCount < fleetShips.length; shipCount++)
    {
      fleetShips[shipCount] = new Ship ( int(random(spaceWidth) ), int(random(spaceHeight) ), spaceWidth, 
      spaceHeight, 0.002);
    }
    // creates the group of spaceShips
    // space ships can also be eaten by the Black Hole

    for (int gravCount = 0; gravCount < solarSystem.length; gravCount++)
    {
      solarSystem[gravCount] = new GravityPlanet( int(random(spaceWidth) ), 
      int(random(spaceHeight) ), int(random(25, 45) ), spaceWidth, spaceHeight, 0.00003);
    } 
    // fills the array of Gravity Planets across the background

    minimPlayer = new Minim(this);

    unleash = minimPlayer.loadSample( "punch_or_whack_Vladimir.mp3", 512);
    if ( unleash == null ) 
    {
      println("The unleash sound did not execute!");
    }
    // loads the sound for unleashing the mighty power of the Black Hole
    // warns the user if the sound fails to load

    consume = minimPlayer.loadSample( "Jump-SoundBible_com-snottyboy.mp3", 512);
    if ( consume == null ) 
    {
      println("Consume sound failed to load!");
    }
    // loads the sound for space objects being swallowed up
    // warns the user that the gravity push sound did not load

    victory = minimPlayer.loadFile( "Griphop.mp3", 1024);
    if ( victory == null ) 
    {
      println("The victory song track is missing!");
    }
    // loads the sound of victory!
    // warns the user that the music did not load
  }
}

void draw()
{

  if (gameState ==0)
  {
    // gameState 0 is the title screen
    image(titleScreen, 0, 0, spaceWidth, spaceHeight);

    if (frameCount %40 == 0 /* && frameCount %19 != 0 */)
    {
      showStart = true;
      // flash the Press to Start button ... classic arcade style!
    }

    if (frameCount %80 == 0)
    {
      showStart = false;
      // disables the instructions
      // uses different fractions of frameCount to determine when to show and disable the push start
    }

    pushStart();
    // shows the instructions!
  }

  if (gameState == 1)
  {
    // playing the game since gameState == 1 

      imageMode(CORNER);
    image (bkgd, 0, 0, spaceWidth, spaceHeight);
    // sets the image that is loaded into background point 0,0

    for (int starRenderCount = 0; starRenderCount < stars.length; starRenderCount++)
    {
      if (stars[starRenderCount] != null)
      {
        stars[starRenderCount].render();
      }
    } 
    // places the non-consumed stars in the background on top of the deep space image

    for (int bkgdRenderCount = 0; bkgdRenderCount < pretty.length; bkgdRenderCount++)
    {
      if (pretty[bkgdRenderCount] != null)
      {
        pretty[bkgdRenderCount].render();
      }
    } 
    // places each background planet in the background, if it still exists, layered on top of the stars

    for (int sateliteCount = 0; sateliteCount < fleetSatelites.length; sateliteCount++)
    {
      if (fleetSatelites[sateliteCount] != null)
      {
        fleetSatelites[sateliteCount].render();
      }
    } 
    // places the satelites that have not been destroyed by blackHole

    for (int shipCount = 0; shipCount < fleetShips.length; shipCount++)
    {
      if (fleetShips[shipCount] != null)
      {
        fleetShips[shipCount].render();
      }
    }
    // places the ships that have not been destroyed by blackHole

    for (int gravRenderCount = 0; gravRenderCount < solarSystem.length; gravRenderCount++)
    {
      if (solarSystem[gravRenderCount] != null)
      {
        solarSystem[gravRenderCount].render();
      }
    } 
    // renders the red-bordered Gravity Planets in the background until they are eaten by the black hole

    noCursor();
    // even the mouse arrow cannot be saved from the appetite of the mighty Black Hole!

    bh1.render();

    for (int sateliteCount = 0; sateliteCount < fleetSatelites.length; sateliteCount++)
    {
      if (fleetSatelites[sateliteCount] != null)
      {
        for (int gravCheckCount = 0; gravCheckCount < solarSystem.length; gravCheckCount++)
        { 
          // each satelite checks for collision with each planet in the array of gravity planets

          if (solarSystem[gravCheckCount] != null)
          {
            fleetSatelites[sateliteCount].gravityPush(solarSystem[gravCheckCount]);
            // calls the gravity push on each gravity planet, for each satelite
          }
        }
      }
    }

    for (int shipCount = 0; shipCount < fleetShips.length; shipCount++)
    {
      if (fleetShips[shipCount] != null)
      {
        for (int gravCheckCount = 0; gravCheckCount < solarSystem.length; gravCheckCount++)
        {
          if (solarSystem[gravCheckCount] != null)
          {
            fleetShips[shipCount].gravityPush(solarSystem[gravCheckCount]);
            // calls the gravity push on each gravity planet, for each ship
          }
        }
      }
    }


    for (int sateliteUpdateCount = 0; sateliteUpdateCount < fleetSatelites.length; sateliteUpdateCount++)
    { 
      // The update function checks to update only the objects that have not been eaten!
      if (fleetSatelites[sateliteUpdateCount] != null && fleetSatelites[sateliteUpdateCount].showMe == true)
      {
        fleetSatelites[sateliteUpdateCount].update();
      }
    }

    for (int shipUpdateCount = 0; shipUpdateCount < fleetShips.length; shipUpdateCount++)
    {
      if (fleetShips[shipUpdateCount] != null && fleetShips[shipUpdateCount].showMe == true)
      {
        fleetShips[shipUpdateCount].update();
      }
    }
    // only the ships that still exist are the ships that get updated

    bh1.update(); 
    // There's our superstar!

    bh1.blackHoleEat(fleetSatelites, fleetShips, solarSystem, pretty, stars); 
    // Watch it go!

    for (int count = 0; count < fleetSatelites.length; count++)
    {
      if (fleetSatelites[count] != null && fleetSatelites[count].showMe == false)
      {
        fleetSatelites[count] = null;
      }
    } 
    // check to see that each satelite still exists before updating

    for (int count = 0; count < fleetShips.length; count++)
    {
      if (fleetShips[count] != null && fleetShips[count].showMe == false)
      {
        fleetShips[count] = null;
      }
    }

    for (int count = 0; count < solarSystem.length; count++)
    {
      if (solarSystem[count] != null && solarSystem[count].showMe == false)
      {
        solarSystem[count] = null;
      }
    } 
    // and check to see which planets are still there before updating

    for (int count = 0; count < pretty.length; count++)
    {
      if (pretty[count] != null && pretty[count].showMe == false)
      {
        pretty[count] = null;
      }
    } 
    // only update the non-null planets

    for (int count = 0; count < stars.length; count++)
    {
      if (stars[count] != null && stars[count].showMe == false)
      {
        stars[count] = null;
      }
    } 
    // this part for updating the stars is just like the rest
  }
}

void mousePressed()
{
  if (gameState == 0)
  {
    gameState = 1;
    setup();
  }

  if (gameState == 1)
  {
    // mousePressed only responds if the game is in running
    unleash.trigger();
  }
}
// when the black hole power is activated, the sound of its presence is unleashed

void pushStart()
{
  // this is the line of credits that blink on and off at start screen
  if (showStart == true)
  {
    textSize(40);
    fill(255, 255, 255);
    pushMatrix();
    
    // rotates the screen for running on Android devices
    // rotate(HALF_PI);
    // text("Push Enter to take control ", 150, -200);
    // text("of the Super Power Black Hole", 150, -100);
    
    // for standard computer screen orientation
    text("Push Enter to take control ", 10, -10);
    // text("of the Super Power Black Hole", 10, 20); 

    popMatrix();
  }
}

//void keyPressed()
//{
//  // defines the function of pressing Enter to start the game
//  if (key == ENTER)
//  {
//    if (gameState == 0)
//    {
//      gameState = 1;
//      setup();
//    }
//  }
//}


void stop()
{
  //  required function for closing minim
  unleash.close();
  consume.close();
  victory.close();

  minimPlayer.stop();
  super.stop();
}

