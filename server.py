import socket
from helper import get_full_message

HOST = "127.0.0.1" # Localhost
PORT = 5000 # Server port number

# Create socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    while True:
        print("Waiting to connect with a client")
        # Waits for connection
        connection, address = server.accept()
        with connection:
            print(f"Connected to client in port {address[1]}")
            while True:
                message = get_full_message(connection)
                print(f'Received message "{message}" from client in port {address[1]}')
                # Closes the server
                if not message or message == "DESCONEXION":
                    print("Client disconnected from server")
                    break
                data = message.upper()
                # Returns uppercase message to client
                connection.sendall(data.encode())

print("Server has been shut down")