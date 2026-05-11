import random

def quick_sort(listă):
   
    def _quick_sort(jos, sus):
        if jos >= sus:
            return
        
        pivot_idx = random.randint(jos, sus)
        pivot = listă[pivot_idx]

        lt = jos
        i = jos
        gt = sus
        
        while i <= gt:
            if listă[i] < pivot:
                listă[lt], listă[i] = listă[i], listă[lt]
                lt += 1
                i += 1
            elif listă[i] > pivot:
                listă[i], listă[gt] = listă[gt], listă[i]
                gt -= 1
            else:
                i += 1

        _quick_sort(jos, lt - 1)
        _quick_sort(gt + 1, sus)

    _quick_sort(0, len(listă) - 1)
    return listă
