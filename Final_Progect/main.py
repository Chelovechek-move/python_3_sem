import pygame
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

wall_width = 100
# r_shift может быть и положительным, и отрицательным
# r_shift принимает положительные значения, если стенка сдвинута вправо относительно width / 2
r_shift = 50


# Ball - это класс, описывающий отдельный шарик
class Ball_l:
	def __init__(self):
		# radius >= 2
		self.radius = 2
		self.position_x = random.randrange(self.radius, width / 2 + r_shift - wall_width / 2 - self.radius)
		self.position_y = random.randrange(self.radius, height - self.radius)
		self.velocity_x = random.randrange(-100, 100)
		self.velocity_y = random.randrange(-100, 100)


class Ball_r:
	def __init__(self):
		# radius >= 2
		self.radius = 2
		self.position_x = random.randrange(width / 2 + r_shift + wall_width / 2 + self.radius, width - self.radius)
		self.position_y = random.randrange(self.radius, height - self.radius)
		self.velocity_x = random.randrange(-100, 100)
		self.velocity_y = random.randrange(-100, 100)


class Wall:
	def __init__(self):
		self.width = wall_width
		self.height = height
		self.x = (width / 2) + r_shift - (self.width / 2)
		self.y = 0

	def move(self, x, y):
		self.x += x
		self.y += y

	def get_right_coord(self):
		return self.x + self.width

	def get_left_coord(self):
		return self.x

	def get_position(self):
		return self.x + self.width / 2

	def set_position(self, pos):
		self.x = pos - self.width / 2


# ____Эта функция сохраняет все необходимые данные для восстановления состояния эксперимента______
# Ей необходимо передать два массива экземпляров шариков и массив с историей положения стенки
def save_experiment_state(balls_l, balls_r, wall_position):
	# Создаём массивы для сохранения данных
	mas_balls_l_pos_x = np.zeros(n_balls)
	mas_balls_l_pos_y = np.zeros(n_balls)
	mas_balls_r_pos_x = np.zeros(n_balls)
	mas_balls_r_pos_y = np.zeros(n_balls)
	mas_balls_l_vel_x = np.zeros(n_balls)
	mas_balls_l_vel_y = np.zeros(n_balls)
	mas_balls_r_vel_x = np.zeros(n_balls)
	mas_balls_r_vel_y = np.zeros(n_balls)

	# Записываем в массивы все текущие данные о шариках. Делаем это в цикле
	for i in range(n_balls):
		mas_balls_l_pos_x[i] = balls_l[i].position_x
		mas_balls_l_pos_y[i] = balls_l[i].position_y
		mas_balls_r_pos_x[i] = balls_r[i].position_x
		mas_balls_r_pos_y[i] = balls_r[i].position_y
		mas_balls_l_vel_x[i] = balls_l[i].velocity_x
		mas_balls_l_vel_y[i] = balls_l[i].velocity_y
		mas_balls_r_vel_x[i] = balls_r[i].velocity_x
		mas_balls_r_vel_y[i] = balls_r[i].velocity_y

	data = {'balls_l_pos_x': mas_balls_l_pos_x,
			'balls_l_pos_y': mas_balls_l_pos_y,
			'balls_r_pos_x': mas_balls_r_pos_x,
			'balls_r_pos_y': mas_balls_r_pos_y,
			'balls_l_vel_x': mas_balls_l_vel_x,
			'balls_l_vel_y': mas_balls_l_vel_y,
			'balls_r_vel_x': mas_balls_r_vel_x,
			'balls_r_vel_y': mas_balls_r_vel_y}

	# Создаём DataFrame со всеми данными о шариках
	df = pd.DataFrame(data)
	# Записываем DataFrame в файл .csv
	df.to_csv('test.csv')
	# Отдельно запишем массив wall_position в файл .txt
	np.savetxt('test.txt', wall_position, fmt='%d')


# Задаём размеры окна
size = width, height = 1000, 750

n_balls = 10000  # Задаём количество шариков
# Создаём массивы шариков слева и справа от стенки
balls_l = np.array([])
balls_r = np.array([])

wall = Wall()  # Создаём экземпляр класса Wall() - это наша стенка
wall_position = np.array([])  # Здесь будут лежать горизонтальные координаты стенки

