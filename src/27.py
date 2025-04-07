def calculate_sum(n):
    """
    Calculate the sum of first n natural numbers.
    
    Parameters:
    n (int): The number of initial natural numbers to be summed up.
    
    Returns:
    int: The sum of the first n natural numbers.
    """
    return n * (n + 1) // 2

def check_solution():
    assert calculate_sum(10) == 55, "Test case 1 failed"
    assert calculate_sum(5) == 15, "Test case 2 failed"
    print("All test cases passed!")

if __name__ == "__main__":
    check_solution()
