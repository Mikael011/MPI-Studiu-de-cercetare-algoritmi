"""""

BENEFICII:
1. Curățenia Codului: Fișierul 'main.py' rămâne scurt și ușor de citit.
2. Reutilizare: Putem folosi aceeași funcție de măsurare a timpului pentru toți cei 
   9 algoritmi, fără a scrie cod duplicat în fiecare fișier.
3. Modularitate: Dacă vrem să schimbăm modul în care măsurăm memoria, modificăm 
   într-un singur loc (aici), iar restul programului va beneficia automat.
"""

import time          
import tracemalloc   

def evaluare_performanță(funcție_sortare, date):
  
    date_copie = date.copy()        
    tracemalloc.start()             
    
    început = time.perf_counter()   
    
    rezultat = funcție_sortare(date_copie)  
    
    if rezultat is None:
        rezultat = date_copie
        
    sfârșit = time.perf_counter() 
    

    curent, vârf = tracemalloc.get_traced_memory()
    tracemalloc.stop()              
    
    timp_scurs = sfârșit - început 
    memorie_vârf_kb = vârf / 1024   
    
    return rezultat, timp_scurs, memorie_vârf_kb  

def este_sortat(date):

    if not isinstance(date, list) or len(date) < 2: 
        return True
    
    return all(date[i] <= date[i+1] for i in range(len(date)-1))

def citește_listă(tip_date):
    
    intrare = input("\nIntrodu elementele listei separate prin spațiu: ")

    elemente = intrare.split()
    
    if not elemente:              
        print("Eroare: Lista este goală!")
        return None
        
    try:
        
        if tip_date == 'int':
            return [int(x) for x in elemente]     
        elif tip_date == 'float':
            return [float(x) for x in elemente]   
        else:
            return elemente 
    except ValueError:
        print(f"Eroare: Unul sau mai multe elemente nu corespund tipului '{tip_date}'!")
        return None

def citește_din_fișier(cale_fișier):

    cazuri_test = []
    try:
        with open(cale_fișier, 'r', encoding='utf-8') as f:
            linii = f.readlines()
            
        curent_tip = 'int'
        curent_desc = 'Implicit'
        curent_date_str = []
        
        def procesează_lista_acumulată():
            if curent_date_str:
                try:
                    if curent_tip == 'int':
                        date = [int(x) for x in curent_date_str]
                    elif curent_tip == 'float':
                        date = [float(x) for x in curent_date_str]
                    else:
                        date = curent_date_str
                    cazuri_test.append({'date': date, 'tip': curent_tip, 'desc': curent_desc})
                except ValueError:
                    print(f"Avertisment: Eroare conversie în {cale_fișier} pentru testul {curent_desc}")

        for linie in linii:
            linie = linie.strip()
            if not linie: continue
            
            if linie.startswith('#'):
                procesează_lista_acumulată()
                curent_date_str = []

                părți = linie.replace('#', '').split('|')
                for p in părți:
                    if 'TIP:' in p: curent_tip = p.split(':')[1].strip().lower()
                    if 'DESC:' in p: curent_desc = p.split(':')[1].strip()
            else:
                curent_date_str.extend(linie.split())

        procesează_lista_acumulată()
        
        if not cazuri_test:
            return None, 
        return cazuri_test, None

    except FileNotFoundError:
        return None, f"Fișierul '{cale_fișier}' nu a fost găsit!"
    except Exception as e:
        return None, f"Eroare: {str(e)}"

def scrie_în_fișier(cale_fișier, nume_algoritm, rezultat, timp, memorie, mod='a'):

    try:
        with open(cale_fișier, mod, encoding='utf-8') as f:
            f.write(f"\n--- REZULTAT {nume_algoritm} ---\n")
            f.write(f"Listă sortată: {rezultat}\n")
            f.write(f"Timp execuție: {timp:.8f} secunde\n")
            f.write(f"Memorie folosită: {memorie:.4f} KB\n")
            f.write("-" * 30 + "\n")
        return True
    except Exception as e:
        print(f"Eroare la scrierea în fișier: {e}")
        return False
