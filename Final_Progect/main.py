import pygame
import numpy as np
import random


# Ball - это класс, описывающий отдельный шарик
class Ball:
	def __init__(self):
		# radius >= 2
		self.radius = 2
		self.delta = 5 + self.radius * 0.5
		self.position_x = random.randrange(0 + self.delta, width - self.delta)
		self.position_y = random.randrange(0 + self.delta, height - self.delta)
		self.velocity_x = random.randrange(-100, 100)
		self.velocity_y = random.randrange(-100, 100)


pygame.init()
# Задаём размеры окна
size = width, height = 1000, 750
n_balls = 1000  # Задаём количество шариков
screen = pygame.display.set_mode(size)

color = 255, 255, 255
delta_t = 0.1

balls = np.array([])

# Создаём массив шариков
for i in range(n_balls):
	balls = np.append(balls, Ball())

run = True
while run:
	pygame.time.delay(50)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	screen.fill((0, 0, 0))

	for i in range(n_balls):
		balls[i].position_x += balls[i].velocity_x * delta_t
		balls[i].position_y += balls[i].velocity_y * delta_t

		if balls[i].position_x - balls[i].radius < 0:
			balls[i].velocity_x *= -1
		if balls[i].position_x + balls[i].radius > width:
			balls[i].velocity_x *= -1
		if balls[i].position_y - balls[i].radius < 0:
			balls[i].velocity_y *= -1
		if balls[i].position_y + balls[i].radius > height:
			balls[i].velocity_y *= -1

		pygame.draw.circle(screen, color, (balls[i].position_x, balls[i].position_y), balls[i].radius)

	pygame.display.update()

pygame.quit()
