import socket
import threading
# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Receive and print messages from the server
            message = client_socket.recv(1024).decode('utf-8')
            print("\n" + message)
        except:
            # If an error occurs, close the connection
            print("An error occurred. Disconnected from chat.")
            client_socket.close()
            break

def start_chatroom_client():
    # Define the server IP address and port to connect to
    server_ip = '127.0.0.1'
    server_port = 12345

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print("Connected to the chatroom. Type 'exit' to leave.")

    # Start a thread to receive messages from the server
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    # Send messages to the server
    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            print("You left the chatroom.")
            client_socket.send("exit".encode('utf-8'))
            client_socket.close()
            break
        else:
            client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_chatroom_client()
