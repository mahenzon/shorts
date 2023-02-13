import timeit

def power_self(numbers):
    return [
        number ** number
        for number in numbers
    ]

print(timeit.timeit(power_self, number=1000, ))
