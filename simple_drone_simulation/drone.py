# drone.py
# This file defines the Drone class

import pygame
import math

class Drone:
    def __init__(self, x, y):
        # Initial position
        self.x = x  # Horizontal position
        self.y = y  # Vertical position
        
        # Movement speed
        self.speed_x = 0  # Horizontal speed
        self.speed_y = 0  # Vertical speed
        
        # Movement direction (in radians)
        # 0 radians = right
        # π/2 radians = up
        # π radians = left
        # 3π/2 radians = down
        self.rotation = 0
        
        # Maximum movement speed
        self.max_speed = 5

    def update(self, controller, target):
        """
        Update drone's position and direction
        controller: current controller (FollowMe or Orbit)
        target: target to follow
        """
        # Ask controller to calculate new position
        controller.update(self, target)
        
        # Update position based on speed
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, screen):
        """
        Draw drone as a triangle
        screen: surface to draw on
        """
        # Calculate coordinates of three triangle points
        # First point: tip of triangle (15 units in rotation direction)
        # Second and third points: back corners (10 units at ±2.5 radians)
        points = [
            # Triangle tip
            (
                self.x + 15 * math.cos(self.rotation),
                self.y + 15 * math.sin(self.rotation),
            ),
            # Right corner
            (
                self.x + 10 * math.cos(self.rotation + 2.5),
                self.y + 10 * math.sin(self.rotation + 2.5),
            ),
            # Left corner
            (
                self.x + 10 * math.cos(self.rotation - 2.5),
                self.y + 10 * math.sin(self.rotation - 2.5),
            ),
        ]
        
        # Draw blue triangle
        pygame.draw.polygon(screen, (0, 0, 255), points) 