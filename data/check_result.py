#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys
import string
from math import sqrt
 # Wywołania: " python oblicz.py nazwa_pliku_macierzy nazwa_pliku_z_wynikiem" (np.: "python oblicz.py berlin52.txt wyniki.txt")

rang = 52
def zbudujMacierz(wiersze):
    macierz = [[0 for col in range(rang)] for row in range(rang)]
    i = 0
    for w in wiersze[1:]:
        w = w.strip().split(' ')
        j = 0
        for odl in w:
            macierz[i][j] = int(odl)
            macierz[j][i] = int(odl)
            j+=1
        i+=1
    return macierz

def obliczOdleglosc(trasa, macierz):
    odleglosc = 0
    trasa = trasa.strip().split('-')
    try:
        trasa = list(map(int, trasa))
    except ValueError:
        pass
    for i in range(len(trasa)-1):
        odleglosc+=macierz[trasa[i]][trasa[i+1]]
    odleglosc+=macierz[trasa[len(trasa)-1]][trasa[0]]
    return odleglosc, trasa

nPliku = sys.argv[1]
nPlikuWynikow = sys.argv[2]

plikWe = open(nPliku, 'r') # Otwarcie pliku wejściowego
plikWe2 = open(nPlikuWynikow, 'r') # Otwarcie pliku wejściowego wyników

plikWy = open('spr_'+nPliku.split('.')[0]+'.txt', 'w') # Stworzenie nowego pliku (wyjściowego) o tej samej nazwie, co wejściowy, ale z rozszerzeniem .txt

wiersze = plikWe.readlines()
plikWe.close()

macierz = zbudujMacierz(wiersze)

wyniki = plikWe2.readlines()
plikWe2.close()

#minimum = sys.maxint
for w in wyniki:
    odleglosc = 0
    w = w.strip().split(' ')
    if len(w)==2:
        odleglosc, trasa = obliczOdleglosc(w[0], macierz)

        flaga = True
        if len(trasa) != int(rang):
            flaga = False

        i=0
        trasa.sort()
        for el in trasa:
            if el!=i:
                flaga = False
            i+=1

#        if odleglosc<minimum:
#            minimum=odleglosc
        wynik = "%i %i %s %s" % (odleglosc, int(w[1]), "Odległość: "+str(odleglosc==int(w[1])), "Trasa: "+str(flaga))
    else:
        wynik = "Pominięto: %s" % w
    print(wynik)
    plikWy.write(wynik+'\n')
       
plikWy.close()
#print(minimum)
