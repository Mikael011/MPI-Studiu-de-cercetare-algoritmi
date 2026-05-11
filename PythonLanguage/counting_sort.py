def counting_sort(listă):

    if not listă: return listă
    if not all(isinstance(x, int) for x in listă):
        return "EROARE: Counting Sort suportă doar numere întregi!"
    
    max_val = max(listă)
    min_val = min(listă)
    interval = max_val - min_val + 1
    numărare = [0] * interval
    rezultat = [0] * len(listă)
    
    for x in listă: numărare[x - min_val] += 1
    for i in range(1, len(numărare)): numărare[i] += numărare[i - 1]
    for i in range(len(listă) - 1, -1, -1):
        rezultat[numărare[listă[i] - min_val] - 1] = listă[i]
        numărare[listă[i] - min_val] -= 1
    return rezultat
