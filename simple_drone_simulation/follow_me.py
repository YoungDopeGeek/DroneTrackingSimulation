# این فایل کنترلر Follow Me را تعریف می‌کند

import math

class FollowMeController:
    def __init__(self):
        """
        ایجاد یک کنترلر Follow Me
        """
        # فاصله مطلوب از هدف (50 واحد)
        self.target_distance = 50
        
        # ناحیه مرده (10 واحد)
        # پهپاد در این ناحیه حرکت نمی‌کند
        # از نوسانات کوچک جلوگیری می‌کند
        self.dead_zone = 10

    def update(self, drone, target):
        """
        به‌روزرسانی موقعیت و جهت پهپاد برای دنبال کردن هدف
        drone: پهپادی که باید کنترل شود
        target: هدفی که باید دنبال شود
        """
        # محاسبه فاصله تا هدف
        dx = target.x - drone.x  # فاصله افقی
        dy = target.y - drone.y  # فاصله عمودی
        distance = math.hypot(dx, dy)  # فاصله مستقیم (با استفاده از قضیه فیثاغورث)

        # اگر فاصله بیشتر از مقدار مطلوب باشد
        if distance > self.target_distance + self.dead_zone:
            # محاسبه زاویه به سمت هدف
            # atan2 زاویه بین -π و π را برمی‌گرداند
            angle = math.atan2(dy, dx)

            # محاسبه تفاوت بین زاویه فعلی و زاویه مطلوب
            # این فرمول تفاوت را بین -π و π نگه می‌دارد
            diff = (angle - drone.rotation + math.pi) % (2 * math.pi) - math.pi
            
            # چرخش نرم به سمت هدف
            # ضریب 0.15 چرخش را ملایم می‌کند
            drone.rotation += diff * 0.15

            # محاسبه سرعت در هر دو محور
            # کسینوس برای سرعت افقی
            # سینوس برای سرعت عمودی
            drone.speed_x = math.cos(drone.rotation) * drone.max_speed
            drone.speed_y = math.sin(drone.rotation) * drone.max_speed
        else:
            # اگر فاصله مناسب باشد، پهپاد را متوقف کن
            drone.speed_x = 0
            drone.speed_y = 0 