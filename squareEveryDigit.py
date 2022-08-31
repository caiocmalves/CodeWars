def square_digits(num):
    x = str(num)
    sup = 0
    apoio = ""
    for i in x:
      sup = int(i) ** 2
      apoio += str(sup)
    return int(apoio)