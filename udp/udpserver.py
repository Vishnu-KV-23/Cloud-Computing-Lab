import socket

def start_udp_server():
    # Define the IP address and port number
    server_ip = '127.0.0.1'  # Localhost
    server_port = 12345  # Any port above 1024 can be used

    # Create a socket object with IPv4 and UDP settings
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the address and port
    server_socket.bind((server_ip, server_port))
    print(f"UDP Server started on {server_ip}:{server_port}")

    # Receive data from the client
    while True:
        message, client_address = server_socket.recvfrom(1024)  # 1024 bytes buffer size
        message = message.decode('utf-8')
        print(f"Received from client {client_address}: {message}")

        if message.lower() == 'exit':
            print("Client requested to close the connection.")
            break

        # Sending a response back to the client
        response = input("Enter response to client: ")
        server_socket.sendto(response.encode('utf-8'), client_address)

    # Close the socket
    server_socket.close()
    print("Server closed.")

if __name__ == "__main__":
    start_udp_server()
