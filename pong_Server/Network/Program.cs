
// Jason Heckard

// Jon Shokoor

// Sam Hohmann

// found a code example showing how to set up the main() with a thread for each player
// http://www.codeproject.com/Articles/10649/An-Introduction-to-Socket-Programming-in-NET-using


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Net;
using System.Net.Sockets;
using System.IO;
using System.Threading;

using System.Diagnostics;

namespace Network
{
    class Program
    {
        static TcpListener listener;

        const int numberPlayers = 2;

        protected static PlayerSocket[] playersPlayingGame = new PlayerSocket[numberPlayers];

        Stopwatch physicsTimer = new Stopwatch();

        static Queue<string> movesMade;
        
        static void Main(string[] args)
        { // start main
            listener = new TcpListener(8754);   // listen on port 8754
            listener.Start();                   // start the listener

            movesMade = new Queue<string>();

            Console.Write("Press Enter to Start the server: ");
            Console.Read();

            for (int p = 0 ; p < numberPlayers; ++p)
            { // for loop 

                Socket sock = listener.AcceptSocket();
                Console.WriteLine("   player socket has accepted the socket " + p);

                NetworkStream nws = new NetworkStream(sock);
                StreamReader sr = new StreamReader(nws);
                StreamWriter sw = new StreamWriter(nws);
                sw.AutoFlush = true;

                playersPlayingGame[p] = new PlayerSocket(nws, sock, sr, sw);

                // assign client number to client
                Console.WriteLine(" player number equals " + p);

                playersPlayingGame[p].playerWriter.WriteLine(p);
                playersPlayingGame[p].connected = true;

                string data = playersPlayingGame[p].playerReader.ReadLine();
                Console.WriteLine(data);

                ReadThread threadClass = new ReadThread(p);

                playersPlayingGame[p].psThread = new Thread(new ThreadStart(threadClass.Service));
                playersPlayingGame[p].psThread.Start();

            } // for loop 

        } // end main 

        public class ReadThread
        {
            int client = -1;
            char delimiter = '&';

            string clientString;
          
            public ReadThread(int clientNumber)
            {
                client = clientNumber;
                clientString = client.ToString();
            }

            public void Service()
            {
                try
                { // start try 

                    while (playersPlayingGame[client].connected)
                    { // start game loop

                        string data = playersPlayingGame[client].playerReader.ReadLine();
                        Console.WriteLine("before delimiter print " + data);

                        movesMade.Enqueue(data);

                        // instruction [0] = paddle move
                        // instruction [1] = player client number
                        // instruction [2] = new Y position
                        string[] instruction = movesMade.Dequeue().Split(delimiter);
                        
                        Console.WriteLine("Service print " + instruction[0] + " " + instruction[1] + " " 
                            + instruction[2] + " client number " + client);

                        for (int p = 0; p < numberPlayers; ++p)
                        {
                            playersPlayingGame[p].playerWriter.WriteLine(instruction);
                        }

                        /*
                        if( (instruction[0] == "paddleMove") && (instruction[1] != clientString ) )
                        {
                            // sending:
                            // instruction [0] = opponentMove
                            // instruction [1] = opponent client number 
                            // instruction [2] = new Y position of opponent 
                            Console.WriteLine("opponentMove&" + instruction[1].ToString() + "&" + instruction[2].ToString() );
                            playersPlayingGame[client].playerWriter.WriteLine("opponentMove&" + instruction[1].ToString() + "&"+ instruction[2].ToString() );
                        }
                         * */
                        
                    } // end game looop
                } // end try

                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
            }
        }
    }

    class Ball
    {
        int ballPositionX;
        int ballPositionY;

        int ballSpeedX;
        int ballSpeedY;
    }
}
