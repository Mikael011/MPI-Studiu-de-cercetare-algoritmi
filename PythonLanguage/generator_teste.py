import random   
import string    
import os       

FOLDER_TESTE = "teste_input"

if not os.path.exists(FOLDER_TESTE):
    os.makedirs(FOLDER_TESTE)

def generează_string_aleator(lungime=5):
    return ''.join(random.choices(string.ascii_lowercase, k=lungime))

def scrie_test(f, tip, desc, date):
    f.write(f"\n# TIP: {tip} | DESC: {desc}\n")
    f.write(" ".join(map(str, date)) + "\n")

def generează_fișier_complex(nume_fișier, dimensiune): 
    cale = os.path.join(FOLDER_TESTE, nume_fișier)
    with open(cale, 'w', encoding='utf-8') as f:
        print(f"Se genereaza {nume_fișier} ({dimensiune} elemente)...")

        scrie_test(f, 'int', 'Aleator', [random.randint(-10000, 10000) for _ in range(dimensiune)])

        scrie_test(f, 'int', 'Sortat Crescător', sorted([random.randint(-10000, 10000) for _ in range(dimensiune)]))

        scrie_test(f, 'int', 'Sortat Descrescător', sorted([random.randint(-10000, 10000) for _ in range(dimensiune)], reverse=True))

        date_aproape = sorted([random.randint(-10000, 10000) for _ in range(dimensiune)])
        numar_schimbari = max(1, dimensiune // 20) 
        for _ in range(numar_schimbari):
            idx1 = random.randint(0, dimensiune - 1)
            idx2 = random.randint(0, dimensiune - 1)
            date_aproape[idx1], date_aproape[idx2] = date_aproape[idx2], date_aproape[idx1]
        scrie_test(f, 'int', 'Aproape Sortat', date_aproape)

        scrie_test(f, 'int', 'Constant (Plat)', [42] * dimensiune)

        scrie_test(f, 'float', 'Float Aleator', [round(random.uniform(-1000.0, 1000.0), 2) for _ in range(dimensiune)])
        
        if dimensiune <= 50000:
            scrie_test(f, 'string', 'String Aleator', [generează_string_aleator() for _ in range(dimensiune)])

def main():
    generează_fișier_complex("dim_mica.txt", 100)    
    generează_fișier_complex("dim_medie.txt", 1000)    
    generează_fișier_complex("dim_mare.txt", 10000)    
    generează_fișier_complex("dim_gigant.txt", 100000) 

    print("\n[OK] Toate fisierele de test au fost generate in 'teste_input'.")

if __name__ == "__main__":
    main()
