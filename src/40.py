import numpy as np
from sklearn.linear_model import LinearRegression

def calculate_mean(variance):
    mean = variance.mean()
    std_deviation = np.sqrt(variance.std(ddof=1))
    return mean, std_deviation

# Example usage:
variance = [2.5, 3.0, 4.0, 5.5, 6.0]
mean, std_deviation = calculate_mean(variance)
print(f"Mean: {mean}, Standard Deviation: {std_deviation}")
