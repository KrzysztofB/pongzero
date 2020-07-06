#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *
from .wymiary import OKNOGRY_SZER, OKNOGRY_WYS
from .plansza import oknogry


def drukuj_punkty1(moje_punkty):
    fontObj = pygame.font.Font('freesansbold.ttf', 64)  # czcionka komunikatów
    tekst1 = fontObj.render(moje_punkty, True, (0, 0, 0))
    tekst_prost1 = tekst1.get_rect()
    tekst_prost1.center = (OKNOGRY_SZER / 2, OKNOGRY_WYS * 0.75)
    oknogry.blit(tekst1, tekst_prost1)

def drukuj_punktyAI(punkty_komputera):
    fontObj = pygame.font.Font('freesansbold.ttf', 64)  # czcionka komunikatów
    tekstAI = fontObj.render(punkty_komputera, True, (0, 0, 0))
    tekst_prostAI = tekstAI.get_rect()
    tekst_prostAI.center = (OKNOGRY_SZER / 2, OKNOGRY_WYS / 4)
    oknogry.blit(tekstAI, tekst_prostAI)