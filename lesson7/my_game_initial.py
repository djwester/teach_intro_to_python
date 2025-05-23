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
images["enemy"] = pygame.image.load("enemy.png")

balls = []
spaceTimer = 0
enemy_timer = 0
enemies = []


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def updateBall(self):
        self.y = self.y - 10


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def love(self):
        return True

    def update_enemy(self):
        self.y = self.y + 10


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
        if spaceTimer == 0:
            spaceTimer = 10
            ball = Ball(rect_x, rect_y - 10)
            balls.append(ball)

    if spaceTimer > 0:
        spaceTimer -= 1

    if enemy_timer == 0:
        enemy_timer = 30
        enemy = Enemy(0, 0)
        enemies.append(enemy)

    if enemy_timer > 0:
        enemy_timer -= 1

    for ball in balls:
        ball.updateBall()
        window.blit(images["ball"], (ball.x, ball.y))

    for enemy in enemies:
        enemy.update_enemy()
        window.blit(images["enemy"], (enemy.x, enemy.y))

    window.blit(images["tank"], (rect_x, rect_y))

    pygame.display.update()
