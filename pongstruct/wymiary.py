#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *

# szerokość i wysokość okna gry
OKNOGRY_SZER = 800
OKNOGRY_WYS = 400


# komunikaty tekstowe ###################################################
# zmienne przechowujące punkty i funkcje wyświetlające punkty
MOJE_PUNKTY = '0'
PUNKTY_KOMPUTERA = '0'

# kolor okna gry, składowe RGB zapisane w tupli
KOLOR_PLANSZY = (230, 255, 255)

FPS = 30  # liczba klatek na sekundę


