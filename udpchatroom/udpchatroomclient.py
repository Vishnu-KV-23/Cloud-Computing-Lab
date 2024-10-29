import socket
import threading

def receive_messages(client_socket):
    # Continuously receive messages from the server
    while True:
        try:
            message, _ = client_socket.recvfrom(1024)
            print("\n" + message.decode('utf-8'))
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def start_chatroom_client():
    # Define the server IP address and port number to connect to
    server_ip = '127.0.0.1'
    server_port = 12345

    # Create a socket object with IPv4 and UDP settings
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Start a thread to listen for incoming messages
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    print("Type 'exit' to leave the chatroom.")

    # Send messages to the server
    while True:
        message = input("You: ")
        client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))

        if message.lower() == 'exit':
            print("You left the chatroom.")
            break

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    start_chatroom_client()
