from concurrent.futures import thread
import socket
import threading
import time

input()

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 433
ADDR = (SERVER_IP, PORT)
FORMATO = 'utf-8'