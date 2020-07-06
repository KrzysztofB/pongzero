#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *
from .wymiary import OKNOGRY_SZER, OKNOGRY_WYS


# powierzchnia do rysowania, czyli inicjacja okna gry
oknogry = pygame.display.set_mode((OKNOGRY_SZER, OKNOGRY_WYS), 0, 32)

