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

from src.influx.InfluxService import InfluxService


class Drawer:
    def __init__(self, board, heat_map):
        self.board = board
        self.heat_map = heat_map
        self.influx_service = InfluxService()
        self.screen = pygame.display.set_mode((self.board.max_width, self.board.max_height))
        self.wall_color = (44, 62, 80)
        self.pedestrian_color = (127, 140, 141)

    def draw(self):
        self.screen.fill((236, 240, 241))
        self._draw_walls()
        self._draw_heat_map()
        self._draw_pedestrians_from_influx_data()

    def _draw_walls(self):
        for point in self.board.board:
            pygame.draw.rect(self.screen, self.wall_color, pygame.Rect(point[0],
                                                                       point[1],
                                                                       self.board.min_width,
                                                                       self.board.min_height))

    def _draw_pedestrians_from_influx_data(self):
        for pedestrian in self.influx_service.get_all_ped_coordinates():
            pygame.draw.circle(self.screen, self.pedestrian_color, (pedestrian[0], pedestrian[1]), 4)
            self.heat_map.increment_for(pedestrian[0], pedestrian[1])

    def _draw_heat_map(self):
        self.heat_map.draw_at(self.screen)
