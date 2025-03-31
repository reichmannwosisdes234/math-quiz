def addition(a: int, b: int) -> int:
    """
    This function takes two integers as input and returns their sum.
    
    Parameters:
    a (int): The first integer to be added.
    b (int): The second integer to be added.
    
    Returns:
    int: The sum of the two integers.
    """
    return a + b

def subtraction(a: int, b: int) -> int:
    """
    This function takes two integers as input and returns their difference.
    
    Parameters:
    a (int): The first integer to be subtracted from.
    b (int): The second integer to be subtracted from.
    
    Returns:
    int: The difference between the two integers.
    """
    return a - b

def multiplication(a: int, b: int) -> int:
    """
    This function takes two integers as input and returns their product.
    
    Parameters:
    a (int): The first integer to be multiplied.
    b (int): The second integer to be multiplied.
    
    Returns:
    int: The product of the two integers.
    """
    return a * b

def division(a: int, b: int) -> float:
    """
    This function takes two integers as input and returns their quotient if possible,
    otherwise it raises an exception.
    
    Parameters:
    a (int): The numerator of the division operation.
    b (int): The denominator of the division operation.
    
    Returns:
    float: The quotient or a ValueError if division is not possible.
    """
    return round(a / b, 2)

def exponentiation(base: int, exponent: int) -> int:
    """
    This function takes two integers as input and returns their power.
    
    Parameters:
    base (int): The base of the exponentiation operation.
    exponent (int): The exponent to which the base is raised.
    
    Returns:
    int: The result of raising the base to the power of the exponent.
    """
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer.")
    return base ** exponent

def factorial(n: int) -> int:
    """
    This function takes an integer as input and returns its factorial.
    
    Parameters:
    n (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def lcm(a: int, b: int) -> int:
    """
    This function takes two integers as input and returns their lowest common multiple (LCM).
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The LCM of the two integers.
    """
    return abs(a * b) // gcd(abs(a), abs(b))

def gcd(a: int, b: int) -> int:
    """
    This function takes two integers as input and returns their greatest common divisor (GCD).
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The GCD of the two integers.
    """
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

def is_even(x: int) -> bool:
    """
    This function takes an integer as input and returns True if the number is even,
    otherwise False.
    
    Parameters:
    x (int): The integer to check for evenness.
    
    Returns:
    bool: True if the number is even, otherwise False.
    """
    return x % 2 == 0

def main():
    print("Welcome to Math Quiz!")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("\nAddition: ", addition(a, b))
    print("Subtraction: ", subtraction(a, b))
    print("Multiplication: ", multiplication(a, b))
    print("Division: ", division(a, b))
    print("Exponentiation: ", exponentiation(base=a, exponent=b))
    print("Factorial: ", factorial(n=a))

if __name__ == "__main__":
    main()
