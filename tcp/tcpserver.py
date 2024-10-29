import socket

def start_server():
    # Define the IP address and port number
    server_ip = '127.0.0.1'  # Localhost
    server_port = 12345  # Any port above 1024 can be used

    # Create a socket object with IPv4 and TCP settings
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((server_ip, server_port))
    print(f"Server started on {server_ip}:{server_port}")

    # Enable the server to accept one connection at a time
    server_socket.listen(1)
    print("Waiting for a connection...")

    # Accept a connection from the client
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Receive data from the client and send a response
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message.lower() == 'exit':
            print("Client requested to close the connection.")
            break
        print(f"Received from client: {message}")
        
        response = input("Enter response to client: ")
        client_socket.send(response.encode('utf-8'))

    # Close the connection
    client_socket.close()
    server_socket.close()
    print("Server closed connection.")

if __name__ == "__main__":
    start_server()
