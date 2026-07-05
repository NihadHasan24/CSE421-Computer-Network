import socket

FORMAT = 'utf-8'
HEADER = 64

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 4949
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = 'End'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print(f'Server is running on {SERVER}:{PORT}')

server.listen()
print(f'Server is listening on {SERVER}:{PORT}')

while True:
    conn, addr = server.accept()
    print(f'Connection from {addr} has been established.')
    Connected = True
    while Connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                Connected = False
                conn.send('Connection closed.'.encode(FORMAT))
            else:
                print(f'Message from {addr}: {msg}')
                conn.send('Message received.'.encode(FORMAT))
    conn.close()