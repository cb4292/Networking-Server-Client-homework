from socket import socket, AF_INET, SOCK_STREAM

if __name__ == "__main__":
    server = input("Input destination IP address: ")
    message = input("Input message text: ")
    (SERVER, PORT) = (server, 9999)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((SERVER, PORT))
    s.send(message)
    response = s.recv(1024)
    s.close()
    print("Received: ", response)
