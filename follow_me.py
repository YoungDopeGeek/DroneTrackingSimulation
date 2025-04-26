# follow_me.py
import math


class FollowMeController:
    def __init__(self):
        self.target_distance = 50 #target distance
        self.dead_zone = 10

    def update(self, drone, target):
        dx = target.x - drone.x #difference x
        dy = target.y - drone.y #difference y
        distance = math.hypot(dx, dy) #strait distance between drone and target

        if distance > self.target_distance + self.dead_zone:
            angle = math.atan2(dy, dx) #angle between drone and target

            # Smooth rotation toward target
            diff = (angle - drone.rotation + math.pi) % (2 * math.pi) - math.pi #difference between drone and target
            drone.rotation += diff * 0.15 #rotation of drone

            drone.speed_x = math.cos(drone.rotation) * drone.max_speed #speed x of drone
            drone.speed_y = math.sin(drone.rotation) * drone.max_speed #speed y of drone
        else:
            drone.speed_x = 0 #speed x of drone
            drone.speed_y = 0 #speed y of drone
