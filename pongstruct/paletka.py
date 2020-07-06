#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *


PALETKA_SZER = 100  # szerokość
PALETKA_WYS = 20  # wysokość


# paletka gracza #########################################################
BLUE = (0, 0, 255)  # kolor wypełnienia
GDZIE_GRACZ_POZ = (350, 360)  # początkowa pozycja zapisana w tupli

# utworzenie powierzchni paletki, wypełnienie jej kolorem,
grafika_gracz = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
grafika_gracz.fill(BLUE)
# ustawienie prostokąta zawierającego paletkę w początkowej pozycji
gdzie_gracz = grafika_gracz.get_rect()
gdzie_gracz.x = GDZIE_GRACZ_POZ[0]
gdzie_gracz.y = GDZIE_GRACZ_POZ[1]

# paletka ai ############################################################
RED = (255, 0, 0)
GDZIE_WROG_POZ = (350, 20)  # początkowa pozycja zapisana w tupli
# utworzenie powierzchni paletki, wypełnienie jej kolorem,
grafika_wrog = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
grafika_wrog.fill(RED)
# ustawienie prostokąta zawierającego paletkę w początkowej pozycji
gdzie_wrog = grafika_wrog.get_rect()
gdzie_wrog.x = GDZIE_WROG_POZ[0]
gdzie_wrog.y = GDZIE_WROG_POZ[1]
# szybkość paletki AI
PREDKOSC_WROG = 5