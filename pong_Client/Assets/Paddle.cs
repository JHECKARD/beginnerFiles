
// Jason Heckard 

// Jon Shokoor 

// Sam Hohmann 

using UnityEngine;
using System.Collections;

public class Paddle : MonoBehaviour 
{
	public Transform paddleMesh;
	public float spinSpeed;
	public int score;
	
	public int positionY;
	
	private const float moveSpeed = 250.0f;
	
	// Use this for initialization
	void Start () 
	{
		score = 0;
	}
	
	// Update is called once per frame
	void Update () 
	{
		positionY = (int) transform.position.y;
		
		if( (spinSpeed - 1) > 0.1f)
		{
			spinSpeed *= 0.98f;
			paddleMesh.Rotate(Vector3.up, spinSpeed * Time.deltaTime);
		}
		
		else
		{
			spinSpeed = 0;
		}
		
		if(transform.position.y > 210f)
		{
			rigidbody.velocity = Vector3.zero;
			transform.position = new Vector3(transform.position.x, 210f, 0.0f);
		}
		
		if(transform.position.y < -210f)
		{
			rigidbody.velocity = Vector3.zero;
			transform.position = new Vector3(transform.position.x, -210f, 0.0f);
		}
		
		if(transform.position.x > 0)
		{
			if( ( (transform.position.x - 380) > 0.1f) || ( (transform.position.x - 380) < -0.1f) )
			{
				transform.position = new Vector3(380.0f, transform.position.y, 0);
			}
		}
		
		if(transform.position.x < 0)
		{
			if( ( (transform.position.x + 380) > 0.1f) || ( (transform.position.x + 380) < -0.1f) )
			{
				transform.position = new Vector3(-380.0f, transform.position.y, 0);
			}
		}
	}
	
	public void Impulse(float magnitude)
	{
		spinSpeed += magnitude;
	}
	
	public void MoveUp()
	{
		rigidbody.velocity = Vector2.up * moveSpeed;
	}
	
	public void MoveDown()
	{
		rigidbody.velocity = -1 * Vector2.up * moveSpeed;
	}
	
	public void Halt()
	{
		rigidbody.velocity = Vector2.zero;
	}
	
	public void setPosition( int newY)
	{
		transform.position = new Vector3(transform.position.x, newY, 0.0f);
	}
}
