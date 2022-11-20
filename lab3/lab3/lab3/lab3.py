import time
import random


#klasa z licznikiem
class Licznik:
    czas = []          #trzymanie danych 
    czas_sr = 0        #średni
    czas_poj = 0       #pojedynczy
    czas_min = 0       #najkrótszy
    czas_max = 0       #najdłuższy
    

    def __init__(self, func):
        self.func = func
 
    def __call__(self, *args, **kwargs):
        start_time = time.time()

        result = self.func(*args, **kwargs)

        end_time = time.time()


        #licznenie czasu
        Licznik.czas_poj = end_time - start_time
        Licznik.czas.append(Licznik.czas_poj)

        Licznik.czas.sort()
        Licznik.czas_min = min(Licznik.czas)
        Licznik.czas_max = max(Licznik.czas)
        Licznik.czas_sr= sum(Licznik.czas) / len(Licznik.czas)

        print()
        print('Poj:', Licznik.czas_poj)
        print('Sredni:', Licznik.czas_sr)
        print('Min:', Licznik.czas_min)
        print('Max:', Licznik.czas_max)
        print()

        return result



@Licznik
def losowy1(delay):
    from time import sleep
    sleep(delay)
 
losowy1(random.randint(2, 4))



@Licznik
def losowy2(delay):
    from time import sleep
    sleep(delay)
 
losowy2(random.randint(2, 4))



@Licznik
def losowy3(delay):
    from time import sleep
    sleep(delay)
 
losowy3(random.randint(2, 4))