using UnityEngine;
using System.Collections;

public class Player2Score : MonoBehaviour 
{
	public Paddle player;
	
	// Use this for initialization
	void Start () 
	{
		player = GameObject.Find("PaddleRight").GetComponent<Paddle>();
		
	}
	
	// Update is called once per frame
	void Update () 
	{
		guiText.text = "Player 2 Score \n" + "           " + player.score;
	}
}
