import pygame
import numpy as np
import random
import matplotlib.pyplot as plt

wall_width = 100
# r_shift может быть и положительным, и отрицательным
# r_shift принимает положительные значения, если стенка сдвинута вправо относительно width / 2
r_shift = 100


# Ball - это класс, описывающий отдельный шарик
class Ball_l:
	def __init__(self):
		# radius >= 2
		self.radius = 2
		self.delta = self.radius * 0.5
		self.position_x = random.randrange(self.delta, width / 2 + r_shift - wall_width / 2 - self.delta)
		self.position_y = random.randrange(self.delta, height - self.delta)
		self.velocity_x = random.randrange(-100, 100)
		self.velocity_y = random.randrange(-100, 100)
		self.m = 10


class Ball_r:
	def __init__(self):
		# radius >= 2
		self.radius = 2
		self.delta = self.radius * 0.5
		self.position_x = random.randrange(width / 2 + r_shift + wall_width / 2 + self.delta, width - self.delta)
		self.position_y = random.randrange(self.delta, height - self.delta)
		self.velocity_x = random.randrange(-100, 100)
		self.velocity_y = random.randrange(-100, 100)
		self.m = 10


class Wall:
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
n_balls = 1000  # Задаём количество шариков
screen = pygame.display.set_mode(size)

white_color = 255, 255, 255  # Переменная, определяющая белый цвет
black_color = 0, 0, 0  # Переменная, определяющая чёрный цвет
delta_t = 0.1  # Шаг по времени, по которому рассчитывается перемещение шариков

# Создаём массивы шариков слева и справа от стенки
balls_l = np.array([])
balls_r = np.array([])

# Заполняем массив шариков слева от стенки
for i in range(n_balls):
	balls_l = np.append(balls_l, Ball_l())

# Заполняем массив шариков справа от стенки
for i in range(n_balls):
	balls_r = np.append(balls_r, Ball_r())

wall = Wall()  # Создаём экземпляр класса Wall() - это наша стенка

run = True  # Переменная, отвечающая за то, активно ли окно
while run:
	pygame.time.delay(50)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	screen.fill(black_color)

	pygame.draw.rect(screen, (0, 255, 0), (wall.x, wall.y, wall.width, wall.height))
	# # Попробуем двинуть стенку
	# rect1.move(10, 0) # --> двигается!!!

	# В цикле проходимся по всем шарикам
	for i in range(n_balls):
		# Работаем с шариками слева от стенки:
		balls_l[i].position_x += balls_l[i].velocity_x * delta_t
		balls_l[i].position_y += balls_l[i].velocity_y * delta_t

		if balls_l[i].position_x - balls_l[i].radius < 0:
			balls_l[i].velocity_x *= -1
		if balls_l[i].position_x + balls_l[i].radius > width:
			balls_l[i].velocity_x *= -1
		# Обработаем столкновения со стенкой
		if balls_l[i].position_x + balls_l[i].radius > wall.get_left_coord():
			balls_l[i].velocity_x *= -1
			# Двигаем саму стенку
			wall.move(1, 0)

		if balls_l[i].position_y - balls_l[i].radius < 0:
			balls_l[i].velocity_y *= -1
		if balls_l[i].position_y + balls_l[i].radius > height:
			balls_l[i].velocity_y *= -1

		# Работаем с шариками справа от стенки:
		balls_r[i].position_x += balls_r[i].velocity_x * delta_t
		balls_r[i].position_y += balls_r[i].velocity_y * delta_t

		if balls_r[i].position_x - balls_r[i].radius < 0:
			balls_r[i].velocity_x *= -1
		if balls_r[i].position_x + balls_r[i].radius > width:
			balls_r[i].velocity_x *= -1
		# Обработаем столкновения со стенкой
		if balls_r[i].position_x - balls_r[i].radius < wall.get_right_coord():
			balls_r[i].velocity_x *= -1
			# Двигаем саму стенку
			wall.move(-1, 0)

		if balls_r[i].position_y - balls_r[i].radius < 0:
			balls_r[i].velocity_y *= -1
		if balls_r[i].position_y + balls_r[i].radius > height:
			balls_r[i].velocity_y *= -1

		# Отрисовываем шарики слева и справа от стенки:
		pygame.draw.circle(screen, white_color, (balls_l[i].position_x, balls_l[i].position_y), balls_l[i].radius)
		pygame.draw.circle(screen, white_color, (balls_r[i].position_x, balls_r[i].position_y), balls_r[i].radius)

	# Обновляем дисплей:
	pygame.display.update()

pygame.quit()
