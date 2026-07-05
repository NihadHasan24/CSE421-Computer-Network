import socket


FORMAT = "utf-8"
HEADER = 64

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 4949
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "End"


def calculate_salary(hours_worked: float) -> float:
    if hours_worked <= 40:
        return hours_worked * 200
    return 8000 + ((hours_worked - 40) * 300)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print(f"Server is running on {SERVER}:{PORT}")

server.listen()
print(f"Server is listening on {SERVER}:{PORT}")

while True:
    conn, addr = server.accept()
    print(f"Connection from {addr} has been established.")
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.send("Connection closed.".encode(FORMAT))
            else:
                hours_worked = float(msg)
                salary = calculate_salary(hours_worked)
                response = f"Salary: Tk {salary:.2f}"
                print(f"Hours received from {addr}: {hours_worked}")
                conn.send(response.encode(FORMAT))

    conn.close()