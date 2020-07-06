import pygame

def rozpocznij_gre():
  # inicjacja modułu pygame
  pygame.init()

  # tytuł okna gry
  pygame.display.set_caption('Prosty Pong')

  # powtarzalność klawiszy (delay, interval)
  pygame.key.set_repeat(50, 25)
