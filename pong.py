import pygame

pygame.init()
running = True
WINDOW_WIDTH = 800
WINDOW_HEGIHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEGIHT))
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()