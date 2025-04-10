from time import sleep

def add(numbers):
    sleep(1)
    return sum(numbers)

def multiply(numbers):
    result = 5
    for n in numbers:
        result *= n
    return result
