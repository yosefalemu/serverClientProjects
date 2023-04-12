import socket

HEADER = 64
PORT = 5050
DISCONNECT_MESSAGE = "!DISCONNECT"
FORMAT = "utf-8"
SERVER = "10.5.223.121"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
send("HELLO WORLD!")
input()
send("HELLO EVERONE!")
input()
send("HELLO TEAM!")
send(DISCONNECT_MESSAGE)
send("work")

 
    





