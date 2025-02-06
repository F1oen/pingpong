import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game settings
paddle_width, paddle_height = 20, 100
ball_size = 15

# Paddle positions
paddle1_y = paddle2_y = HEIGHT // 2 - paddle_height // 2
paddle_speed = 7

# Ball position and speed
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 5, 5

# Scores
score1, score2 = 0, 0

# Game loop
running = True
while running:
    pygame.time.delay(16)  # Control frame rate (~60 FPS)
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < HEIGHT - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - paddle_height:
        paddle2_y += paddle_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top/bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (ball_x <= 50 and paddle1_y < ball_y < paddle1_y + paddle_height) or \
       (ball_x >= WIDTH - 50 - ball_size and paddle2_y < ball_y < paddle2_y + paddle_height):
        ball_speed_x *= -1  # Reverse direction

    # Scoring system
    if ball_x < 0:  # Player 2 scores
        score2 += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x *= -1
    if ball_x > WIDTH:  # Player 1 scores
        score1 += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x *= -1

    # Draw paddles, ball, and scoreboard
    pygame.draw.rect(screen, WHITE, (50, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (WIDTH - 50 - paddle_width, paddle2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display scores
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 20, 20))

    # Refresh screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
