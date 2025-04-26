import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def f(x):
    return np.sin(2 * np.pi * x)

a = -0.5  # a
b = 0.5   # b
t = 1     # t
N = 1000  # number of samples

x = np.random.uniform(a, b, N)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) versus x')
plt.show()
