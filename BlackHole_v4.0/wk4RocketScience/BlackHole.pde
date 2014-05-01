// Jason Heckard
// UCID 84851006
// ICS 62
// Week 4 Project

class BlackHole extends SpaceObject // Superstar of the week:  Black Hole!
{
  int blackHoleSize;
  int angleCount;
  // values that can change and are relevant to Black Hole's ultimacy!

  BlackHole(int inputSize)
  {
    super( mouseX - inputSize / 2, mouseY - inputSize / 2, 0 );
    // superClass consturctor!
    
    blackHoleSize = inputSize;
    spaceObjectRadius = blackHoleSize / 2;
    location = new PVector(mouseX - spaceObjectRadius, mouseY - spaceObjectRadius);

    angleCount = 0;
    // used for tracking rotation of the powerful rings of the Black Hole!
    
    score = 0;
    // used to give the player a guage of the total worth of the galaxy they consumed!

  } // Black Hole follows the mouse wherever you go!

  void render() // at first glance, Black Hole is just a harmless dark spot...
  {
    stroke(0);
    fill(0, 0, 0);
    centerX = mouseX;
    centerY = mouseY;
    ellipse(centerX - spaceObjectRadius, centerY -spaceObjectRadius, blackHoleSize, blackHoleSize);
    // black hole's size is now based on a variable that can change!
  }

  void update()
  {
    spaceObjectRadius = blackHoleSize / 2;
    xLeft = int (centerX - (spaceObjectRadius) );
    yTop = int (centerY - (spaceObjectRadius) );

    if (mousePressed)
    { // but if MousePressed is True, then its true beautiful hunger is revealed!
      // when this happens Black Hole physically pulls the rest of the world to it!

      pushMatrix();
      translate(centerX, centerY);
      angleCount++;
      angleCount %= 360;
      rotate(radians(angleCount) );
      println("angle of rotation " + angleCount);
      // rotates the arcs of power as the button is held!  Makes Black Hole even more amazing!

      stroke(0);
      fill(0, 0, 0);
      ellipse(0 -(blackHoleSize / 2), 0 -(blackHoleSize / 2), blackHoleSize, blackHoleSize);
      // allows mousePressed black hole value to change

      strokeWeight(blackHoleSize / 7); // the arcs become more prominent as Black Hole gets bigger
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
  }

  public void blackHoleEat(Satelite[] satelites, GravityPlanet[] gravPlanets, 
  BkgdPlanet [] bkgdPlanets, Star [] stars)
  { // This is the no longer inherited method that BlackHole uses to eat all the tasty Space Objects!
    int numberSatelites = 0;
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
          satelites[sateliteCount].acceleration.add ( ( (mouseX - 
            satelites[sateliteCount].location.x) 
            * satelites[sateliteCount].pullDelay), 0, 0 );
          satelites[sateliteCount].acceleration.add (0, ( (mouseY - 
            satelites[sateliteCount].location.y)  
            * satelites[sateliteCount].pullDelay), 0 );

          if ( dist(satelites[sateliteCount].centerX, satelites[sateliteCount].centerY, 
          mouseX, mouseY ) < 2.5* this.spaceObjectRadius)
          {
            satelites[sateliteCount].showMe = false;
            numberSatelites--;
            this.blackHoleSize += (satelites[sateliteCount].spaceObjectRadius) / 10;
            score += (satelites[sateliteCount].spaceObjectRadius) / 10;
            // Black Hole gets bigger and the player gets points for consuming each Satelite!
          }
        }
      }

