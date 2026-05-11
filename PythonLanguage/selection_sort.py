def selection_sort(listă):

    n = len(listă)
    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if listă[j] < listă[indice_min]:
                indice_min = j
        listă[i], listă[indice_min] = listă[indice_min], listă[i]
    return listă
