import pygame
import pickle

# Properties
max_width = 400
max_height = 400
min_width = 1
min_height = 1
step = 5

builder_size = 10
(builder_x, builder_y) = (0, 0)

is_finished = False
is_building = False
blue_color = (0, 128, 255)
red_color = (231, 76, 60)

points = []

# Methods
def set_new_position(x_pos, y_pos):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if y_pos >= step:
            y_pos -= step
    if pressed[pygame.K_DOWN]:
        if y_pos <= max_height - builder_size - step:
            y_pos += step
    if pressed[pygame.K_LEFT]:
        if x_pos >= step:
            x_pos -= step
    if pressed[pygame.K_RIGHT]:
        if x_pos <= max_width - builder_size - step:
            x_pos += step
    return x_pos, y_pos


def build():
    for x in range(builder_size):
        for y in range(builder_size):
            new_point = (builder_x + x, builder_y + y)
            if new_point not in points:
                points.append(new_point)


# Init and main loop
pygame.init()
screen = pygame.display.set_mode((max_width, max_height))
pygame.display.set_caption("Board builder")
clock = pygame.time.Clock()

while not is_finished:
    # Get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_building = not is_building

    # Move
    (builder_x, builder_y) = set_new_position(builder_x, builder_y)
    if is_building:
        build()

    # Draw
    screen.fill((0, 0, 0))
    color = red_color if is_building else blue_color
    pygame.draw.rect(screen, color, pygame.Rect(builder_x,
                                                builder_y,
                                                builder_size,
                                                builder_size))
    for point in points:
        pygame.draw.rect(screen, color, pygame.Rect(point[0],
                                                    point[1],
                                                    min_width,
                                                    min_height))
    # Render
    pygame.display.flip()
    clock.tick(30)

# Save data to file
with open("points.txt", "wb") as fp:
    pickle.dump(points, fp)

# Exit
pygame.quit()
exit(0)
