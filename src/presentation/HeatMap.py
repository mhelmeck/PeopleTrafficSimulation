#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Artur Siepietowski
# Copyright 2018 Maciej Hełmecki
#
# This file is part of PeopleTrafficSimulation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import pygame


class HeatMap:
    def __init__(self, max_width, max_height):
        self.max_width = max_width
        self.max_height = max_height
        self.radius = 2
        self.increment_value = 1
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

    # noinspection PyMethodMayBeStatic
    def _color_for_value_by_fraction(self, value):
        max_value = max(max(self.visited_points))
        fraction = value / max_value
        print(fraction)

        if fraction < 0.25:
            return 16, 20, 248
        if fraction in (0.25, 0.5):
            return 99, 250, 43
        if fraction in (0.5, 0.75):
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
                    color = self._color_for_value_by_fraction(self.visited_points[x][y])
                    pygame.draw.rect(screen, color, pygame.Rect(x, y, 1, 1))
