import socket
import threading

# List to keep track of connected clients
clients = []

# Broadcast function to send a message to all clients
def broadcast(message, sender_socket):
    for client in clients:
        # Don't send the message back to the sender
        if client != sender_socket:
            try:
                client.send(message)
            except:
                # Remove client if sending fails
                clients.remove(client)

# Handle each client connection
def handle_client(client_socket, client_address):
    print(f"{client_address} connected.")
    while True:
        try:
            # Receive a message from the client
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Received from {client_address}: {message.decode('utf-8')}")

            # Broadcast the received message to all clients
            broadcast(message, client_socket)
        except:
            # If an error occurs, remove the client and break the loop
            clients.remove(client_socket)
            client_socket.close()
            print(f"{client_address} disconnected.")
            break

def start_chatroom_server():
    # Define IP address and port
    server_ip = '127.0.0.1'
    server_port = 12345

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen()
    print(f"Chatroom server started on {server_ip}:{server_port}")

    # Accept connections from multiple clients
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)

        # Start a new thread for each client
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    start_chatroom_server()
