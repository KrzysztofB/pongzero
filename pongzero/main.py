#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pgzrun
from pgzero import *


# from pongzero.wymiary import OKNOGRY_SZER, OKNOGRY_WYS, MOJE_PUNKTY, PUNKTY_KOMPUTERA, KOLOR_PLANSZY, FPS

WIDTH = 800 #OKNOGRY_SZER
HEIGHT = 600 #OKNOGRY_WYS

#while gra_trwa():
  #input
  #update
  #draw

def draw():
  #screen.fill(KOLOR_PLANSZY)
  screen.clear()
  screen.draw.circle((400, 300), 30, 'white')

# ta linia na koncu
pgzrun.go()