def sum_two_smallest_numbers(numbers):
    min1 = 0
    min2 = 0
    
    min1 = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min1:
            min1 = numbers[i]
    min2 = numbers[1]    
    for i in range(0, len(numbers)):
        if numbers[i] > min1 and numbers[i] < min2:
            min2 = numbers[i]
    
    return min1 + min2