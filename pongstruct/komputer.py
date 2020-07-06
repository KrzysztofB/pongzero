#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def komputer_graj(gdzie_pilka, gdzie_wrog, gdzie_gracz, P_PREDKOSC_Y, PREDKOSC_AI):
      # AI (jak gra komputer)
    # jeżeli piłka ucieka na prawo, przesuń za nią paletkę
    if gdzie_pilka.centerx > gdzie_wrog.centerx:
        gdzie_wrog.x += PREDKOSC_AI
    # w przeciwnym wypadku przesuń w lewo
    elif gdzie_pilka.centerx < gdzie_wrog.centerx:
        gdzie_wrog.x -= PREDKOSC_AI

    # jeżeli piłka dotknie paletki AI, skieruj ją w przeciwną stronę
    if gdzie_pilka.colliderect(gdzie_wrog):
        P_PREDKOSC_Y *= -1
        # uwzględnij nachodzenie paletki na piłkę (przysłonięcie)
        gdzie_pilka.top = gdzie_wrog.bottom

    return P_PREDKOSC_Y
