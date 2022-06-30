from concurrent.futures import thread
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

conexoes = []
mensagens = []

def enviar_mensagem_ind(conexao):
    print("[ENVIANDO] Enviando mensagem")
    for i in range(conexao['last'], len(mensagens)):
        mensagem_de_envio = "msg=" + mensagens[i]
        conexao['conn'].send(mensagem_de_envio)
        conexao['last'] = i + 1
        time.sleep(0.2)

def enviar_mensagem_todos():
    global conexoes
    for conexao in conexoes:
        enviar_mensagem_ind(conexao)

def handle_alvo(conn, addr):
    print(f"[NOVA CONEXÃO] O peixe fisgou a isca pelo endereço {addr}")
    global conexoes
    global mensagens
    nome = False

    while(True):
        msg = conn.recv(1024).decode(FORMATO)
        if(msg):
            if (msg.startswith("nome")):
                mensagem_separada = msg.split('=')
                nome = mensagem_separada[1]
                mapa_conexao = {
                    "conn": conn, 
                    "addr": addr, 
                    "nome": nome, 
                    "last": 0
                }
                conexoes.append(mapa_conexao)
                enviar_mensagem_ind(mapa_conexao)
            elif(msg.startswith("msg=")):
                mensagem_separada = msg.split('=')
                mensagem = mensagem_separada[1]
                mensagem.append(mensagem)
                enviar_mensagem_todos()

def start ():
    print("[INICIANDO]"+"*"*20)
    socket.listen()
    while(True):
        conn, addr = socket.accept()
        thread = threading.Thread(target=handle_alvo, args=(conn, addr))
        thread.start()

start()
