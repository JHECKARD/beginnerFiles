
// Jason Heckard 

// Jon Shokoor 

// Sam Hohmann 

using UnityEngine;
using System.Collections.Generic;
using System.Text;
using System.Linq;

using System.Net.Sockets;
using System.IO;
using System.Threading;

public class PlayerClient : MonoBehaviour 
{
	public TcpClient client;
	public int number = -1;
	
	NetworkStream stream;
	StreamReader reader;
	StreamWriter writer;
	
	Queue<string> moves = new Queue<string>();
	
	public PongManager manager;
	
	char delimiter = '&';
	
	// Use this for initialization
	void Start () 
	{ // start start
		
		manager = GameObject.Find("PongManager").GetComponent<PongManager>();

		print("Trying to connect to server");

		try
		{ // start try
			
			client = new TcpClient();
			
			// 128 195 11 140
			client.Connect("127.0.0.1", 4002);
			
			if(! client.Connected)
			{
				print ("Connection failed!");	
			}
			
			stream = client.GetStream();
			reader = new StreamReader(stream);
			writer = new StreamWriter(stream);
			writer.AutoFlush = true;
			
			string data = reader.ReadLine();

            print(data);
            number = int.Parse(data);

            print(" client number " + number);
			
            writer.WriteLine("Player says client number " + number);
			
			Thread mThread = new Thread(new ThreadStart(Process) );
			
			mThread.Start();
			
		} // end try
		
		catch (System.Exception e)
		{
			print("Exception e" + e.ToString() );
		}

		print ("end start");
	} // end start
	
	// Update is called once per frame
	void Update () 
	{ // start update

		print(" ********  Queue Size " + moves.Count);
		
		if(manager.movingUp)
		{
			writer.WriteLine("paddleUp&" + number);
		}
		
		if(manager.movingDown)
		{
			writer.WriteLine("paddleDown&" + number);
		}
			
		if(moves.Count > 0)
		{
			string nextMove = moves.Dequeue();
				
			print(" next move " + nextMove); 
				 
			string[] instruction = nextMove.Split (delimiter);
			
			// define a new instruction string
			// instruction[0] = player number
			// instruction[1] = position y
			manager.paddles[ (int.Parse(instruction[0]) ) ].setPosition( int.Parse(instruction[1]) );
		}
			
	}
	
	void Process()
	{
		while(client.Connected)
		{ // thread game loop for the client 
			print ("Thread Processing");
			
			try
			{
				if(moves.Count < 100)
				{
					string data = reader.ReadLine();
				
					moves.Enqueue(data);
	
	        		// print(data);
				}
			}
			
			catch(System.Exception ira)
			{
				print(" process catch " + ira.Message);	
			}
			
		} // end game loop 
		
		
	}
}
