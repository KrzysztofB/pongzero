#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *

from .wymiary import OKNOGRY_SZER
from .paletka import gdzie_gracz, PALETKA_SZER


def obsluz_ruch_myszki(event):
  if event.type == MOUSEMOTION:
    myszaX, myszaY = event.pos  # współrzędne x, y kursora myszy
    # oblicz przesunięcie paletki gracza
    przesuniecie = myszaX - (PALETKA_SZER / 2)
    # jeżeli wykraczamy poza okno gry w prawo
    if przesuniecie > OKNOGRY_SZER - PALETKA_SZER:
      przesuniecie = OKNOGRY_SZER - PALETKA_SZER
      # jeżeli wykraczamy poza okno gry w lewo
    if przesuniecie < 0:
      przesuniecie = 0
      # zaktualizuj położenie paletki w poziomie
    gdzie_gracz.x = przesuniecie

def obsluz_klawiature(event):
# przechwyć naciśnięcia klawiszy kursora
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        gdzie_gracz.x -= 5
        if gdzie_gracz.x < 0:
            gdzie_gracz.x = 0
    if event.key == pygame.K_RIGHT:
        gdzie_gracz.x += 5
        if gdzie_gracz.x > OKNOGRY_SZER - PALETKA_SZER:
            gdzie_gracz.x = OKNOGRY_SZER - PALETKA_SZER

def obsluz_wyjscie(event):
  # przechwyć zamknięcie okna
  if event.type == QUIT:
    pygame.quit()
    sys.exit()

def obsluz_sterowanie(event):
  obsluz_wyjscie(event)
  obsluz_ruch_myszki(event)
  obsluz_klawiature(event)