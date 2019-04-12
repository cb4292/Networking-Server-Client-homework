from socket import socket, AF_INET, SOCK_STREAM


def handle(self):
    self.message = self.upper.request.recv(4096)
    print("Message contents are:")
    string_start = self.message.find("SECRET")
    if string_start > -1:
        self.response = "Digits: "
        self.count_up = 0
        for i in self.message:
            if i > 47 & i < 58:
                self.countup + 1
                self.response = self.response + i
        self.response += " Count: "
        self.response += self.countup
        self.sendall(self.response)


if __name__== "main__":
    s = socket(AF_INET, SOCK_STREAM)
    s.bind('127.0.0.1, 9999')
    s.listen(5)
    while True:
        new_socket, client_address = s.accept()
        new_socket.handle()
        