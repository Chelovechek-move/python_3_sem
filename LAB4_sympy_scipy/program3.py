import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from scipy.integrate import odeint

# Решение с использованием SymPy
x = Symbol('x')
y = Function('y')
diffeq = Eq(y(x).diff(x), -2 * y(x))
sol = dsolve(diffeq, y(x), ics={y(0): sqrt(2)})  # ics is the set of initial conditions
# lambdify transform sympy expressions to lambda functions
f = lambdify(x, sol.rhs)  # res.rhs returns the right part of solved_eq

data_x = np.linspace(0, 10, 1000)
data1_y = f(data_x)


# Решение с использованием Scipy
def dydx(y, x):
	return -2 * y


data_x = np.linspace(0, 10, 1000)
y0 = np.sqrt(2)  # set initial conditions
data2_y = odeint(dydx, y0, data_x)
data2_y = np.array(data2_y).flatten()  # flatten() return a copy of the array collapsed into one dimension

# Построение графиков
plt.subplot(1, 3, 1)
plt.title("SymPy solution")
plt.grid(True)
plt.plot(data_x, data1_y, linewidth=2, color='blue')

plt.subplot(1, 3, 2)
plt.title("Scipy solution")
plt.grid(True)
plt.plot(data_x, data2_y, linewidth=2, color='red')

plt.subplot(1, 3, 3)
plt.title("Difference of solutions")
plt.grid(True)
plt.plot(data_x, np.abs(data1_y - data2_y), linewidth=1, color='green')

plt.show()
