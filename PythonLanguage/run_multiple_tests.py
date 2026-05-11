import os
import sys
import time

base_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(base_path)

if base_path not in sys.path:
    sys.path.insert(0, base_path)


from utilitare import citește_din_fișier

sys.setrecursionlimit(200000)

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from counting_sort import counting_sort
from radix_sort import radix_sort


def measure_time_ms(func, data, reps=1):
    start = time.perf_counter()
    for _ in range(reps):
        data_copy = data.copy()
        func(data_copy)
    end = time.perf_counter()
    return ((end - start) * 1000) / reps

def main():
    folder_input = "teste_input"
    nr_rulari = 5 
    

    algoritmi = [
        {"nume": "Bubble Sort",    "func": bubble_sort,    "max_n": 10000}, # Marit limita pentru a vedea rezultate pe liste medii
        {"nume": "Selection Sort", "func": selection_sort, "max_n": 10000},
        {"nume": "Insertion Sort", "func": insertion_sort, "max_n": 30000},
        {"nume": "Shell Sort",     "func": shell_sort,     "max_n": 1000000},
        {"nume": "Merge Sort",     "func": merge_sort,     "max_n": 1000000},
        {"nume": "Quick Sort",     "func": quick_sort,     "max_n": 1000000},
        {"nume": "Heap Sort",      "func": heap_sort,      "max_n": 1000000},
        {"nume": "Counting Sort",  "func": counting_sort,  "max_n": 1000000, "only_int": True},
        {"nume": "Radix Sort",     "func": radix_sort,     "max_n": 1000000, "only_int": True}
    ]


    fisiere = sorted([f for f in os.listdir(folder_input) if f.endswith('.txt')])
    
    with open("raport_analiza_algoritmi.md", "w", encoding="utf-8") as f:
        f.write("# Raport Detaliat - Rulari Multiple (Statistica Imbunatatita)\n\n")
        f.write("NOTA: Pentru liste mici (N < 500), timpul este media a 1.000 de rulari interne per celula pentru a elimina zgomotul de sistem.\n\n")

        for nume_fisier in fisiere:
            cale_in = os.path.join(folder_input, nume_fisier)
            cazuri, eroare = citește_din_fișier(cale_in)
            if eroare: continue

            for caz in cazuri:
                lista = caz['date']
                n = len(lista)
                tip = caz['tip']
                desc = caz['desc']
                reps_interne = 1000 if n < 500 else 1

                f.write(f"## Test: {nume_fisier} ({desc}, N={n})\n")
                f.write(f"*Metodologie: {nr_rulari} esantioane x {reps_interne} repetitii interne*\n\n")
                f.write("| Algoritm       | Rularea 1 | Rularea 2 | Rularea 3 | Rularea 4 | Rularea 5 | Media (ms)  |\n")
                f.write("| :------------- | :-------- | :-------- | :-------- | :-------- | :-------- | :---------- |\n")

                for alg in algoritmi:
                    if n > alg["max_n"]: continue
                    if alg.get("only_int") and tip != 'int': continue
                    
                    timpi = []
                    for _ in range(nr_rulari):
                        try:
                            t = measure_time_ms(alg["func"], lista, reps=reps_interne)
                            timpi.append(t)
                        except Exception as e:
                            timpi.append(None)
                    
                    if None in timpi:
                        row = f"| {alg['nume']:14} | Eroare    | -        | -        | -        | -        | -          |"
                    else:
                        media = sum(timpi) / len(timpi)
                        row = f"| {alg['nume']:14} | {timpi[0]:<9.4f} | {timpi[1]:<9.4f} | {timpi[2]:<9.4f} | {timpi[3]:<9.4f} | {timpi[4]:<9.4f} | **{media:<9.4f}** |"
                    
                    f.write(row + "\n")
                f.write("\n")

        f.write("\n--- \n")
        f.write("## Concluzii Detaliate si Analiza de Performanta\n\n")
        f.write("... (Aici urmeaza continutul analizat anterior) ...\n")

if __name__ == "__main__":
    main()
