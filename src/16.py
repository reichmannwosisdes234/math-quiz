import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt

# Generate some data points for demonstration
np.random.seed(0)
x = np.random.randn(100)

def calculate_erf(x):
    return 2. / np.sqrt(np.pi) * np.exp(-x**2 / 2)

erf_x = calculate_erf(x)
