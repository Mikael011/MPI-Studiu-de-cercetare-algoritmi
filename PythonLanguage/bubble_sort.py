def bubble_sort(listă):
    n = len(listă)
    for i in range(n):
        interschimbat = False
        for j in range(0, n - i - 1):
            if listă[j] > listă[j + 1]:
                listă[j], listă[j + 1] = listă[j + 1], listă[j]
                interschimbat = True
        if not interschimbat:
            break
    return listă
