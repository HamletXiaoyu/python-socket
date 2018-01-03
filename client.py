# -*- coding: utf-8 -*-
import socket


obj = socket.socket()

obj.connect(("127.0.0.1", 8080))

ret_bytes = obj.recv(1024)
ret_str = str(ret_bytes)
print(ret_str)

while True:
    inp = input("Hi, what's your question?\n>>>")
    if inp == "q":
        obj.sendall(bytes(inp))
        break
    else:
        obj.sendall(bytes(inp))
        ret_bytes = obj.recv(1024)
        ret_str = str(ret_bytes)
        print(ret_str)