# Поговорим с пользователем
print('Здравсвуйте! Сейчас мы будем моделировать поведение перегородки в сосуде между двумя одинаковыми газами.')
print('Вы хотите начать эксперимент с начала или продолжить, используя ваши начальные данные?')
print('Для того чтобы выбрать первый вариант необходимо ввести далее "1", второй вариан - "2".')
try:
	user_selection = int(input())
except:
	print('Вы ввели неверное значение!')
	print('Необходим ввести либо "1", либо "2".')
	print('Запустите программу ещё раз и попробуйте заново.')
	exit()
if user_selection != 1 and user_selection != 2:
	print('Вы ввели неверное значение!')
	print('Необходим ввести либо "1", либо "2".')
	print('Запустите программу ещё раз и попробуйте заново.')
	exit()
elif user_selection == 1:
	# Создаём массив шариков слева от стенки и заполняем его пустыми экземплярами класса Ball_l
	for i in range(n_balls):
		balls_l = np.append(balls_l, Ball_l())

	# Создаём массив шариков слева от стенки и заполняем его пустыми экземплярами класса Ball_r
	for i in range(n_balls):
		balls_r = np.append(balls_r, Ball_r())
elif user_selection == 2:
	print('Введите далее названия двух файлов вместе с расширением.')
	print('Один из них должен быть с расширением .csv, а другой .txt.')
	print('Название файла с расширением .csv: ', end='')
	name_csv = input()
	print('Название файла с расширением .txt: ', end='')
	name_txt = input()
	# Считываем все необходимые данные из файлов
	try:
		start_df = pd.read_csv(f'{name_csv}')
	except:
		print(f'Файла "{name_csv}" не существует! Проверьте правильность ввода.')
		print('Запустите программу ещё раз и попробуйте заново.')
		exit()
	try:
		wall_position = np.loadtxt(f'{name_txt}')
	except:
		print(f'Файла "{name_txt}" не существует! Проверьте правильность ввода.')
		print('Запустите программу ещё раз и попробуйте заново.')
		exit()
	mas_balls_l_pos_x = np.array(start_df.loc[:, 'balls_l_pos_x'])
	mas_balls_l_pos_y = np.array(start_df.loc[:, 'balls_l_pos_y'])
	mas_balls_r_pos_x = np.array(start_df.loc[:, 'balls_r_pos_x'])
	mas_balls_r_pos_y = np.array(start_df.loc[:, 'balls_r_pos_y'])
	mas_balls_l_vel_x = np.array(start_df.loc[:, 'balls_l_vel_x'])
	mas_balls_l_vel_y = np.array(start_df.loc[:, 'balls_l_vel_y'])
	mas_balls_r_vel_x = np.array(start_df.loc[:, 'balls_r_vel_x'])
	mas_balls_r_vel_y = np.array(start_df.loc[:, 'balls_r_vel_y'])

	n_balls = len(mas_balls_l_pos_x)  # Количество шариков в задаче пользователя

	# Создаём массив шариков слева от стенки и заполняем его пустыми экземплярами класса Ball_l
	for i in range(n_balls):
		balls_l = np.append(balls_l, Ball_l())

	# Создаём массив шариков слева от стенки и заполняем его пустыми экземплярами класса Ball_r
	for i in range(n_balls):
		balls_r = np.append(balls_r, Ball_r())

	# Теперь мы присвоим считанные из файлов значения экземпляров классов Ball_l и Ball_r в массивах balls_l и balls_r
	for i in range(n_balls):
		balls_l[i].position_x = mas_balls_l_pos_x[i]
		balls_l[i].position_y = mas_balls_l_pos_y[i]
		balls_l[i].velocity_x = mas_balls_l_vel_x[i]
		balls_l[i].velocity_y = mas_balls_l_vel_y[i]
		balls_r[i].position_x = mas_balls_r_pos_x[i]
		balls_r[i].position_y = mas_balls_r_pos_y[i]
		balls_r[i].velocity_x = mas_balls_r_vel_x[i]
		balls_r[i].velocity_y = mas_balls_r_vel_y[i]

	# Задаём последнюю координату, которая имела стенка за всё время
	wall.set_position(wall_position[-1])
# ____Теперь мы имеем полностью установленные начальные значения, заданные пользователем, а значит можем
# осуществлять эксперимент____

pygame.init()
screen = pygame.display.set_mode(size)

