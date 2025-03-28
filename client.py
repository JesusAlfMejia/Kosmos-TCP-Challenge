import socket
from helper import get_full_message

HOST = "127.0.0.1" # Localhost
PORT = 5000 # Server port number

# Creates socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    # Connects to server
    client.connect((HOST, PORT))
    while True:
        message = input("What message do you want converted to uppercase?\n")
        # Sends message to server
        client.sendall(message.encode())
        # Closes the connection
        if message == "DESCONEXION":
            print("Disconnecting from server")
            break
        # Receives returned message from server
        data = get_full_message(client)
        print(data)
