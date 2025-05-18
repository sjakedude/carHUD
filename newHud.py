import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Digital Dash")

font_large = pygame.font.SysFont("Courier", 72)
font_small = pygame.font.SysFont("Courier", 36)

clock = pygame.time.Clock()

def draw_fuel_bars(surface, fuel_level, x, y):
    total_bars = 10
    max_bar_width = 120
    bar_height = 10
    spacing = 4

    bars_to_draw = int((fuel_level / 100) * total_bars)

    for i in range(total_bars):
        if i < bars_to_draw:
            color = (0, 255, 0)  # Green for filled
        else:
            color = (40, 80, 40)  # Dim green for empty

        # Bars get wider as they go up
        bar_width = int((i + 1) / total_bars * max_bar_width)
        rect = pygame.Rect(x, y - (i * (bar_height + spacing)), bar_width, bar_height)
        pygame.draw.rect(surface, color, rect)

def draw_temp_bar(surface, temp_percent, x, y):
    pygame.draw.rect(surface, (100, 100, 100), (x, y, 30, 200))  # background
    fill_height = int((temp_percent / 100) * 200)
    pygame.draw.rect(surface, (255, 0, 0), (x, y + 200 - fill_height, 30, fill_height))  # temp bar

def draw_mph(surface, mph):
    text = font_large.render(f"{mph:.1f} MPH", True, (0, 255, 0))
    surface.blit(text, (250, 200))

def draw_tachometer(surface, rpm, max_rpm):
    width, _ = surface.get_size()
    tach_height = 40
    bar_width = int((rpm / max_rpm) * width)
    
    # Background bar (grey)
    pygame.draw.rect(surface, (50, 50, 50), (0, 0, width, tach_height))
    
    # Foreground bar (red)
    pygame.draw.rect(surface, (255, 0, 0), (0, 0, bar_width, tach_height))

    # RPM Text centered in tach
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"{int(rpm)} RPM", True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, tach_height // 2))
    surface.blit(text, text_rect)


running = True
while running:
    screen.fill((0, 0, 0))

    # Fake data for now
    mph = random.uniform(10, 30)
    fuel_percent = random.randint(0, 100)
    temp_percent = random.randint(0, 100)

    draw_mph(screen, mph)
    draw_temp_bar(screen, temp_percent, 740, 130)
    draw_fuel_bars(screen, fuel_percent, 20, 460)  # Bottom-left

    # Labels
    fuel_label = font_small.render("FUEL", True, (0, 255, 0))
    screen.blit(fuel_label, (20, 460 - 10 * (10 + 4) - 40))  # Moved above the top bar

    temp_label = font_small.render("TEMP", True, (255, 0, 0))
    screen.blit(temp_label, (700, 80))

    # Example: simulate RPM (replace this with actual OBD reading)
    current_rpm = 3500
    max_rpm = 7000

    draw_tachometer(screen, current_rpm, max_rpm)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
