def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)

# Example usage:
# numbers = [1, 2, 3, 4, 5]
# print(calculate_average(numbers))