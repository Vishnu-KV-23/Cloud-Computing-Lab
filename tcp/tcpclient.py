import socket

def start_client():
    # Define the server IP address and port number to connect to
    server_ip = '127.0.0.1'  # Localhost
    server_port = 12345

    # Create a socket object with IPv4 and TCP settings
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server at {server_ip}:{server_port}")

    # Send and receive messages from the server
    while True:
        message = input("Enter message to send (type 'exit' to close): ")
        client_socket.send(message.encode('utf-8'))

        if message.lower() == 'exit':
            print("Closing connection with the server.")
            break

        # Receive response from the server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
