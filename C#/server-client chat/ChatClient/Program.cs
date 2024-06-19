using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace ChatClient
{
    class Program
    {
        static async Task Main(string[] args)
        {
            try
            {
                string serverIP = "127.0.0.1";
                int port = 1234;


                TcpClient client = new TcpClient();
                await client.ConnectAsync(serverIP, port);
                Console.WriteLine("Connected to server.");

                NetworkStream stream = client.GetStream();

                while (true)
                {
                    Console.Write("Enter message: ");
                    string message = Console.ReadLine();
                    byte[] data = Encoding.ASCII.GetBytes(message);
                    await stream.WriteAsync(data, 0, data.Length);

                    byte[] buffer = new byte[1024];
                    int bytesRead = await stream.ReadAsync(buffer, 0, buffer.Length);
                    string response = Encoding.ASCII.GetString(buffer, 0, bytesRead);
                    Console.WriteLine($"Server response: {response}");
                }

            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
