def shell_sort(listă):
   
    n = len(listă)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temporar = listă[i]
            j = i
            while j >= interval and listă[j - interval] > temporar:
                listă[j] = listă[j - interval]
                j -= interval
            listă[j] = temporar
        interval //= 2
    return listă
