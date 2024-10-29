import socket

def start_chatroom_server():
    # Define the IP address and port number
    server_ip = '127.0.0.1'
    server_port = 12345

    # Create a socket object with IPv4 and UDP settings
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the address and port
    server_socket.bind((server_ip, server_port))
    print(f"Chatroom server started on {server_ip}:{server_port}")

    # Dictionary to store active client addresses
    clients = set()

    # Receive and broadcast messages
    while True:
        try:
            # Receive message and client address
            message, client_address = server_socket.recvfrom(1024)
            message = message.decode('utf-8')

            # Check for exit command
            if message.lower() == 'exit':
                print(f"{client_address} left the chat.")
                clients.discard(client_address)
                continue

            # Add the client to the list of active clients
            if client_address not in clients:
                clients.add(client_address)
                print(f"{client_address} joined the chat.")

            # Display received message
            print(f"Received from {client_address}: {message}")

            # Broadcast the message to all active clients
            for client in clients:
                if client != client_address:  # Avoid sending back to sender
                    server_socket.sendto(f"{client_address}: {message}".encode('utf-8'), client)

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    # Close the socket
    server_socket.close()

if __name__ == "__main__":
    start_chatroom_server()
