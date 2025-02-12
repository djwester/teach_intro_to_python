# mypy: ignore-errors
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

window = pygame.display.set_mode((WIDTH, HEIGHT))

rect_h = 25
rect_w = 25
rect_x = 0
rect_y = HEIGHT - rect_h

starting_ball_y = rect_y - rect_h

images = {}
images["tank"] = pygame.image.load("tank.png")
images["ball"] = pygame.image.load("red-ball.png")


def plot_balls(balls):
    updated_balls = []
    for ball in balls:
        window.blit(images["ball"], (ball["x"], ball["y"]))
        ball["y"] -= 10
        if ball["y"] > 0:
            updated_balls.append(ball)
    return updated_balls


balls = []
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

    window.fill((0, 0, 0))

    if keys[pygame.K_SPACE]:
        new_ball = {"x": rect_x, "y": rect_y - rect_h}
        balls.append(new_ball)

    ball = plot_balls(balls)

    window.blit(images["tank"], (rect_x, rect_y))

    pygame.display.update()
