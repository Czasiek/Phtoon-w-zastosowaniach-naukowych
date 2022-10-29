from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import rich
from rich.progress import track
import argparse

#nazwa ksiazki znajdujaca sie w katalogu pliku
plik = 'ksiazka.txt'

#ile wyrazow chcemy wyswietlic
ilosc = 10 

#słowinik
slownik={}
znaki_zakazane=['…', '-', '—', '+', '"', '^', '&', '[', '}', '{', '}', ',', '.', '!', '?', ';', ':', '*', '(', ')']


#zczytywanie pliku
wlasciwosci = argparse.ArgumentParser()
wlasciwosci.add_argument('-l', '--dlugosc', default = 0, required = False)
dane = wlasciwosci.parse_args()
dlugosc = dane.dlugosc


with rich.progress.open(plik, 'r', encoding='utf8') as a:
    for linia in a:
        #usuniecie znakow zakazanych    
        for i in range(len(znaki_zakazane)):
            linia=linia.replace(znaki_zakazane[i], '') 

        
        linia = linia.split() #usuwanie niepotrzebnych spacji
        for slowo in linia:
            if len(slowo) > int(dlugosc):
                #liczenie wartosci w slowniku
                slownik[slowo] = slownik.get(slowo, 0) + 1 

#dalesze zliczanie
counts = dict(Counter(slownik).most_common(ilosc))
labels, values = zip(*counts.items())

# sortuje wartości od największego do najmniejszego
indSort = np.argsort(values)[::-1]

# zarządanie danymi
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]
indexes = np.arange(len(labels))
bar_width = 0.35

plt.bar(indexes, values)

# podpisy do osi
plt.xticks(indexes + bar_width, labels)
plt.show()