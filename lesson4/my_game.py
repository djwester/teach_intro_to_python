# mypy: ignore-errors
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

window = pygame.display.set_mode((WIDTH, HEIGHT))

rect_x = 0
rect_y = 0
rect_h = 10
rect_w = 10
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect_x -= 10
    if keys[pygame.K_RIGHT]:
        rect_x += 10
    if keys[pygame.K_UP]:
        rect_y -= 10
    if keys[pygame.K_DOWN]:
        rect_y += 10
    pygame.draw.rect(window, (255, 0, 0), (rect_x, rect_y, rect_h, rect_w))
    pygame.display.update()
