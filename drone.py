# drone.py
import pygame
import math


class Drone:
    def __init__(self, x, y):
        self.x = x #drone position x
        self.y = y #drone position y
        self.speed_x = 0 #drone speed x
        self.speed_y = 0 #drone speed y
        self.rotation = 0  # Radians
        self.max_speed = 5 #max speed of drone

    #update drone position
    def update(self, controller, target):       
        controller.update(self, target)

        self.x += self.speed_x
        self.y += self.speed_y

    #draw triangle drone
    def draw(self, screen):
        points = [
            (
                self.x + 15 * math.cos(self.rotation),
                self.y + 15 * math.sin(self.rotation),
            ),
            (
                self.x + 10 * math.cos(self.rotation + 2.5),
                self.y + 10 * math.sin(self.rotation + 2.5),
            ),
            (
                self.x + 10 * math.cos(self.rotation - 2.5),
                self.y + 10 * math.sin(self.rotation - 2.5),
            ),
        ]
        pygame.draw.polygon(screen, (0, 0, 255), points)
