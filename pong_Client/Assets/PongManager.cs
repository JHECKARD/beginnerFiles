
// Jason Heckard 

// Jon Shokoor 

// Sam Hohmann 

using UnityEngine;
using System.Collections;

public class PongManager : MonoBehaviour 
{
	public Paddle[] paddles;
	
	public PlayerClient player;
	
	int paddlePositionY;
	
	public bool movingUp;
	public bool movingDown;
	
	Ball gameBall;

	// Use this for initialization
	void Start () 
	{
		paddles = new Paddle[2];
		
		paddles[0] = GameObject.Find("PaddleLeft").GetComponent<Paddle>();
		paddles[1] = GameObject.Find("PaddleRight").GetComponent<Paddle>();

		player = GameObject.Find("PongClient").GetComponent<PlayerClient>();
		
		movingUp = false;
		movingDown = false;
		
		gameBall = GameObject.Find("Ball").GetComponent<Ball>();
		
	}
	
	// Update is called once per frame
	void Update () 
	{
		// left paddle controls
		if(player.number == 0 && player.client.Connected )
		{
			if(Input.GetKeyDown(KeyCode.UpArrow) )
			{
				movingUp = true;
				
				paddles[0].MoveUp();
			}
			
			if(Input.GetKeyUp(KeyCode.UpArrow) )
			{
				movingUp = false;
				
				paddles[0].Halt();
			}
			
			if(Input.GetKeyDown(KeyCode.DownArrow) )
			{
				movingDown = true;
				
				paddles[0].MoveDown();
			}
			
			if(Input.GetKeyUp(KeyCode.DownArrow) )
			{
				movingDown = false;
				
				paddles[0].Halt();
			}
			
			if(Input.GetKeyDown(KeyCode.LeftArrow) )
			{
				paddles[0].Impulse(317.5f);
			}
		}
		
		else if (player.number == 1)
		{
			if(Input.GetKeyDown(KeyCode.UpArrow) )
			{
				movingUp = true;
				
				paddles[1].MoveUp();
			}
			
			if(Input.GetKeyUp(KeyCode.UpArrow) )
			{
				movingUp = false;
				
				paddles[1].Halt();
			}
			
			if(Input.GetKeyDown(KeyCode.DownArrow) )
			{
				movingDown = true;
				
				paddles[1].MoveDown();
			}
			
			if(Input.GetKeyUp(KeyCode.DownArrow) )
			{
				movingDown = false;
				
				paddles[1].Halt();
			}
			
			if(Input.GetKeyDown(KeyCode.LeftArrow) )
			{
				paddles[1].Impulse(-317.5f);
			}
		}
	}
}
