# فایل اصلی برنامه که رابط کاربری را مدیریت می‌کند

import pygame
from drone import Drone
from target import Target
from follow_me import FollowMeController
from orbit import OrbitController

# مقداردهی اولیه Pygame
pygame.init()

# ایجاد پنجره با اندازه 800x600 پیکسل
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drone Simulation - Simple Version")

# ایجاد ساعت برای کنترل نرخ فریم
clock = pygame.time.Clock()

# تعریف رنگ‌ها
WHITE = (255, 255, 255)  # رنگ سفید برای پس‌زمینه

# تعریف محدودیت‌های صفحه
SCREEN_WIDTH = 800  # عرض صفحه
SCREEN_HEIGHT = 600  # ارتفاع صفحه
MARGIN = 20  # حاشیه امن از لبه‌های صفحه

# ایجاد اشیاء اولیه
# پهپاد در مرکز صفحه (400, 300)
drone = Drone(400, 300)
# هدف در موقعیت (200, 200)
target = Target(200, 200)
# شروع با کنترلر Follow Me
controller = FollowMeController()

# تعریف کلیدهای تغییر حالت
# کلید 1: حالت Follow Me
# کلید 2: حالت Orbit
MODES = {
    pygame.K_1: FollowMeController,
    pygame.K_2: OrbitController,
}

# حلقه اصلی بازی
running = True
while running:
    # محدود کردن نرخ فریم به 60 فریم در ثانیه
    dt = clock.tick(60)

    # بررسی رویدادها
    for event in pygame.event.get():
        # اگر کاربر پنجره را بست
        if event.type == pygame.QUIT:
            running = False

        # اگر کلیدی فشرده شد
        if event.type == pygame.KEYDOWN:
            # تغییر حالت کنترل
            if event.key in MODES:
                controller = MODES[event.key]()
                print(f"Switched to: {controller.__class__.__name__}")
            
            # ریست کردن شبیه‌سازی با کلید R
            if event.key == pygame.K_r:
                print("Resetting simulation...")
                drone = Drone(400, 300)
                target = Target(200, 200)
                controller = FollowMeController()

    # حرکت هدف با کلیدهای جهت‌نما
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        target.x = max(MARGIN, target.x - 5)  # حرکت به چپ با محدودیت
    if keys[pygame.K_RIGHT]:
        target.x = min(SCREEN_WIDTH - MARGIN, target.x + 5)  # حرکت به راست با محدودیت
    if keys[pygame.K_UP]:
        target.y = max(MARGIN, target.y - 5)  # حرکت به بالا با محدودیت
    if keys[pygame.K_DOWN]:
        target.y = min(SCREEN_HEIGHT - MARGIN, target.y + 5)  # حرکت به پایین با محدودیت

    # به‌روزرسانی و رسم
    drone.update(controller, target)  # به‌روزرسانی موقعیت پهپاد
    screen.fill(WHITE)  # پاک کردن صفحه
    drone.draw(screen)  # رسم پهپاد
    target.draw(screen)  # رسم هدف
    pygame.display.flip()  # به‌روزرسانی نمایش

# خروج از برنامه
pygame.quit() 