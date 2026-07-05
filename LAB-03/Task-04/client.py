import socket


FORMAT = "utf-8"
HEADER = 64

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 4949
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "End"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg: str) -> None:
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(FORMAT))

while True:
    hours_worked = input("Enter a message: ")
    send(hours_worked)
    if hours_worked == DISCONNECT_MESSAGE:
        break