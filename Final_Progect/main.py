import pygame
import numpy as np
import random

wall_width = 20

# Ball - это класс, описывающий отдельный шарик
class Ball_l:
	def __init__(self):
		# radius >= 2
		self.radius = 2
		self.delta = 5 + self.radius * 0.5
		self.position_x = random.randrange(0 + self.delta, width / 2 - wall_width - self.delta)
		self.position_y = random.randrange(0 + self.delta, height - self.delta)
		self.velocity_x = random.randrange(-100, 100)
		self.velocity_y = random.randrange(-100, 100)
		self.m = 10


class Ball_r:
	def __init__(self):
		# radius >= 2
		self.radius = 2
		self.delta = 5 + self.radius * 0.5
		self.position_x = random.randrange(width / 2 + wall_width + self.delta, width - self.delta)
		self.position_y = random.randrange(0 + self.delta, height - self.delta)
		self.velocity_x = random.randrange(-100, 100)
		self.velocity_y = random.randrange(-100, 100)
		self.m = 10


class Rect:
	def __init__(self):
		self.width = wall_width
		self.height = height
		self.x = (width / 2) - (self.width / 2)
		self.y = 0
		self.m = 100


	def move(self, x, y):
		self.x += x
		self.y += y

	def get_right_coord(self):
		return self.x + self.width

	def get_left_coord(self):
		return self.x


pygame.init()
# Задаём размеры окна
size = width, height = 1000, 750
n_balls = 10000  # Задаём количество шариков
screen = pygame.display.set_mode(size)

color = 255, 255, 255
delta_t = 0.1

balls_l = np.array([])
balls_r = np.array([])


# Создаём массив шариков
for i in range(n_balls):
	balls_l = np.append(balls_l, Ball_l())

for i in range(n_balls):
	balls_r = np.append(balls_r, Ball_r())


rect1 = Rect()

run = True
while run:
	pygame.time.delay(50)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	screen.fill((0, 0, 0))

	pygame.draw.rect(screen, color, (rect1.x, rect1.y, rect1.width, rect1.height))
	# # Попробуем двинуть стенку
	# rect1.move(10, 0) # --> двигается!!!

	for i in range(n_balls):
		balls_l[i].position_x += balls_l[i].velocity_x * delta_t
		balls_l[i].position_y += balls_l[i].velocity_y * delta_t

		if balls_l[i].position_x - balls_l[i].radius < 0:
			balls_l[i].velocity_x *= -1
		if balls_l[i].position_x + balls_l[i].radius > width:
			balls_l[i].velocity_x *= -1
		# Обработаем столкновения со стенкой
		if balls_l[i].position_x + balls_l[i].radius > rect1.get_left_coord():
			balls_l[i].velocity_x *= -1
			# Двигаем саму стенку
			rect1.move(1, 0)

		if balls_l[i].position_y - balls_l[i].radius < 0:
			balls_l[i].velocity_y *= -1
		if balls_l[i].position_y + balls_l[i].radius > height:
			balls_l[i].velocity_y *= -1

		balls_r[i].position_x += balls_r[i].velocity_x * delta_t
		balls_r[i].position_y += balls_r[i].velocity_y * delta_t

		if balls_r[i].position_x - balls_r[i].radius < 0:
			balls_r[i].velocity_x *= -1
		if balls_r[i].position_x + balls_r[i].radius > width:
			balls_r[i].velocity_x *= -1
		# Обработаем столкновения со стенкой
		if balls_r[i].position_x - balls_r[i].radius < rect1.get_right_coord():
			balls_r[i].velocity_x *= -1
			# Двигаем саму стенку
			rect1.move(-1, 0)

		if balls_r[i].position_y - balls_r[i].radius < 0:
			balls_r[i].velocity_y *= -1
		if balls_r[i].position_y + balls_r[i].radius > height:
			balls_r[i].velocity_y *= -1

		pygame.draw.circle(screen, color, (balls_l[i].position_x, balls_l[i].position_y), balls_l[i].radius)
		pygame.draw.circle(screen, color, (balls_r[i].position_x, balls_r[i].position_y), balls_r[i].radius)

	pygame.display.update()

pygame.quit()
