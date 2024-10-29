import socket

def start_udp_client():
    # Define the server IP address and port number to connect to
    server_ip = '127.0.0.1'  # Localhost
    server_port = 12345

    # Create a socket object with IPv4 and UDP settings
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send and receive messages from the server
    while True:
        message = input("Enter message to send (type 'exit' to close): ")
        client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))

        if message.lower() == 'exit':
            print("Closing connection with the server.")
            break

        # Receive response from the server
        response, server_address = client_socket.recvfrom(1024)
        print(f"Received from server: {response.decode('utf-8')}")

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    start_udp_client()
