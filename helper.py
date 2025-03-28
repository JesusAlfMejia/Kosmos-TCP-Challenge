# Helper function to receive full message in case it is larger than 1024 bytes
def get_full_message(connection):
    full_message = ""
    while True:
        segment = connection.recv(1024).decode()
        full_message += segment
        if len(segment) < 1024:
            break
    return full_message
