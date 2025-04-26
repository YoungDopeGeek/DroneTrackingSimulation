# target.py
import pygame


class Target:
    def __init__(self, x, y):
        self.x = x #target position x
        self.y = y

    #draw circle target
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 10)
