def better_than_average(class_points, your_points):
    mediaClass = 0
    iterador = 0
    for i in range(0,len(class_points)):
        iterador += 1
        mediaClass += class_points[i]
    if mediaClass / iterador >= your_points:
        return False
    else:
        return True