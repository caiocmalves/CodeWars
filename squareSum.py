import math

def square_sum(numbers):
    total = 0
    valor = 0
    if numbers == "":
        return 0
    else:
        for i in range(0,len(numbers)):
            total += math.pow(numbers[i], 2)
    return total