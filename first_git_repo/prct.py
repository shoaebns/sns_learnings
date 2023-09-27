def compute(numbers):
    result = 1
    for num in numbers:
        result *= num - 3
    return result

values = [7, 4, 5]
computed_value = compute(values)
print(computed_value)