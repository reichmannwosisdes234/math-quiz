def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return round(average, 2)

# Example usage
numbers = [1, 2, 3, 4, 5]
print(f"The average of the numbers is: {calculate_average(numbers)}")
