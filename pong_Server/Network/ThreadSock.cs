
// Jason Heckard

// Jon Shokoor

// Sam Hohmann


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.Net.Sockets;

namespace Network
{
    class ThreadSock
    {
        private NetworkStream nws;
        private SocketShutdown socks;
        private PlayerSocket socket;

        public ThreadSock(NetworkStream inStream, PlayerSocket newSocket)
        {
            nws = inStream;
            socket = newSocket;
        }

        public void Operate()
        {
            try
            {
                while (true)
                {

                }
            }

            catch (Exception problem)
            {
                Console.WriteLine ("Exception thrown " + problem.Message);
            }
        }
    }
}
