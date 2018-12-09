import time

import pygame

from src.presentation.Board import Board
from src.presentation.Pedestrian import Pedestrian
from src.presentation.PedestrianRepository import PedestrianRepository

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
x = 1
for initial_spawn_point in entrances:
    pedestrians.append(Pedestrian(x, board, (initial_spawn_point[0], initial_spawn_point[1])))
    x = x + 1

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

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


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
            # print(event)
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
