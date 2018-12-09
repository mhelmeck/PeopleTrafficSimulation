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

from src.presentation.Board import Board
from src.presentation.Drawer import Drawer
from src.presentation.HeatMap import HeatMap
from src.presentation.Pedestrian import Pedestrian
from src.presentation.PedestrianRepository import PedestrianRepository

is_finished = False

# Init and main loop
pygame.init()
pygame.display.set_caption("Presentation")
clock = pygame.time.Clock()

board = Board()
heat_map = HeatMap(board.max_width, board.max_height)
entrances = [x for x in board.board if (x[2] == 'Entrance')]
shops = [x for x in board.board if (x[2] == 'Shop')]

pedestrians = []
x = 1
for initial_spawn_point in entrances:
    pedestrians.append(Pedestrian(x, board, heat_map, (initial_spawn_point[0], initial_spawn_point[1])))
    x = x + 1

ped_rep = PedestrianRepository([pedestrians, 'Pedestrian Repo'])
drawer = Drawer(board, ped_rep, heat_map)

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
