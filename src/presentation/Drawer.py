import pygame

from src.influx.InfluxService import InfluxService


class Drawer:
    def __init__(self, board, ped_rep, heat_map):
        self.board = board
        self.ped_rep = ped_rep
        self.heat_map = heat_map
        self.influx_service = InfluxService()
        self.screen = pygame.display.set_mode((self.board.max_width, self.board.max_height))
        self.blue_color = (0, 128, 255)
        self.red_color = (15, 15, 15)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self._draw_walls()
        self._draw_heat_map()
        self._draw_pedestrians_from_influx_data()

    def _draw_walls(self):
        for point in self.board.board:
            pygame.draw.rect(self.screen, self.blue_color, pygame.Rect(point[0],
                                                                       point[1],
                                                                       self.board.min_width,
                                                                       self.board.min_height))

    def _draw_pedestrians_from_simulation(self):
        for pedestrian in self.ped_rep.pedestrians:
            pygame.draw.circle(self.screen, self.red_color, (pedestrian.x, pedestrian.y), 4)

    def _draw_pedestrians_from_influx_data(self):
        for pedestrian in self.influx_service.get_all_ped_coords():
            pygame.draw.circle(self.screen, self.red_color, (pedestrian[0], pedestrian[1]), 4)

    def _draw_heat_map(self):
        self.heat_map.draw_at(self.screen)
