import numpy as np
from scipy.special import comb
from math import factorial

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_combinations(n, r):
    return comb(n, r)

def factorial(n):
    return factorial(n)

# Example usage
num1 = 5
num2 = 3
print("Combinations of", num1, "numbers chosen from", num2, "numbers:", calculate_combinations(num1, num2))
