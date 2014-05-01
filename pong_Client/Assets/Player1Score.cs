using UnityEngine;
using System.Collections;

public class Player1Score : MonoBehaviour 
{
	public Paddle player;

	// Use this for initialization
	void Start () 
	{
		player = GameObject.Find("PaddleLeft").GetComponent<Paddle>();
		
	}
	
	// Update is called once per frame
	void Update () 
	{
		guiText.text = "Player 1 Score \n" + "           " + player.score;
	}
}
