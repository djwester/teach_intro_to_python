# mypy: ignore-errors
import random

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

window = pygame.display.set_mode((WIDTH, HEIGHT))

rect_h = 25
rect_w = 25
rect_x = 0
rect_y = HEIGHT - rect_h

ball_step_size = 10

images = {}
images["tank"] = pygame.image.load("tank.png")
images["ball"] = pygame.image.load("red-ball.png")
images["enemy"] = pygame.image.load("enemy.png")

pygame.font.init()
game_over_font = pygame.font.SysFont("Arial", 50)
score_font = pygame.font.SysFont("Arial", 14)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        dimensions = images["ball"].get_rect()
        self.width = dimensions.width
        self.height = dimensions.height

    def update(self):
        self.y = self.y - ball_step_size

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Enemies:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        dimensions = images["enemy"].get_rect()
        self.width = dimensions.width
        self.height = dimensions.height

    def update(self):
        self.y = self.y + ball_step_size

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


balls = []
enemies = []
spaceTimer = 0
enemy_rate = 20
enemy_timer = 0
game_over = False
score = 0
level = 1
enemies_per_second = 0.5
delay = 100
time_since_last_enemy_created = 0

while True:
    pygame.time.delay(delay)
    time_since_last_enemy_created += delay
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
    if score % 10 == 0 and score != 0:
        level += 1
        score += 1
        enemies_per_second += 0.5

    if keys[pygame.K_SPACE]:
        if spaceTimer == 0:
            spaceTimer = 10
            new_ball = Ball(rect_x, rect_y - ball_step_size)
            balls.append(new_ball)

    if spaceTimer > 0:
        spaceTimer -= 1

    if time_since_last_enemy_created >= (delay*10)/enemies_per_second:
        x = random.randint(0, WIDTH)
        new_enemy = Enemies(x, 0)
        enemies.append(new_enemy)
        time_since_last_enemy_created = 0

    enemy_timer += 1

    ball_recs = []
    for ball in balls:
        if ball.y < 0:
            balls.remove(ball)
        ball.update()
        ball_recs.append(ball.get_rect())
        window.blit(images["ball"], (ball.x, ball.y))

    tank_rect = pygame.Rect(rect_x, rect_y, rect_w, rect_h)
    for enemy in enemies:
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
        if enemy.get_rect().collidelist(ball_recs) != -1:
            enemies.remove(enemy)
            score += 1
        enemy.update()
        window.blit(images["enemy"], (enemy.x, enemy.y))
        if enemy.get_rect().colliderect(tank_rect):
          game_over = True

    window.blit(images["tank"], (rect_x, rect_y))
    if keys[pygame.K_J]:
        window.blit(images["tank"], (100, 100))
    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    level_text = score_font.render(f"Level: {level}", True, (255, 255, 255))
    window.blit(level_text, (10, 30))

    if game_over:
        game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
        text_width = game_over_text.get_width()
        window.blit(
            game_over_text,
            ((WIDTH -text_width )// 2, HEIGHT // 2),
        )
        break
    
    pygame.display.update()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()   
