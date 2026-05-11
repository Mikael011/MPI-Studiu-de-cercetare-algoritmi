import os    
import sys     
import time   


base_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(base_path)
if base_path not in sys.path:
    sys.path.insert(0, base_path)


from utilitare import citește_din_fișier, evaluare_performanță


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

def main():
    folder_input = "teste_input"              
    fisier_raport = "raport_performanta.txt"  
    
    with open(fisier_raport, 'a', encoding='utf-8') as f:
        f.write("\n" + "=" * 65 + "\n")
        f.write("=== SESIUNE NOUA DE TESTARE ===\n")
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"Data si ora pornirii: {timestamp}\n")
        f.write("=" * 65 + "\n")

    algoritmi = [
        ("Bubble Sort", bubble_sort, False),
        ("Selection Sort", selection_sort, False),
        ("Insertion Sort", insertion_sort, False),
        ("Shell Sort", shell_sort, False),
        ("Merge Sort", merge_sort, False),
        ("Quick Sort", quick_sort, False),
        ("Heap Sort", heap_sort, False),
        ("Counting Sort", counting_sort, True),
        ("Radix Sort", radix_sort, True)
    ]


    if not os.path.exists(folder_input):
        print(f"Eroare: Folderul '{folder_input}' nu a fost gasit in directorul curent!")
        return

    fisiere = sorted([f for f in os.listdir(folder_input) if f.endswith('.txt')])
    
    for nume_fisier in fisiere:
        cale_in = os.path.join(folder_input, nume_fisier)
        cazuri, eroare = citește_din_fișier(cale_in)
        
        if eroare: continue

        print(f"\nProcesare fisier: {nume_fisier}")
        
        with open(fisier_raport, 'a', encoding='utf-8') as f:
            f.write(f"\n>>> FISIER: {nume_fisier} <<<\n")
        
        for caz in cazuri:
            lista = caz['date']
            tip = caz['tip']
            desc = caz['desc']
            n = len(lista)
            
            print(f"  Test: {desc} ({n} elemente)")
            with open(fisier_raport, 'a', encoding='utf-8') as f:
                f.write(f"\n  [CAZ: {desc} | N: {n} | TIP: {tip}]\n")

            for nume_alg, func_alg, doar_int in algoritmi:
                if n > 10000 and nume_alg in ["Bubble Sort", "Selection Sort", "Insertion Sort"]:
                    continue
                
                if doar_int and tip != 'int':
                    continue

                if nume_alg == "Counting Sort" and tip == 'int':
                    v_min, v_max = min(lista), max(lista)
                    if (v_max - v_min > 10**7): continue

                print(f"    - Se executa {nume_alg}...", end="", flush=True)
                rezultat, timp, memorie = evaluare_performanță(func_alg, lista)
                print(f" Gata")
 
                with open(fisier_raport, 'a', encoding='utf-8') as f:
                    f.write(f"    {nume_alg:15} | Timp: {timp:10.6f}s | Memorie: {memorie:8.2f} KB\n")

    print(f"\n[FINALIZAT] Raportul a fost actualizat in '{os.path.abspath(fisier_raport)}'.")

if __name__ == "__main__":
    main()
