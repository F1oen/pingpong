import socket
import threading
import pygame
import sys

# Network settings
SERVER_IP = '192.168.194.130'
SERVER_PORT = 5555

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Network Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_RADIUS = 10
FPS = 60

# Positions
player_id = 0
paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
opponent_y = paddle_y
ball_pos = [WIDTH // 2, HEIGHT // 2]

# Connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
player_id = int(client_socket.recv(1024).decode()[-1]) # "You are player X"
print(f"You are player {player_id}")

def receive():
    global opponent_y, ball_pos
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if data:
                parts = data.split(",")
                if len(parts) == 3:
                    opponent_y = int(parts[0])
                    ball_pos[0] = int(parts[1])
                    ball_pos[1] = int(parts[2])
        except:
            print("Connection lost.")
            break

threading.Thread(target=receive, daemon=True).start()

# Ball movement (only for Player 1)
ball_vel = [4, 4] if player_id == 1 else [0, 0]

clock = pygame.time.Clock()

def draw():
    WIN.fill(BLACK)
    # Paddles
    if player_id == 1:
        pygame.draw.rect(WIN, WHITE, (50, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(WIN, WHITE, (WIDTH - 65, opponent_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    else:
        pygame.draw.rect(WIN, WHITE, (50, opponent_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(WIN, WHITE, (WIDTH - 65, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    # Ball
    pygame.draw.circle(WIN, WHITE, (ball_pos[0], ball_pos[1]), BALL_RADIUS)
    pygame.display.update()

def move_ball():
    global ball_pos, ball_vel
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] *= -1
    if ball_pos[0] <= 0 or ball_pos[0] >= WIDTH:
        ball_pos = [WIDTH // 2, HEIGHT // 2] # Reset

while True:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    # Control paddle
    if keys[pygame.K_UP] and paddle_y > 0:
        paddle_y -= 5
    if keys[pygame.K_DOWN] and paddle_y < HEIGHT - PADDLE_HEIGHT:
        paddle_y += 5

    if player_id == 1:
        move_ball()

    # Send paddle position + ball position
    message = f"{paddle_y},{ball_pos[0]},{ball_pos[1]}"
    client_socket.send(message.encode())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw()