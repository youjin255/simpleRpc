import socket


class Server(object):
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind_listen(self, port):
        self.socket.bind(('0.0.0.0', port))
        self.socket.listen(5)

    def accept_receive_close(self):
        (connection, address) = self.socket.accept()
        req = connection.recv(1024)
        self.on_req(req)
        connection.close()