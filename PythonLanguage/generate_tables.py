import os
import time
import sys
from utilitare import citește_din_fișier

base_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(base_path)
if base_path not in sys.path:
    sys.path.insert(0, base_path)

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

def measure_time_ms(func, data):
    data_copy = data.copy() 
    start = time.perf_counter()
    func(data_copy)
    end = time.perf_counter()
    return (end - start) * 1000

def main():
    folder_input = "teste_input"
    
    algoritmi = [
        {
            "nume": "Bubble Sort",
            "func": bubble_sort,
            "time_o": "O(n²)",
            "space_o": "O(1)",
            "only_int": False,
            "max_n": 5000 
        },
        {
            "nume": "Selection Sort",
            "func": selection_sort,
            "time_o": "O(n²)",
            "space_o": "O(1)",
            "only_int": False,
            "max_n": 5000
        },
        {
            "nume": "Insertion Sort",
            "func": insertion_sort,
            "time_o": "O(n²)",
            "space_o": "O(1)",
            "only_int": False,
            "max_n": 10000
        },
        {
            "nume": "Shell Sort",
            "func": shell_sort,
            "time_o": "O(n log² n)",
            "space_o": "O(1)",
            "only_int": False,
            "max_n": 50000
        },
        {
            "nume": "Merge Sort",
            "func": merge_sort,
            "time_o": "O(n log n)",
            "space_o": "O(n)",
            "only_int": False,
            "max_n": 1000000
        },
        {
            "nume": "Quick Sort",
            "func": quick_sort,
            "time_o": "O(n log n)",
            "space_o": "O(log n)",
            "only_int": False,
            "max_n": 1000000
        },
        {
            "nume": "Heap Sort",
            "func": heap_sort,
            "time_o": "O(n log n)",
            "space_o": "O(1)",
            "only_int": False,
            "max_n": 1000000
        },
        {
            "nume": "Counting Sort",
            "func": counting_sort,
            "time_o": "O(n + k)",
            "space_o": "O(k)",
            "only_int": True,
            "max_n": 1000000
        },
        {
            "nume": "Radix Sort",
            "func": radix_sort,
            "time_o": "O(n * d)",
            "space_o": "O(n + k)",
            "only_int": True,
            "max_n": 1000000
        }
    ]

    if not os.path.exists(folder_input):
        print(f"Eroare: Folderul '{folder_input}' nu există.")
        return

    fisiere = sorted([f for f in os.listdir(folder_input) if f.endswith('.txt')])

    all_results = {alg["nume"]: [] for alg in algoritmi}

    for nume_fisier in fisiere:
        cale_in = os.path.join(folder_input, nume_fisier)
        cazuri, eroare = citește_din_fișier(cale_in)
        if eroare: continue
        
        for caz in cazuri:
            lista = caz['date']
            tip = caz['tip']
            n = len(lista)
            
            for alg in algoritmi:
                if n > alg["max_n"]:
                    all_results[alg["nume"]].append((nume_fisier, tip, n, "N/A (Prea lent)"))
                    continue
                if alg["only_int"] and tip != 'int':
                    all_results[alg["nume"]].append((nume_fisier, tip, n, "N/A (Tip incompatibil)"))
                    continue

                try:
                    t_ms = measure_time_ms(alg["func"], lista)
                    all_results[alg["nume"]].append((nume_fisier, tip, n, f"{t_ms:.4f}"))
                except Exception as e:
                    all_results[alg["nume"]].append((nume_fisier, tip, n, "Eroare"))

    print("# Raport Performanță Algoritmi de Sortare\n")
    print("| Algoritm | Complexitate Timp | Complexitate Spațiu |")
    print("| :--- | :--- | :--- |")
    for alg in algoritmi:
        print(f"| {alg['nume']} | {alg['time_o']} | {alg['space_o']} |")
    print("\n")

    for alg in algoritmi:
        print(f"## {alg['nume']}")
        print(f"| Fișier Input | Tip | N | Timp (ms) |")
        print(f"| :--- | :--- | :--- | :--- |")
        for res in all_results[alg["nume"]]:
            print(f"| {res[0]} | {res[1]} | {res[2]} | {res[3]} |")
        print("\n")

if __name__ == "__main__":
    main()
