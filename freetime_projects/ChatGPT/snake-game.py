import pygame
import random
import sys
import numpy as np

# Initialize pygame
pygame.init()

# Window size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 150, 0)
RED = (255, 0, 0)
BG = (25, 25, 25)

# Clock & fonts
clock = pygame.time.Clock()
snake_size = 20
snake_speed = 12
font = pygame.font.SysFont("Arial", 28, bold=True)

# -----------------------------------------
# 🔊 SIMPLE BEEP SOUND GENERATOR
# -----------------------------------------
def generate_beep(frequency=500, duration=0.1):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration))
    waveform = 4096 * np.sin(2 * np.pi * frequency * t)
    sound_array = waveform.astype(np.int16)
    return pygame.sndarray.make_sound(sound_array)

eat_sound = generate_beep(600, 0.07)
gameover_sound = generate_beep(200, 0.3)
# -----------------------------------------

def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, DARK_GREEN, [x, y, snake_size, snake_size])

def message(text, color):
    msg = font.render(text, True, color)
    screen.blit(msg, (WIDTH/6, HEIGHT/3))

def game_loop():
    game_over = False
    game_close = False

    # Snake initial position
    x = WIDTH // 2
    y = HEIGHT // 2
    dx, dy = 0, 0

    snake = []
    snake_length = 1
    score = 0

    # Food random position
    food_x = round(random.randrange(0, WIDTH - snake_size) / 20) * 20
    food_y = round(random.randrange(0, HEIGHT - snake_size) / 20) * 20

    while not game_over:

        while game_close:
            screen.fill(BG)
            message("Game Over! Press C to Play Again or Q to Quit", RED)
            pygame.display.update()

            gameover_sound.play()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -snake_size; dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = snake_size; dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -snake_size; dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = snake_size; dx = 0

        # Move snake
        x += dx
        y += dy

        # Border collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        screen.fill(BG)

        # Draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_size, snake_size])

        # Snake movement
        snake_head = [x, y]
        snake.append(snake_head)

        if len(snake) > snake_length:
            del snake[0]

        # Self-collision
        if snake_head in snake[:-1]:
            game_close = True

        draw_snake(snake)
        show_score(score)
        pygame.display.update()

        # Food collision
        if x == food_x and y == food_y:
            eat_sound.play()
            score += 1
            snake_length += 1

            food_x = round(random.randrange(0, WIDTH - snake_size) / 20) * 20
            food_y = round(random.randrange(0, HEIGHT - snake_size) / 20) * 20

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

game_loop()
