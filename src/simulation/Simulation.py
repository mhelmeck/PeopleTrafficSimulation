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

from src.common.Board import Board
from src.simulation.Pedestrian import Pedestrian
from src.simulation.PedestrianRepository import PedestrianRepository

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (236, 240, 241)
red = (192, 57, 43)
green = (39, 174, 96)
bright_red = (231, 76, 60)
bright_green = (46, 204, 113)
loading_icon = pygame.image.load('assets/saving_to_influx.png')
pygame.display.set_icon(loading_icon)

saving_simulation_results = False

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PeopleTrafficSimulation')
clock = pygame.time.Clock()

board = Board()
entrances = [x for x in board.board if (x[2] == 'Entrance')]
shops = [x for x in board.board if (x[2] == 'Shop')]

pedestrians = []
uuid = 0
for i, shop in enumerate(shops):
    if i % 3 == 0:
        pedestrians.append(Pedestrian(uuid, board, (shop[0], shop[1])))
        uuid += 1

pedRep = PedestrianRepository([pedestrians, 'Pedestrian Repo'])


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(text_surf, text_rect)


def text_field(font_name, font_size, text, x, y):
    large_text = pygame.font.Font(font_name, font_size)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = (x, y)
    gameDisplay.blit(text_surf, text_rect)


def stop_simulation():
    pygame.quit()
    quit()


def game_intro():
    intro = True

    def turn_on_saving():
        global saving_simulation_results
        saving_simulation_results = True

    def turn_off_saving():
        global saving_simulation_results
        saving_simulation_results = False

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_simulation()

        gameDisplay.fill(white)
        text_field('freesansbold.ttf', 60, "Simulation", (display_width / 2), (display_height / 8))

        button("Save to Influx", 150, 450, 150, 50, bright_green, green, turn_on_saving)
        button("OFF", 300, 450, 50, 50, bright_red, red, turn_off_saving)
        button("EXIT", 500, 450, 150, 50, bright_red, red, stop_simulation)

        if saving_simulation_results:
            gameDisplay.blit(loading_icon, ((display_width / 8), (display_height / 3)))
            pedRep.move_all()
        pygame.display.update()
        clock.tick(30)


game_intro()
stop_simulation()
