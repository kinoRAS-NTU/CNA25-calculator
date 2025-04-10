from time import sleep

def add(numbers):
    return sum(numbers)

def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result