      if (numberSatelites == 0)
      {
        for (int gravCount = 0; gravCount < gravPlanets.length; gravCount++)
        {
          // once the Satelites are gone, consume the gravity planets!
          if (gravPlanets[gravCount] != null)
          {
            numberGravPlanets++;
            gravPlanets[gravCount].acceleration.add ( ( (mouseX - 
              gravPlanets[gravCount].location.x) 
              * gravPlanets[gravCount].pullDelay), 0, 0 );
            gravPlanets[gravCount].acceleration.add (0, ( (mouseY - 
              gravPlanets[gravCount].location.y)  
              * gravPlanets[gravCount].pullDelay), 0 );

            if ( dist(gravPlanets[gravCount].location.x, gravPlanets[gravCount].location.y, mouseX, 
            mouseY ) < 2* gravPlanets[gravCount].spaceObjectRadius)
            {
              gravPlanets[gravCount].showMe = false;
              numberGravPlanets--;
              this.blackHoleSize += (gravPlanets[gravCount].spaceObjectRadius) / 10;
              score += (gravPlanets[gravCount].spaceObjectRadius) / 10;
              // Black Hole gets even bigger and the player gets even points for consuming each gravity planet!
            }
          }
        }
      }

      if (numberGravPlanets == 0 && numberSatelites ==0)
      {
        for (int bkgdCount = 0; bkgdCount < bkgdPlanets.length; bkgdCount++)
        {
          // background planets get attracted next!
          if (bkgdPlanets[bkgdCount] != null)
          {
            numberBkgdPlanets++;
            bkgdPlanets[bkgdCount].acceleration.add ( ( (mouseX - 
              bkgdPlanets[bkgdCount].location.x) 
              * bkgdPlanets[bkgdCount].pullDelay), 0, 0 );
            bkgdPlanets[bkgdCount].acceleration.add (0, ( (mouseY - 
              bkgdPlanets[bkgdCount].location.y)  
              * bkgdPlanets[bkgdCount].pullDelay), 0 );

            if ( dist(bkgdPlanets[bkgdCount].location.x, bkgdPlanets[bkgdCount].location.y, mouseX, 
            mouseY ) < 3* bkgdPlanets[bkgdCount].spaceObjectRadius)
            {
              bkgdPlanets[bkgdCount].showMe = false;
              numberBkgdPlanets--;
              this.blackHoleSize += (bkgdPlanets[bkgdCount].spaceObjectRadius) / 10;
              score += (bkgdPlanets[bkgdCount].spaceObjectRadius) / 10;
              // Black Hole continues to grow, and so does the user's score!
            }
          }
        }
      }

      if (numberBkgdPlanets == 0 && numberGravPlanets == 0 && numberSatelites ==0)
      {
        for (int starCount = 0; starCount < stars.length; starCount++)
        {
          // stars get eaten last!
          if (stars[starCount] != null)
          {
            numberStars++;

            stars[starCount].acceleration.add ( ( (mouseX - 
              stars[starCount].location.x) 
              * stars[starCount].pullDelay), 0, 0 );
            stars[starCount].acceleration.add (0, ( (mouseY - 
              stars[starCount].location.y)  
              * stars[starCount].pullDelay), 0 );

            if ( dist(stars[starCount].location.x, stars[starCount].location.y, mouseX, 
            mouseY ) < this.spaceObjectRadius)
            {
              stars[starCount].showMe = false;
              numberStars--;
              this.blackHoleSize += 1;
              score += 1;
              // Watch Black Hole eat the stars in the sky, and score big for the user!
            }
          }
        }
      }
      if (numberBkgdPlanets == 0 && numberGravPlanets == 0 && numberSatelites ==0 && numberStars == 0)
      {
        textSize(50);
        fill(255, 0, 0);
        text("Black Hole has consumed the galaxy!", 100, 100);
        text("Black Hole scored " + score + " points!", 100,500);
        // Game Over!  The Black Hole has conusmed the galaxy!
        // The player gets to see how many points their randomly generated galaxy was worth!
      }
    } // Satelites respond by directly attempting to get close to the 
    //   position of the mouse
    // for as long as the mouse button is held down.  If the user moves the mouse 
    //   around while
    // continuing to hold the button down, the satelites will attempt to follow
    // The same holds true for the gravity planets, then the background planets, then the stars!

    if (! mousePressed)
    {
      // When Black Hole's power is hidden, the galaxy is not pulled toward it!
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
}

