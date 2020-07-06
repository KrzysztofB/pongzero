#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
from .wymiary import OKNOGRY_SZER, OKNOGRY_WYS
from .plansza import oknogry


# # powierzchnia do rysowania, czyli inicjacja okna gry
# oknogry = pygame.display.set_mode((OKNOGRY_SZER, OKNOGRY_WYS), 0, 32)

# piłka #################################################################
P_SZER = 20  # szerokość
P_WYS = 20  # wysokość
P_PREDKOSC_X = 4  # prędkość pozioma x
P_PREDKOSC_Y = 4  # prędkość pionowa y
GREEN = (0, 255, 0)  # kolor piłki



# utworzenie powierzchni piłki, narysowanie piłki i wypełnienie kolorem
grafika_pilka = pygame.Surface([P_SZER, P_WYS], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(grafika_pilka, GREEN, [0, 0, P_SZER, P_WYS])


# ustawienie prostokąta zawierającego piłkę w początkowej pozycji
gdzie_pilka = grafika_pilka.get_rect()
gdzie_pilka.x = OKNOGRY_SZER / 2
gdzie_pilka.y = OKNOGRY_WYS / 2