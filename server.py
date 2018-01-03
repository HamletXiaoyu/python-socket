# -*- coding: utf-8 -*-
import socket
import  socketserver

class Myserver(socketserver.BaseRequestHandler):

    def handle(self):
        conn = self.request
        conn.sendall(bytes("Hi, I am robot"))
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes)
            if ret_str == "q":
                break
            conn.sendall(bytes('I can only say Hi'))

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 8080), Myserver)
    server.serve_forever()