white_color = 255, 255, 255  # Переменная, определяющая белый цвет
black_color = 0, 0, 0  # Переменная, определяющая чёрный цвет
delta_t = 0.1  # Шаг по времени, по которому рассчитывается перемещение шариков

# _____Далее идёт основной блок, в котором происходит сам эксперимент______
run = True  # Переменная, отвечающая за то, активно ли окно
while run:
	# Сделаем задержку для того чтобы мы могли наблюдать за отрисовкой процесса
	# Если в отрисовке нет необходимости, то строчку лучше закомментировать
	# pygame.time.delay(50)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# screen.fill(black_color)

	# Отрисовка стенки
	# pygame.draw.rect(screen, (0, 255, 0), (wall.x, wall.y, wall.width, wall.height))

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
			# Мы будем немного телепортировать шарики от стенки после соударения,так как из-за того,
			# что и шарики, и стенка движутся, то они как бы "прилипают" к ней и сильно замедляют ее перемещение.
			# Данный сдвиг имеет довольно большое значение на среднюю скорость движения стенки к асимптоте,
			# поэтому его стоит сохранять одинаковым, если необходимо сравнить данные из нескольких экспериментов
			balls_l[i].position_x = balls_l[i].position_x - 5
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
			# Мы будем немного телепортировать шарики от стенки после соударения,так как из-за того,
			# что и шарики, и стенка движутся, то они как бы "прилипают" к ней и сильно замедляют ее перемещение.
			# Данный сдвиг имеет довольно большое значение на среднюю скорость движения стенки к асимптоте,
			# поэтому его стоит сохранять одинаковым, если необходимо сравнить данные из нескольких экспериментов
			balls_r[i].position_x = balls_r[i].position_x + 5
			# Двигаем саму стенку
			wall.move(-1, 0)

		if balls_r[i].position_y - balls_r[i].radius < 0:
			balls_r[i].velocity_y *= -1
		if balls_r[i].position_y + balls_r[i].radius > height:
			balls_r[i].velocity_y *= -1

		# Заполняем массив с положениями стенки
		wall_position = np.append(wall_position, wall.get_position())

		# Отрисовываем шарики слева и справа от стенки:
		# pygame.draw.circle(screen, white_color, (balls_l[i].position_x, balls_l[i].position_y), balls_l[i].radius)
		# pygame.draw.circle(screen, white_color, (balls_r[i].position_x, balls_r[i].position_y), balls_r[i].radius)

		# Будем сохранять состояние эксперимента каждые 100 000 перемещений стенки для того чтобы уберечь вычисленные
		# данные от удаления в случае аварийного завершения процесса
		if len(wall_position) % 100000 == 0:
			save_experiment_state(balls_l, balls_r, wall_position)
			# Следующая строчка удобна для отладки программы и построения графика
			print(len(wall_position), wall_position[-1])

		# Будем строить график сразу же по ходу проведения эксперимента
		# Будем вносить изменения в график каждые 1000 перемещений стенки
		if len(wall_position) % 1000 == 0:
			data_x = np.arange(len(wall_position))
			plt.ion()  # interactive mode will be on
			plt.clf()  # clear the current figure
			plt.grid(True)
			plt.plot(data_x, wall_position, label='Сырые данные')
			plt.draw()  # updating plot
			plt.gcf().canvas.flush_events()  # updating plot
			plt.show()

	# Обновляем дисплей:
	pygame.display.update()

pygame.quit()
plt.ioff()  # interactive mode will be off
# ____Основной вычислительный блок эксперимента закончился______

# Сохраним текущее состояние эксперимента:
save_experiment_state(balls_l, balls_r, wall_position)
# ____Теперь все необходимые данные сохранены_____

# Для того чтобы получить первое представление о полученной зависимости сгладим колебания графика,
# используя скользящее среднее с шагом n
n = 100000
data_y_new = np.zeros(wall_position.size)

for i in range(wall_position.size):
	if i + 1 <= n:
		sum_data = (wall_position[:i + 1].sum()) / (i + 1)
		data_y_new[i] = sum_data
	else:
		sum_data = (wall_position[i - n:i].sum()) / n
		data_y_new[i] = sum_data

# Построим итоговый график
data_x = np.arange(len(wall_position))
plt.grid(True)
plt.plot(data_x, wall_position, label='Сырые данные')
plt.plot(data_x, data_y_new, label='Данные после фильтра')
plt.legend()
plt.show()
