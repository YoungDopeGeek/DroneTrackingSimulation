# این فایل کنترلر Orbit را تعریف می‌کند

import math
import random

def lerp(a, b, t):
    """
    محاسبه مقدار میانی بین دو عدد
    a: عدد اول
    b: عدد دوم
    t: نسبت (بین 0 و 1)
    مثال: lerp(0, 10, 0.5) = 5
    """
    return a + (b - a) * t

class OrbitController:
    def __init__(self):
        """
        ایجاد یک کنترلر Orbit
        """
        # شعاع مدار (80 واحد)
        self.orbit_radius = 80
        
        # زاویه فعلی در مدار (برای حرکت نرم)
        self.current_angle = 0
        
        # افزایش سرعت زاویه‌ای (برای حرکت سریع‌تر)
        self.angular_speed = 0.04
        
        # نوسان طبیعی در مدار
        self.orbit_oscillation = 0
        self.oscillation_speed = 0.05
        self.max_oscillation = 5

    def update(self, drone, target):
        """
        به‌روزرسانی موقعیت و جهت پهپاد برای گردش به دور هدف
        drone: پهپادی که باید کنترل شود
        target: هدفی که باید دور آن بچرخد
        """
        # به‌روزرسانی زاویه مدار
        self.current_angle += self.angular_speed
        
        # محاسبه نوسان طبیعی
        self.orbit_oscillation = math.sin(self.current_angle * 2) * self.max_oscillation
        
        # محاسبه شعاع مؤثر با در نظر گرفتن نوسان
        effective_radius = self.orbit_radius + self.orbit_oscillation
        
        # محاسبه موقعیت جدید در مدار
        orbit_x = target.x + effective_radius * math.cos(self.current_angle)
        orbit_y = target.y + effective_radius * math.sin(self.current_angle)
        
        # محاسبه فاصله تا موقعیت مطلوب
        dx = orbit_x - drone.x
        dy = orbit_y - drone.y
        distance = math.hypot(dx, dy)
        
        # محاسبه سرعت مطلوب با در نظر گرفتن فاصله
        # افزایش ضریب سرعت برای حرکت سریع‌تر
        target_speed = min(distance * 0.3, drone.max_speed)
        
        # محاسبه زاویه حرکت
        move_angle = math.atan2(dy, dx)
        
        # محاسبه سرعت در هر محور
        target_speed_x = math.cos(move_angle) * target_speed
        target_speed_y = math.sin(move_angle) * target_speed
        
        # تغییر نرم سرعت با استفاده از تابع lerp
        # افزایش ضریب تغییر سرعت برای واکنش سریع‌تر
        drone.speed_x = lerp(drone.speed_x, target_speed_x, 0.15)
        drone.speed_y = lerp(drone.speed_y, target_speed_y, 0.15)
        
        # محاسبه زاویه به سمت هدف
        angle = math.atan2(target.y - drone.y, target.x - drone.x)
        
        # محاسبه تفاوت بین زاویه فعلی و زاویه مطلوب
        diff = (angle - drone.rotation + math.pi) % (2 * math.pi) - math.pi
        
        # چرخش نرم به سمت هدف
        drone.rotation += diff * 0.2 