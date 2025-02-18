# Socket - QOTD Server
This project implements a Quote of the Day (QOTD) server using Python's socket API. The server listens for incoming connections and sends a random quote when a client connects. It demonstrates the fundamental concepts of socket programming, including creating a socket, binding it to a port, listening for connections, and sending/receiving data using TCP or UDP protocols.

The project includes both the server code and a client implementation, and can be tested locally or across multiple machines using virtual containers.

## Code Explanation
### Server
The customServer.py script creates a TCP or UDP server that listens on a specified port for incoming client connections. When a connection is established, the server sends a quote in response and then closes the connection.

Key parts of the server code:

- Socket creation: socket.socket(socket.AF_INET, socket.SOCK_STREAM) (for TCP) or socket.SOCK_DGRAM (for UDP).
- Binding: The server binds to a host and port.
- Listening: The server listens for incoming connections using listen() for TCP connections.
- Accepting connections: Using accept() for TCP connections.
- Receiving and sending data: recv() to receive data and send() or sendto() to send a response.
- Closing: Once data is sent, the server closes the connection.

### Client
The customClient.py script connects to the server, sends a message, and receives the response.

Key parts of the client code:

- Socket creation: Similar to the server.
- Connection: The client connects to the server using connect().
- Sending and receiving data: send() to send data and recv() to receive the response.
- Closing the connection: Once the message is sent and the response is received, the connection is closed.