import numpy as np

def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle.
        
    Returns:
        float: The area of the circle.
    """
    area = 3.14159 * radius ** 2
    return area

# Generate random numbers for demonstration purposes
random_numbers = np.random.randint(0, 100, size=5)

result = calculate_area(random_numbers[0])
print(f"The area of the circle is: {result}")
