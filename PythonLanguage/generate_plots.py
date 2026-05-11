import matplotlib.pyplot as plt
import numpy as np


n_valori = [100, 1000, 10000, 100000]

bubble = [0.389, 97.398, np.nan, np.nan]
selection = [0.194, 45.390, np.nan, np.nan]
insertion = [0.186, 38.241, 4812.219, np.nan]
shell = [0.075, 3.096, 67.270, 1242.820]
merge = [0.227, 3.260, 49.742, 693.479]
quick = [0.151, 3.257, 42.757, 477.651]
heap = [0.134, 2.846, 48.318, 747.362]
counting = [4.128, 5.001, 12.920, 97.224]
radix = [0.179, 2.725, 35.102, 470.450]

def plot_all_9_log():
    plt.figure(figsize=(12, 8))
    
    # Adaugam fiecare algoritm in grafic
    plt.plot(n_valori, bubble,    marker='o', label='Bubble Sort', linestyle='--')
    plt.plot(n_valori, selection, marker='v', label='Selection Sort', linestyle='--')
    plt.plot(n_valori, insertion, marker='s', label='Insertion Sort', linestyle='--')
    plt.plot(n_valori, shell,     marker='p', label='Shell Sort')
    plt.plot(n_valori, merge,     marker='h', label='Merge Sort', linewidth=2)
    plt.plot(n_valori, quick,     marker='*', label='Quick Sort', linewidth=2)
    plt.plot(n_valori, heap,      marker='D', label='Heap Sort')
    plt.plot(n_valori, counting,  marker='X', label='Counting Sort', linewidth=2)
    plt.plot(n_valori, radix,     marker='P', label='Radix Sort')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Dimensiune listă (N) - Scară Logaritmică')
    plt.ylabel('Timp mediu (ms) - Scară Logaritmică')
    plt.title('Comparație Completă: Toți cei 9 Algoritmi de Sortare')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.tight_layout()
    
    plt.savefig('grafic_toti_algoritmii.png')
    print("Salvat grafic_toti_algoritmii.png")

if __name__ == "__main__":
    try:
        plot_all_9_log()
        print("\n[OK] Graficul cu toti cei 9 algoritmi a fost generat.")
    except Exception as e:
        print(f"Eroare: {e}")
