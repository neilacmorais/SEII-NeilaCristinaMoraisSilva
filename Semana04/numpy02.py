import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([3, 5, 7, 3])
print(2*a1)

print(1/a1)

print(a1>4)

print(1/a1 + a1 + 2)

x = np.linspace(0, 1, 100)
y = x**2

plt.plot(x, y)
plt.show()

a2= np.random.random(10)
plt.hist(a2)
plt.show()

def f(x):
	return x**2 * np.sin(x) / np.exp(-x)

x = np.linspace(0, 10, 100)
y = f(x)
plt.plot(x, y)
plt.show()
