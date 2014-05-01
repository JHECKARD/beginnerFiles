
// Jason Heckard

// Jon Shokoor

// Sam Hohmann


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.IO;
using System.Net.Sockets;
using System.Net;
using System.Diagnostics;
using System.Threading;

namespace Network
{ // start namespace

    class PlayerSocket
    { // start class
        const string SERVER_LOCATION = "128.195.11.140";
        const int SERVER_PORT = 8754;

        public TcpClient client;

        // player socket network stream
        public NetworkStream psnws;
        public int clientNumber;              
        public bool startGame;
        public bool connected;
        public DateTime dateTime;
        public Thread psThread = null;
        protected static bool threadState = false;
        public Queue<string> updates;
        public Socket pSock;

        public StreamReader playerReader;
        public StreamWriter playerWriter;

        public PlayerSocket(NetworkStream newStream, Socket newSocket, StreamReader newSR, StreamWriter newSW)
        {
            psnws = newStream;
            pSock = newSocket;
            playerReader = newSR;
            playerWriter = newSW;

            updates = new Queue<string>();
        }

        /*
        public bool Connect()
        {
            Console.WriteLine(" trying to connect");

            try
            {
                client = new TcpClient(SERVER_LOCATION, SERVER_PORT);

                if (client.Connected)
                {
                    psnws = client.GetStream();
                    ThreadSock connectSock = new ThreadSock(psnws, this);
                    psThread = new Thread(new ThreadStart(connectSock.Operate) );
                    psThread.IsBackground = true;
                    psThread.Start();

                    threadState = true;
                }
            } 

            catch (Exception problem)
            {
                Console.WriteLine("Exception thrown " + problem.Message);
            }

            if (client == null)
            {
                return false;
            }

            return client.Connected;
        }

        public bool Disconnect()
        {
            try
            {
                psnws.Close();
                client.Close();
                //endThread();  threads end automatically?
                //testThread(); ?
            }
            catch (Exception problem)
            {
                Console.WriteLine("Exception thrown " + problem.Message);
                return false;
            }
            return true;

        }

        public void SendTCPPacket(int toSend)
        {
            try
            {
                Console.WriteLine("Trying to send nonexistant packet");
            }
            catch (Exception ira)
            {
                Console.WriteLine("Exception thrown " + ira.Message);
            }
        }

        public bool sendStartGame()
        {
            if (client.Connected)
            {
                Console.WriteLine("Connected!");
                return true;
            }

            Console.WriteLine("Not connected :-( " );
            return false;
        }

        public void setStreamReader(StreamReader newReader)
        {
            playerReader = newReader;
        }

        public void setStreamWriter(StreamWriter newWriter)
        {
            playerWriter = newWriter;
        }

        public static void Service()
        {


        }
         * */
    } // end class
} // end namespace 
