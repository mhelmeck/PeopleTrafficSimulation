import pygame

max_width = 800
max_height = 200
min_width = 1
min_height = 1

class Drawer:
    screen = pygame.display.set_mode((max_width, max_height))
    blue_color = (0, 128, 255)
    red_color = (231, 76, 60)

    def __init__(self, board, ped_rep):
        self.ped_rep = ped_rep
        self.board = board

    def draw(self):
        self.screen.fill((0, 0, 0))
        self._draw_walls()
        self._draw_pedestrians()

    def _draw_pedestrians(self):
        for pedestrian in self.ped_rep.pedestrians:
            pygame.draw.circle(self.screen, self.red_color, (pedestrian.x, pedestrian.y), 2)

    def _draw_walls(self):
        for point in self.board.board:
            pygame.draw.rect(self.screen, self.blue_color, pygame.Rect(point[0],
                                                                       point[1],
                                                                       min_width,
                                                                       min_height))
