// Jason Heckard
// UCID 84851006
// ICS 62
// Week 8 Project

class BlackHole extends SpaceObject 
// Superstar Black Hole!
{
  int blackHoleSize;
  int angleCount;
  // values that can change and are relevant to Black Hole's ultimacy!

  boolean spaceVictory = false;

  BlackHole(int inputSize)
  {
    super( mouseX - inputSize / 2, mouseY - inputSize / 2, 0 );

    blackHoleSize = inputSize;
    spaceObjectRadius = blackHoleSize / 2;
    location = new PVector(mouseX - spaceObjectRadius, mouseY - spaceObjectRadius);
    // Black Hole follows the mouse

    angleCount = 0;
    // used for tracking rotation of the powerful rings of the Black Hole

    score = 0;
    // used to give the player a guage of the total worth of the solar system they consumed
  } 

  void render() 
    // at first glance, Black Hole is just a harmless dark spot...
  {
    stroke(0);
    fill(0, 0, 0);
    centerX = mouseX;
    centerY = mouseY;
    ellipse(centerX - spaceObjectRadius, centerY -spaceObjectRadius, blackHoleSize, blackHoleSize);
    // Black Hole's size is based on a variable that can change as it eats and eats
  }

  void update()
  {
    spaceObjectRadius = blackHoleSize / 2;
    xLeft = int (centerX - (spaceObjectRadius) );
    yTop = int (centerY - (spaceObjectRadius) );

    if (mousePressed)
    { 
      // if MousePressed is True, then its true beautiful hunger is revealed
      // when this happens, Black Hole physically pulls the rest of the world to it

      pushMatrix();
      translate(centerX, centerY); 
      // translates the center of the arcs to the center of the black hole

      angleCount++;
      angleCount %= 360;
      rotate(radians(angleCount) );
      // rotates the arcs of power as the button is held!  Makes Black Hole even more amazing!

      stroke(0);
      fill(0, 0, 0);
      ellipse(0 -(blackHoleSize / 2), 0 -(blackHoleSize / 2), blackHoleSize, blackHoleSize);
      // as Black Hole eats, it gets bigger

      strokeWeight(blackHoleSize / 7); 
      // the arcs become more prominent as Black Hole gets bigger

      stroke(0, 225, 255);
      arc(0 -(blackHoleSize / 4), 0 -(blackHoleSize *3 /4), blackHoleSize / 2, 
      blackHoleSize * 1.5, (QUARTER_PI ), (PI + HALF_PI + QUARTER_PI) );

      stroke(255, 125, 0);
      arc(0 -(blackHoleSize * 3/4 ), 0 -(blackHoleSize / 4), blackHoleSize * 1.5, 
      blackHoleSize / 2, (0 - (QUARTER_PI) ), (PI + QUARTER_PI) );
      strokeWeight(1);
      // create the arcs, then reset stroke weight

      popMatrix();
    }

    if (spaceVictory == true)
    {
      // functions that shows the endgame script once the entire solar system is eaten
      victory();
    }
  }

  public void blackHoleEat(Satelite[] satelites, Ship [] ships, GravityPlanet[] gravPlanets, 
  BkgdPlanet [] bkgdPlanets, Star [] stars)
  {
    // This is the method that BlackHole uses to eat all the tasty Space Objects!
    int numberSatelites = 0;
    int numberShips = 0;
    int numberGravPlanets = 0;
    int numberBkgdPlanets = 0;
    int numberStars = 0;

    if (mousePressed)
    {
      for (int sateliteCount = 0; sateliteCount < satelites.length; sateliteCount++)
      {
        // consume the satelites first!
        if (satelites[sateliteCount] != null)
        {
          numberSatelites++;
          satelites[sateliteCount].acceleration.set(0, 0, 0);
          satelites[sateliteCount].acceleration.add ( ( (mouseX - satelites[sateliteCount].location.x) 
            * satelites[sateliteCount].pullDelay), 0, 0 );
          satelites[sateliteCount].acceleration.add (0, ( (mouseY - satelites[sateliteCount].location.y)  
            * satelites[sateliteCount].pullDelay), 0 );
          // accelerates the satelite in x and y toward the Black Hole

          if ( dist(satelites[sateliteCount].location.x + satelites[sateliteCount].spaceObjectWidth /2, 
          satelites[sateliteCount].location.y + satelites[sateliteCount].spaceObjectHeight /2, mouseX, 
          mouseY ) < 2.5* this.spaceObjectRadius)
          {
            satelites[sateliteCount].showMe = false;
            numberSatelites--;
            this.blackHoleSize += (satelites[sateliteCount].spaceObjectRadius) / 10;
            score += (satelites[sateliteCount].spaceObjectRadius) / 10;
            // Black Hole gets bigger for consuming each Satelite!

            consume.trigger();
            // plays the sound of consuming a target when Black Hole eats a satelite
          }
        }
      }

      for (int i = 0; i < ships.length; i++)
      {
        // ships and satelites get consumed together!
        if (ships[i] != null)
        {
          numberShips++;
          ships[i].acceleration.add ( ( (mouseX - ships[i].location.x) * ships[i].pullDelay), 0, 0); 
          ships[i].acceleration.add  (0, ( (mouseY - ships[i].location.y) * ships[i].pullDelay), 0 );
          // Black Hole can suck the ships into its tasty emptiness!

          if (dist(ships[i].location.x, ships[i].location.y, mouseX, mouseY ) < 2 * this.spaceObjectRadius)
          {
            ships[i].showMe = false;
            numberShips--;
            this.blackHoleSize += ships[i].shipSize /5;
            score += ships[i].shipSize /5;
            // Black Hole gets bigger for consuming each Ship!

            consume.trigger();
            // plays the sound of consuming a target when Black Hole eats a ship
          }
        }
      }

      if (numberShips == 0 && numberSatelites == 0)
      {
        for (int gravCount = 0; gravCount < gravPlanets.length; gravCount++)
        {
          // once the Satelites are gone, consume the gravity planets!
          if (gravPlanets[gravCount] != null)
          {
            numberGravPlanets++;
            gravPlanets[gravCount].acceleration.add ( ( (mouseX - gravPlanets[gravCount].location.x) 
              * gravPlanets[gravCount].pullDelay), 0, 0 );
            gravPlanets[gravCount].acceleration.add (0, ( (mouseY - gravPlanets[gravCount].location.y)  
              * gravPlanets[gravCount].pullDelay), 0 );
            // accelerates the planets toward the Black Hole

            if ( dist(gravPlanets[gravCount].location.x, gravPlanets[gravCount].location.y, mouseX, 
            mouseY ) < 2* gravPlanets[gravCount].spaceObjectRadius)
            {
              gravPlanets[gravCount].showMe = false;
              numberGravPlanets--;
              this.blackHoleSize += (gravPlanets[gravCount].spaceObjectRadius) / 10;
              score += (gravPlanets[gravCount].spaceObjectRadius) / 10;
              // Black Hole gets even bigger for consuming each gravity planet!

              consume.trigger();
              // when Black Hole eats a planet, trigger the sound
            }
          }
        }
      }

      if (numberGravPlanets == 0 && numberShips == 0 && numberSatelites == 0)
      {
        for (int bkgdCount = 0; bkgdCount < bkgdPlanets.length; bkgdCount++)
        {
          // background planets get attracted next!
          if (bkgdPlanets[bkgdCount] != null)
          {
            numberBkgdPlanets++;
            bkgdPlanets[bkgdCount].acceleration.add ( ( (mouseX - bkgdPlanets[bkgdCount].location.x) 
              * bkgdPlanets[bkgdCount].pullDelay), 0, 0 );
            bkgdPlanets[bkgdCount].acceleration.add (0, ( (mouseY - bkgdPlanets[bkgdCount].location.y)  
              * bkgdPlanets[bkgdCount].pullDelay), 0 );
            // background planets can be accelerated toward the Black Hole as well

            if ( dist(bkgdPlanets[bkgdCount].location.x, bkgdPlanets[bkgdCount].location.y, mouseX, 
            mouseY ) < 3* bkgdPlanets[bkgdCount].spaceObjectRadius)
            {
              bkgdPlanets[bkgdCount].showMe = false;
              numberBkgdPlanets--;
              this.blackHoleSize += (bkgdPlanets[bkgdCount].spaceObjectRadius) / 10;
              score += (bkgdPlanets[bkgdCount].spaceObjectRadius) / 10;
              // Black Hole continues to grow, and so does the user's score!

              consume.trigger();
              // play the consume sound when Black Hole consumes
            }
          }
        }
      }

      if (numberBkgdPlanets == 0 && numberGravPlanets == 0 && numberShips == 0 && numberSatelites == 0)
      {
        for (int starCount = 0; starCount < stars.length; starCount++)
        {
          // stars get eaten last!
          if (stars[starCount] != null)
          {
            numberStars++;

            stars[starCount].acceleration.add ( ( (mouseX - stars[starCount].location.x) 
              * stars[starCount].pullDelay), 0, 0 );
            stars[starCount].acceleration.add (0, ( (mouseY - stars[starCount].location.y)  
              * stars[starCount].pullDelay), 0 );
            // stars accelerate toward the Black Hole last

            if ( dist(stars[starCount].location.x, stars[starCount].location.y, mouseX, mouseY ) 
              < this.spaceObjectRadius)
            {
              stars[starCount].showMe = false;
              numberStars--;
              this.blackHoleSize += 1;
              score += 1;
              // Watch Black Hole eat the stars in the sky, and score big for the user!

              consume.trigger();
              // play the consume sound for swallowing the stars in the sky
            }
          }
        }
      }
      if (numberShips == 0 && numberBkgdPlanets == 0 && numberGravPlanets == 0 && numberSatelites ==0 
        && numberStars == 0)
      {
        spaceVictory = true;
      }
    } 
    // Satelites respond by attempting to get close to the Black Hole for as long as the mouse 
    // button is held down.  If the user moves the Black Hole while continuing to hold 
    // the button down, the satelites will attempt to follow.  The same holds true for the gravity 
    // planets, then the background planets, then the stars!

    if (! mousePressed)
    {
      // When Black Hole's power is hidden, the galaxy is not pulled toward it!
      // defining the non addition to each acceleration is required to keep 
      // the solar system stable when the Black Hole is hiding

      for (int gravCount = 0; gravCount < gravPlanets.length; gravCount++)
      {
        if (gravPlanets[gravCount] != null)
        {
          gravPlanets[gravCount].velocity.set(0, 0, 0);
          gravPlanets[gravCount].acceleration.set(0, 0, 0);
        }
      }

      for (int bkgdCount = 0; bkgdCount < bkgdPlanets.length; bkgdCount++)
      {
        if (bkgdPlanets[bkgdCount] != null)
        {
          bkgdPlanets[bkgdCount].velocity.set(0, 0, 0);
          bkgdPlanets[bkgdCount].acceleration.set(0, 0, 0);
        }
      }

      for (int starCount = 0; starCount < stars.length; starCount++)
      {
        if (stars[starCount] != null)
        {
          stars[starCount].velocity.set(0, 0, 0);
          stars[starCount].acceleration.set(0, 0, 0);
        }
      }
    }
  }

  void victory()
  {
    textSize(30);
    fill(40, 150, 40);
    pushMatrix();
    rotate(HALF_PI);
    text("Black Hole has consumed the galaxy!", 25, -350);
    text("This solar system was worth " + score + " points!", 25, -150);
    // Game Over!  The Black Hole has conusmed the galaxy!
    // The player gets to see how many points their randomly generated galaxy was worth!

    victory.play();

    popMatrix();
    // play the music for victory against the star system!
  }
}

