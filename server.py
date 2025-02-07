import socket

HOST = "0.0.0.0" #can connect from any IP 
PORT = 5555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

print(" Waiting for players to connect...")
clients = []

while len(clients) < 2:
    conn, addr = server.accept()
    print(f"Player connected from {addr}")
    clients.append(conn)

for conn in clients:
    conn.sendall(b"Connected to Ping Pong Server")

ball_x, ball_y = 400, 300
ball_speed_x, ball_speed_y = 5, 5

paddles_y = [250, 250]

while True:
    try:
        paddles_y[0] = int(clients[0].recv(1024).decode())
        paddles_y[1] = int(clients[1].recv(1024).decode())

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_y <= 0 or ball_y >= 600 - 15:
            ball_speed_y *= -1

        if (ball_x <= 70 and paddles_y[0] < ball_y < paddles_y[0] + 100) or \
           (ball_x >= 730 and paddles_y[1] < ball_y < paddles_y[1] + 100):
            ball_speed_x *= -1 

        if ball_x < 0 or ball_x > 800:
            ball_x, ball_y = 400, 300 

        game_state = f"{paddles_y[1]},{ball_x},{ball_y}" 
        clients[0].sendall(game_state.encode())

        game_state = f"{paddles_y[0]},{ball_x},{ball_y}"
        clients[1].sendall(game_state.encode())

    except:
        break 

for conn in clients:
    conn.close()
server.close()
