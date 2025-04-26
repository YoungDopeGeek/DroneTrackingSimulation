# main.py
import pygame
from drone import Drone
from target import Target
from follow_me import FollowMeController
from orbit import OrbitController

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drone Simulation")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)

# Create objects
drone = Drone(400, 300)
target = Target(200, 200)
controller = FollowMeController()

# Mode switching
MODES = {
    pygame.K_1: FollowMeController,
    pygame.K_2: OrbitController,
}

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in MODES:
                controller = MODES[event.key]()
                print("Switched to", controller.__class__.__name__)
            if event.key == pygame.K_r:
                print("Resetting simulation...")
                drone = Drone(400, 300)
                target = Target(200, 200)
                controller = FollowMeController()

    # Move target with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        target.x -= 5
    if keys[pygame.K_RIGHT]:
        target.x += 5
    if keys[pygame.K_UP]:
        target.y -= 5
    if keys[pygame.K_DOWN]:
        target.y += 5

    # Update and draw
    drone.update(controller, target)

    screen.fill(WHITE)
    drone.draw(screen)
    target.draw(screen)

    pygame.display.flip()

pygame.quit()
