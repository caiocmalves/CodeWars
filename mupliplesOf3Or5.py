def solution(number):
    soma = 0
    if number < 0:
        return 0
    else:
        for i in range(1, number):
            if i % 3 == 0 or i % 5 == 0:
                soma += i
            else:
                soma += 0
    return soma