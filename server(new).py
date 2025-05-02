import socket

# Server settings
SERVER_IP = '0.0.0.0'
SERVER_PORT = 5555
BUFFER_SIZE = 1024

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(2)

print(f"[SERVER STARTED] Waiting for connections on {SERVER_IP}:{SERVER_PORT}")

players = []

# Wait for two players to connect
while len(players) < 2:
    conn, addr = server_socket.accept()
    print(f"[CONNECTED] {addr} joined the game.")
    players.append(conn)
    conn.send(str.encode(f"You are player {len(players)}"))

# Simple message exchange between players
while True:
    try:
        for i, conn in enumerate(players):
            data = conn.recv(BUFFER_SIZE).decode()
            if data:
                print(f"[PLAYER {i+1}] {data}")
                # Send data to the other player
                other = players[1] if i == 0 else players[0]
                other.send(str.encode(data))
    except:
        print("Connection lost.")
        break

server_socket.close()
