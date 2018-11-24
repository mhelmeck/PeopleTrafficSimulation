import pygame

# Properties
max_width = 400
max_height = 400
step = 3

builder_size = 20
(builder_x, builder_y) = (0, 0)

is_finished = False
blue_color = (0, 128, 255)

# Methods
def set_new_position_when_pressed(x_pos, y_pos):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if y_pos >= step:
            y_pos -= step
    if pressed[pygame.K_DOWN]:
        if y_pos <= max_height - builder_size:
            y_pos += step
    if pressed[pygame.K_LEFT]:
        if x_pos >= step:
            x_pos -= step
    if pressed[pygame.K_RIGHT]:
        if x_pos <= max_width - builder_size:
            x_pos += step
    return x_pos, y_pos


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

    # Move
    (builder_x, builder_y) = set_new_position_when_pressed(builder_x, builder_y)

    # Draw
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, blue_color, pygame.Rect(builder_x,
                                                     builder_y,
                                                     builder_size,
                                                     builder_size))
    # Render
    pygame.display.flip()
    clock.tick(60)
