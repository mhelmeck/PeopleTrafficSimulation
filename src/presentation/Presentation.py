import pygame

from src.presentation.Board import Board
from src.presentation.Drawer import Drawer
from src.presentation.Pedestrian import Pedestrian
from src.presentation.PedestrianRepository import PedestrianRepository

is_finished = False

# Init and main loop
pygame.init()
pygame.display.set_caption("Presentation")
clock = pygame.time.Clock()

board = Board()
entrances = [x for x in board.board if (x[2] == 'Entrance')]
shops = [x for x in board.board if (x[2] == 'Shop')]

pedestrians = []
x = 1
for initial_spawn_point in entrances:
    pedestrians.append(Pedestrian(x, board, (initial_spawn_point[0], initial_spawn_point[1])))
    x = x + 1

pedRep = PedestrianRepository([pedestrians, 'Pedestrian Repo'])
drawer = Drawer(Board(), pedRep)

while not is_finished:
    # Get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_finished = True

    # pedRep.move_all()
    drawer.draw()

    pygame.display.flip()
    clock.tick(30)

# Exit
pygame.quit()
exit(0)
