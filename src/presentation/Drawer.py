import colorsys
import pygame


class Drawer:
    def __init__(self, board, ped_rep):
        self.ped_rep = ped_rep
        self.board = board
        self.screen = pygame.display.set_mode((self.board.max_width, self.board.max_height))
        self.blue_color = (0, 128, 255)
        self.red_color = (231, 76, 60)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self._draw_walls()
        # self._draw_pedestrians()
        self._draw_heat_map()

    def _heat_map_color_for_value(self, value):
        # max_val = max(self.board.visited_points)
        if value >= 255:
            value = 255
        return value, 0, 0

    def _draw_pedestrians(self):
        for pedestrian in self.ped_rep.pedestrians:
            pygame.draw.circle(self.screen, self.red_color, (pedestrian.x, pedestrian.y), 2)

    def _draw_walls(self):
        for point in self.board.board:
            pygame.draw.rect(self.screen, self.blue_color, pygame.Rect(point[0],
                                                                       point[1],
                                                                       self.board.min_width,
                                                                       self.board.min_height))

    def _draw_heat_map(self):
        for x in range(self.board.max_width):
            for y in range(self.board.max_height):
                visited_points = self.board.visited_points
                if visited_points[x][y] != 0:
                    color = self._heat_map_color_for_value(visited_points[x][y])
                    # print(color)
                    pygame.draw.rect(self.screen, color, pygame.Rect(x, y, self.board.min_width, self.board.min_height))
