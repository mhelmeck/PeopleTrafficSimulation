import pygame


class HeatMap:
    def __init__(self, max_width, max_height):
        self.max_width = max_width
        self.max_height = max_height
        self.radius = 2
        self.increment_value = 3
        self.visited_points = [[0 for _ in range(self.max_height)] for _ in range(self.max_width)]

    # Private methods
    def _increment_if_possible_for(self, new_x, new_y):
        if new_x in range(0, self.max_width):
            if new_y in range(0, self.max_height):
                self.visited_points[new_x][new_y] += self.increment_value

    # noinspection PyMethodMayBeStatic
    def _color_for_value(self, value):
        if value in range(0, 25):
            return 16, 20, 248
        if value in range(25, 50):
            return 99, 250, 43
        if value in range(50, 75):
            return 235, 137, 35

        return 227, 35, 27

    # Public methods
    def increment_for(self, x, y):
        for i in range(x - self.radius, x + self.radius):
            for j in range(y - self.radius, y + self.radius):
                self._increment_if_possible_for(i, j)

    def draw_at(self, screen):
        for x in range(self.max_width):
            for y in range(self.max_height):
                if self.visited_points[x][y] != 0:
                    color = self._color_for_value(self.visited_points[x][y])
                    pygame.draw.rect(screen, color, pygame.Rect(x, y, 1, 1))