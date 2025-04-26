# target.py
# This file defines the Target class

import pygame

class Target:
    def __init__(self, x, y):
        """
        Create a new target
        x: horizontal position
        y: vertical position
        """
        # Store target position
        self.x = x
        self.y = y

    def draw(self, screen):
        """
        Draw target as a red circle
        screen: surface to draw on
        """
        # Draw red circle with radius 10 pixels
        # Convert coordinates to integers because pygame only accepts integers
        pygame.draw.circle(
            screen,           # Drawing surface
            (255, 0, 0),     # Red color (RGB)
            (int(self.x), int(self.y)),  # Circle center
            10               # Circle radius
        ) 