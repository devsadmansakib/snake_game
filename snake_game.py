# importing...
import pygame
import random

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 36)
score = 0

# game state
PLAYING = 1
GAME_OVER = 2
game_state = PLAYING


# Colors
white = (255, 255, 255)


def generate_starting_position():
    x_position_range = (pixel_width // 2, screen_width - pixel_width // 2, pixel_width)
    y_position_range = (pixel_width // 2, screen_height - pixel_width // 2, pixel_width)
    return [random.randrange(*x_position_range), random.randrange(*y_position_range)]


def is_out_of_bounds():
    return (
        snake_pixel.bottom > screen_height
        or snake_pixel.top < 0
        or snake_pixel.left < 0
        or snake_pixel.right > screen_width
    )


def draw_score(score, message="Score: "):
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, [0, 0])


def show_game_over():
    lines = [
        f"Game Over!",
        f"Your Final Score is {score}.",
        f"Press R to restart or Q to quit.",
    ]
    y_offset = 0
    for line in lines:
        game_over_text = font.render(line, True, white)
        screen.blit(
            game_over_text,
            (screen_width // 2 - 200, screen_height // 2 - 100 + y_offset),
        )
        y_offset += 40


def reset_game():
    global pixel_width, snake_pixel, snake, snake_direction, snake_length, target
    snake_pixel = pygame.rect.Rect([0, 0, pixel_width, pixel_width])
    snake_pixel.center = generate_starting_position()
    snake = []
    snake_direction = (0, 0)
    snake_length = 1
    target = pygame.rect.Rect([0, 0, pixel_width, pixel_width])
    target.center = generate_starting_position()


# playground
pixel_width = 50
reset_game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_state == GAME_OVER:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_state = PLAYING
                    reset_game()
                elif event.key == pygame.K_q:
                    running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    if game_state == PLAYING:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            snake_direction = (0, -pixel_width)
        if keys[pygame.K_s]:
            snake_direction = (0, pixel_width)
        if keys[pygame.K_a]:
            snake_direction = (-pixel_width, 0)
        if keys[pygame.K_d]:
            snake_direction = (pixel_width, 0)

        snake_pixel.move_ip(snake_direction)
        snake.append(snake_pixel.copy())
        snake = snake[-snake_length:]

        if is_out_of_bounds():
            game_state = GAME_OVER

        if snake_pixel.center == target.center:
            target.center = generate_starting_position()
            snake_length += 1
            snake.append(snake_pixel.copy())
            score += 1

    if game_state == PLAYING:
        for snake_part in snake:
            pygame.draw.rect(screen, "green", snake_part)
        pygame.draw.rect(screen, "red", target)
        # Draw the score
        draw_score(score)
    elif game_state == GAME_OVER:
        draw_score(score, "Final Score: ")
        show_game_over()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(5)  # limits FPS to 60


pygame.quit()
