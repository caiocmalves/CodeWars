def two_sum(numbers, target):
    
    for i in range(0, len(numbers)):
        aux1 = numbers[i]
        for j in range(1, len(numbers)):
            aux2 = numbers[j]
            if aux1 + aux2 == target:
                break
            else:
                continue
        if aux1 + aux2 == target:
                break
    return (i, j)