def insertion_sort(listă):
   
    for i in range(1, len(listă)):
        valoare_curentă = listă[i]
        j = i - 1
        while j >= 0 and valoare_curentă < listă[j]:
            listă[j + 1] = listă[j]
            j -= 1
        listă[j + 1] = valoare_curentă
    return listă
