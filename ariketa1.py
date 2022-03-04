# langileak.csv
# zbkia, izena, soldata...
#    - Listetan kargatu python bidez
#   - Listetan bilaketak egin. Menu baten bidez, Adibidez:

# -xxx Izena duten langileak
# -xxx baino gehiago irabazten duten langileak
import csv

from csv import reader


import pandas as pd

line_count = 0
fitxategia=input('Zein fitxategi nahi duzu irakurri? ')

with open('fitxategia1.txt', mode='r') as f:
    testua = f.readlines()


def hitzaBilatu():

    count = 0
    hitza = input("Sartu hitza:")

    for row in testua:
        count += row.count(hitza)

    print(count)

def azkenEsaldia():
    print(testua[len(testua) -1])


def hitzaOrdezkatu():
    global line_count

    cambio = input('Sartu ordezkatu nahi duzun hitza:')
    berria = input('Sartu hitz berria:')
    for i in testua:
        print(i.replace(cambio, berria))

print('MENUA ')
print('================')
print('a) Kontatu Hitza')
print('b) Azken esaldia pantailaratu')
print('c) Ordezkatu hitza')
print('d) Irten')


aukera = input('Sartu aukera bat: ').lower()

while aukera != 'd':
    if aukera == 'a':
        hitzaBilatu()
    if aukera == 'b':
        azkenEsaldia()
    if aukera == 'c':
        hitzaOrdezkatu()

    aukera = input('Sartu aukera bat: ').lower()

