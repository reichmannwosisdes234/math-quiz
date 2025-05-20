import math

def is_even(n):
    """Check if a number is even"""
    return n % 2 == 0

def cube_root(a):
    """Calculate the cube root of a number (x)"""
    return math.pow(x, 1/3)

def prime_factors(number):
    """Find the prime factors of a given number"""
    i = 2
    factors = []
    while i * i <= number:
        if number % i == 0:
            factors.append(i)
            number //= i
        else:
            i += 1
    if number > 1:
        factors.append(number)
    return factors

def is_perfect_cube(x):
    """Check if a number is a perfect cube"""
    y = x ** (1/3)
    return y == int(y)

# Example usage:
n = 8  # This should be an even number
even_check = is_even(n)
cube_root_result = cube_root(n)
prime_factors_result = prime_factors(n)
is_perfect_cube_test = is_perfect_cube(n)
