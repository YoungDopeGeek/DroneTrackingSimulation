# orbit.py
import math


def lerp(a, b, t):
    return a + (b - a) * t


class OrbitController:
    def __init__(self):
        self.orbit_radius = 80  # شعاع دایره (حالا این مقدار ثابت و دقیق است)

    def update(self, drone, target):
        # محاسبه فاصله بین پهباد و هدف
        dx = target.x - drone.x
        dy = target.y - drone.y
        distance = math.hypot(dx, dy)

        # هدف اینه که فاصله پهباد از هدف ثابت بمونه
        desired_angle = math.atan2(dy, dx)  # زاویه جهت هدف

        # محاسبه زاویه مداری پهباد نسبت به هدف
        orbit_angle = desired_angle + math.pi / 2  # چرخش به طور عمودی نسبت به زاویه هدف

        # فاصله بین پهباد و هدف باید برابر با شعاع مدنظر باشه
        scale_factor = self.orbit_radius / distance  # نسبت تغییر فاصله
        offset_x = dx * scale_factor  # تغییر در موقعیت x
        offset_y = dy * scale_factor  # تغییر در موقعیت y

        # موقعیت جدید پهباد در دایره حول هدف
        drone.x = target.x - offset_x
        drone.y = target.y - offset_y

        # تغییر زاویه برای حرکت در دایره به دور هدف
        drone.rotation = orbit_angle

        # تنظیم سرعت حرکت پهباد (اگر نیاز بود، این خط رو تغییر بده تا دقیق‌تر بشه)
        target_speed_x = math.cos(drone.rotation) * drone.max_speed
        target_speed_y = math.sin(drone.rotation) * drone.max_speed

        drone.speed_x = lerp(drone.speed_x, target_speed_x, 0.1)
        drone.speed_y = lerp(drone.speed_y, target_speed_y, 0.1)
