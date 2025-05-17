def find_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: A list of numerical values.
        
    Returns:
        The average of the given numbers as a float.
    """
    if not numbers:
        return 0.0
    
    total = sum(numbers)
    count = len(numbers)
    return total / count

# Example usage
numbers = [1, 2, 3, 4, 5]
average = find_average(numbers)
print("The average is:", average)
