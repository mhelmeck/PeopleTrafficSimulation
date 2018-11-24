import pygame

# Properties
is_finished = False
blue_color = (0, 128, 255)
(builder_x, builder_y) = (0, 0)

# Methods
def set_new_position_when_pressed(x_pos, y_pos):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if y_pos >= 3:
            y_pos -= 3
    if pressed[pygame.K_DOWN]:
        if y_pos <= 380:
            y_pos += 3
    if pressed[pygame.K_LEFT]:
        if x_pos >= 3:
            x_pos -= 3
    if pressed[pygame.K_RIGHT]:
        if x_pos <= 380:
            x_pos += 3
    return x_pos, y_pos


# Init and main loop
pygame.init()
screen = pygame.display.set_mode((400, 400))
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
                                                     20,
                                                     20))
    # Render
    pygame.display.flip()
    clock.tick(60)


#if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#for point in points:
        #pygame.draw.rect(screen, color, pygame.Rect(point[0], point[1], 20, 20))