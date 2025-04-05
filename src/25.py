import math

def is_perfect_square(n):
    """
    Check if n is a perfect square.
    
    A number is considered a perfect square if it can be expressed as the product of two identical numbers.
    For example, 4 is a perfect square because 2 * 2 = 4. However, 8 is not a perfect square since it's also
    the product of 2 and 2.
    
    Parameters:
    n (int): The number to check if it's a perfect square.
    
    Returns:
    bool: True if n is a perfect square, False otherwise.
    """
    return math.isqrt(n) ** 2 == n

def calculate_square_root(num):
    """
    Calculate the square root of a given number.
    
    Parameters:
    num (int): The number for which to calculate the square root.
    
    Returns:
    float: The square root of the input number.
    """
    return math.sqrt(num)

# Example usage
print(is_perfect_square(4))  # True
print(is_perfect_square(8))  # False
print(calculate_square_root(16))  # 4.0
