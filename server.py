import socket
import threading
import time

input()

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 433
ADDR = (SERVER_IP, PORT)
FORMATO = 'utf-8'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def start ():
    print("[INICIANDO]"+"*"*20)
    socket.listen()
    while(True):
        socket.accept()
