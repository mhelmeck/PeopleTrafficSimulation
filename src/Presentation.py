import pygame

from src.Board import Board
from src.Pedestrian import Pedestrian
from src.PedestrianRepository import PedestrianRepository

max_width = 800
max_height = 200
min_width = 1
min_height = 1

is_finished = False
blue_color = (0, 128, 255)
red_color = (231, 76, 60)

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

    board = Board()

    # Move
    x = Pedestrian(1, board, (2, 4))
    y = Pedestrian(2, board, (5, 10))
    z = Pedestrian(2, board, (5, 10))

    pedRep = PedestrianRepository([[x, y, z], 'Pedestrian Repo'])
    pedRep.move_all()



    # Draw
    screen.fill((0, 0, 0))
    for pedestrian in pedRep.pedestrians:
        pygame.draw.rect(screen, red_color, pygame.Rect(pedestrian.x,
                                                        pedestrian.y,
                                                        pedestrian.size,
                                                        pedestrian.size))

    for point in board.board:
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
