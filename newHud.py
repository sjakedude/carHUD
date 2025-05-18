import pygame
import sys

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Retro Digital Dash")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 128, 0)
WHITE = (255, 255, 255)

# Fonts
font_big = pygame.font.Font(None, 140)  # For MPG
font_small = pygame.font.Font(None, 40)  # For labels

# Dummy data (replace with real OBD data later)
mpg = 32.4
fuel_percent = 0.65  # 65% full
temp_percent = 0.50  # 50% hot

# Helper function to draw digital bar gauge
def draw_bar_gauge(x, y, width, height, percent, label):
    pygame.draw.rect(screen, DARK_GREEN, (x, y, width, height), 2)
    inner_width = int(width * percent)
    pygame.draw.rect(screen, GREEN, (x, y, inner_width, height))
    label_surface = font_small.render(label, True, GREEN)
    screen.blit(label_surface, (x, y - 30))

# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display MPG
    mpg_text = font_big.render(f"{mpg:.1f} MPG", True, GREEN)
    screen.blit(mpg_text, (200, 50))

    # Fuel gauge
    draw_bar_gauge(100, 250, 600, 30, fuel_percent, "FUEL")

    # Temp gauge
    draw_bar_gauge(100, 320, 600, 30, temp_percent, "TEMP")

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()