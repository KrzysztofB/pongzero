#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *
from .paletka import grafika_gracz, gdzie_gracz, gdzie_wrog, grafika_wrog, PALETKA_SZER
from .wymiary import OKNOGRY_SZER, OKNOGRY_WYS, MOJE_PUNKTY, PUNKTY_KOMPUTERA, KOLOR_PLANSZY, FPS
from .pilka import gdzie_pilka, P_PREDKOSC_X, P_PREDKOSC_Y, grafika_pilka
from .punktacja import drukuj_punktyAI, drukuj_punkty1
from .plansza import oknogry
from .rozpoczecie import rozpocznij_gre
from .komputer import komputer_graj
from .obsluga import obsluz_sterowanie

rozpocznij_gre()

# ustawienia animacji ###################################################
fpsClock = pygame.time.Clock()  # zegar śledzący czas

# szybkość paletki AI
PREDKOSC_WROG = 5
SRODEK_X = OKNOGRY_SZER // 2
SRODEK_Y = OKNOGRY_WYS // 2

def lista_zdarzen():
  return pygame.event.get()

# pętla główna programu
while True:
    # obsługa zdarzeń generowanych przez gracza
    for event in lista_zdarzen():
        obsluz_sterowanie(event)

    # ruch piłki ########################################################
    # przesuń piłkę po obsłużeniu zdarzeń
    gdzie_pilka.move_ip(P_PREDKOSC_X, P_PREDKOSC_Y)

    # jeżeli piłka wykracza poza pole gry
    # z lewej/prawej – odwracamy kierunek ruchu poziomego piłki
    if gdzie_pilka.right >= OKNOGRY_SZER:
        P_PREDKOSC_X = -P_PREDKOSC_X
    if gdzie_pilka.left <= 0:
        P_PREDKOSC_X = -P_PREDKOSC_X

    if gdzie_pilka.top <= 0:  # piłka uciekła górą
        # P_PREDKOSC_Y *= -1  # odwracamy kierunek ruchu pionowego piłki
        gdzie_pilka.x = SRODEK_X  # więc startuję ze środka
        gdzie_pilka.y = SRODEK_Y
        MOJE_PUNKTY = str(int(MOJE_PUNKTY) + 1)

    if gdzie_pilka.bottom >= OKNOGRY_WYS:  # piłka uciekła dołem
        gdzie_pilka.x = SRODEK_X  # więc startuję ze środka
        gdzie_pilka.y = SRODEK_Y
        PUNKTY_KOMPUTERA = str(int(PUNKTY_KOMPUTERA) + 1)

    P_PREDKOSC_Y = komputer_graj(gdzie_pilka, gdzie_wrog, gdzie_gracz, P_PREDKOSC_Y, PREDKOSC_WROG)


    # jeżeli piłka dotknie paletki gracza, skieruj ją w przeciwną stronę
    if gdzie_pilka.colliderect(gdzie_gracz):
        P_PREDKOSC_Y = -P_PREDKOSC_Y
        # zapobiegaj przysłanianiu paletki przez piłkę
        gdzie_pilka.bottom = gdzie_gracz.top   




    # rysowanie obiektów ################################################
    oknogry.fill(KOLOR_PLANSZY)  # wypełnienie okna gry kolorem

    drukuj_punkty1(MOJE_PUNKTY)  # wyświetl punkty gracza
    drukuj_punktyAI(PUNKTY_KOMPUTERA)  # wyświetl punkty AI

    # narysuj w oknie gry paletki
    oknogry.blit(grafika_gracz, gdzie_gracz)
    oknogry.blit(grafika_wrog, gdzie_wrog)

    # narysuj w oknie piłkę
    oknogry.blit(grafika_pilka, gdzie_pilka)

    # zaktualizuj okno i wyświetl
    pygame.display.update()

    # zaktualizuj zegar po narysowaniu obiektów
    fpsClock.tick(FPS)

# KONIEC
