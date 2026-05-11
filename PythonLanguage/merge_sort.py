def merge_sort(listă):
  
    if len(listă) > 1:
        mijloc = len(listă) // 2
        stânga = listă[:mijloc]
        dreapta = listă[mijloc:]

        merge_sort(stânga)
        merge_sort(dreapta)

        i = j = k = 0
        while i < len(stânga) and j < len(dreapta):
            if stânga[i] <= dreapta[j]:
                listă[k] = stânga[i]
                i += 1
            else:
                listă[k] = dreapta[j]
                j += 1
            k += 1

        while i < len(stânga):
            listă[k] = stânga[i]
            i += 1
            k += 1

        while j < len(dreapta):
            listă[k] = dreapta[j]
            j += 1
            k += 1
    return listă
