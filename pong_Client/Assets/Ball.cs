
// Jason Heckard 84851006

// Jon Shokoor 54287589

// Sam Hohmann 92315421

using UnityEngine;
using System.Collections;

public class Ball : MonoBehaviour 
{ 
	public Vector3 speed;
	public float ballSpeedX = 100.0f;
	public float ballSpeedY = 100.0f;
	
	public Paddle[] paddles;
	
	// Use this for initialization
	void Start () 
	{
		
		speed = rigidbody.velocity;
		
		transform.position = new Vector2(0f, 0f);
		
		float startX = (Random.Range(-1.0f, 1.0f) ) * ballSpeedX;
		float startY = (Random.Range(-1.0f, 1.0f) ) * ballSpeedY;
		
		rigidbody.velocity = new Vector2(startX, startY);
		
		paddles = new Paddle[2];
		
		paddles[0] = GameObject.Find("PaddleLeft").GetComponent<Paddle>();
		paddles[1] = GameObject.Find("PaddleRight").GetComponent<Paddle>();
		
	}
	
	// Update is called once per frame
	void Update () 
	{
		
		 if( Mathf.Abs(rigidbody.velocity.x) < 100.0f)
		{
			if(rigidbody.velocity.x > 0.0f)
			{
				rigidbody.velocity = new Vector2(100.0f, rigidbody.velocity.y);	
			}
			
			else
			{
				rigidbody.velocity = new Vector2(-100.0f, rigidbody.velocity.y);
			}
		}
		
		if(Mathf.Abs(rigidbody.velocity.y) < 100.0f)
		{
			if(rigidbody.velocity.y > 0.0f)
			{
				rigidbody.velocity = new Vector2(rigidbody.velocity.x, 100.0f);
			}
			
			else
			{
				rigidbody.velocity = new Vector2(rigidbody.velocity.x, -100.0f);
			}
		}
		
		speed = rigidbody.velocity;
		
	}
	
	void OnCollisionEnter(Collision collidedWith) 
	{
		Paddle p = collidedWith.collider.GetComponent<Paddle>();
		
		if(p != null)
		{
			p.Impulse(535.5f);
		}
    	
		if (collidedWith.collider.name == "BorderLeft")
        {
			// print ("Collide" + collidedWith.collider.name);
			
			paddles[1].score++;
            // ToDo: right player scores a point  
			transform.position = Vector3.zero;
			
			rigidbody.velocity = new Vector2( (Random.Range(-100.0f, 100.0f) ), Random.Range(-100.0f, 100.0f) );
			rigidbody.velocity = rigidbody.velocity * -1.0f;
			
			rigidbody.velocity = (rigidbody.velocity.normalized * 125.0f);
        }

        else if (collidedWith.collider.name == "BorderRight")
        {
			// print ("Collide" + collidedWith.collider.name);
			
			paddles[0].score++;
            // ToDo: left player scroes a point
			transform.position = Vector3.zero;
			
			rigidbody.velocity = new Vector2( (Random.Range(-100.0f, 100.0f) ), Random.Range(-100.0f, 100.0f) );
			rigidbody.velocity = rigidbody.velocity * -1.0f;
			
			rigidbody.velocity = (rigidbody.velocity.normalized * 125.0f);

        }

        else if (collidedWith.collider.name == "BorderTop")

        {
			// print ("Collide" + collidedWith.collider.name);
            // ToDo bounce off in the way we want it to 
			rigidbody.velocity = new Vector2(rigidbody.velocity.x, -100.0f);

        }

        else if (collidedWith.collider.name == "BorderBottom")

        {
			// print ("Collide" + collidedWith.collider.name);
            // ToDo bounce off in the way we want it to 
			rigidbody.velocity = new Vector2(rigidbody.velocity.x, 100.0f);
        }               

        else if (collidedWith.collider.name == "PaddleLeft")

        {
			// print ("Collide" + collidedWith.collider.name);
            // ToDo bounce off in the way we want it to 
			rigidbody.velocity = new Vector2 ( 75.0f, rigidbody.velocity.y );
        }               

        else if (collidedWith.collider.name == "PaddleRight")

        {
			// print ("Collide" + collidedWith.collider.name);
            // ToDo bounce off in the way we want it to 
			rigidbody.velocity = new Vector3 ( -75.0f, rigidbody.velocity.y );

        }
        
    }
}
