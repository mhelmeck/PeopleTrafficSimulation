import pygame
import pickle
import random

# Properties
max_width = 400
max_height = 400
min_width = 1
min_height = 1
step = 5

sample_size = step
(sample_x, sample_y) = (200, 200)

is_finished = False
blue_color = (0, 128, 255)
red_color = (231, 76, 60)

with open("points.txt", "rb") as fp:
    board = pickle.load(fp)

# Methods
def should_move_to(nex_x, new_y):
    new_point = (nex_x, new_y)
    is_valid = False if new_point in board else True
    return is_valid

def set_new_position(direction, x_pos, y_pos):
    if direction == "N":
        if y_pos >= step and should_move_to(x_pos, y_pos - step):
            y_pos -= step
    if direction == "S":
        new_step = sample_size + step
        if y_pos <= max_height - new_step and should_move_to(x_pos, y_pos + step):
            y_pos += step
    if direction == "W":
        if x_pos >= step and should_move_to(x_pos - step, y_pos):
            x_pos -= step
    if direction == "E":
        new_step = sample_size + step
        if x_pos <= max_width - new_step and should_move_to(x_pos + step, y_pos):
            x_pos += step

    return x_pos, y_pos


def random_move(pos_x, pos_y):
    val = random.randint(1, 40)
    if val in range(1, 11):
        return set_new_position("N", pos_x, pos_y)
    if val in range(11, 21):
        return set_new_position("E", pos_x, pos_y)
    if val in range(21, 31):
        return set_new_position("S", pos_x, pos_y)
    if val in range(31, 41):
        return set_new_position("W", pos_x, pos_y)

    return pos_x, pos_y


# Init and main loop
pygame.init()
screen = pygame.display.set_mode((max_width, max_height))
pygame.display.set_caption("Presentation")
clock = pygame.time.Clock()

while not is_finished:
    # Get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_finished = True

    # Move
    (sample_x, sample_y) = random_move(sample_x, sample_y)

    # Draw
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, red_color, pygame.Rect(sample_x,
                                                    sample_y,
                                                    sample_size,
                                                    sample_size))

    for point in board:
        pygame.draw.rect(screen, blue_color, pygame.Rect(point[0],
                                                         point[1],
                                                         min_width,
                                                         min_height))
    # Render
    pygame.display.flip()
    clock.tick(30)

# Exit
pygame.quit()
exit(0)
