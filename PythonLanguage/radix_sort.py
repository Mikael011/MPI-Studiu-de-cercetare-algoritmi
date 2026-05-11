def radix_sort(listă):
    
    if not listă: return listă
    if not all(isinstance(x, int) for x in listă):
        return 
    
    def sortare_numărare_radix(listă, exp):
        n = len(listă)
        rezultat = [0] * n
        numărare = [0] * 10
        for i in range(n):
            index = listă[i] // exp
            numărare[index % 10] += 1
        for i in range(1, 10): numărare[i] += numărare[i - 1]
        i = n - 1
        while i >= 0:
            index = listă[i] // exp
            rezultat[numărare[index % 10] - 1] = listă[i]
            numărare[index % 10] -= 1
            i -= 1
        for i in range(len(listă)): listă[i] = rezultat[i]

    max_val = max(listă)
    exp = 1
    while max_val // exp > 0:
        sortare_numărare_radix(listă, exp)
        exp *= 10
    return listă
