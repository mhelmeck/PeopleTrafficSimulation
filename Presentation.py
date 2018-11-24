import pygame
import pickle

# Properties
max_width = 400
max_height = 400
min_width = 1
min_height = 1
step = 10

is_finished = False
blue_color = (0, 128, 255)

with open("points.txt", "rb") as fp:
    points = pickle.load(fp)

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

    # Draw
    screen.fill((0, 0, 0))
    for point in points:
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
