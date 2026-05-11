def heapify(listă, n, i):

    cel_mai_mare = i
    stânga = 2 * i + 1
    dreapta = 2 * i + 2
    if stânga < n and listă[stânga] > listă[cel_mai_mare]: cel_mai_mare = stânga
    if dreapta < n and listă[dreapta] > listă[cel_mai_mare]: cel_mai_mare = dreapta
    if cel_mai_mare != i:
        listă[i], listă[cel_mai_mare] = listă[cel_mai_mare], listă[i]
        heapify(listă, n, cel_mai_mare)

def heap_sort(listă):
   
    n = len(listă)
    for i in range(n // 2 - 1, -1, -1): heapify(listă, n, i)
    for i in range(n - 1, 0, -1):
        listă[0], listă[i] = listă[i], listă[0]
        heapify(listă, i, 0)
    return listă
