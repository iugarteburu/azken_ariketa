
line_count = 0
#automatikoki sartuta dago fitxategia ez dau ezertarako balio galderak
fitxategia=input('Zein fitxategi nahi duzu irakurri? ')
testua2= 'kaixo Markel Naiz'

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


def ordezkatuChar():
    cambio = input('Sartu ordezkatu nahi ez duzun letra:')
    for i in testua2:
        for j in range(len(i)):
            if i[j] == " " :
                print(' ',end='')
            elif i[j] != cambio:
                print('*', end='')
            elif i[j] == cambio:
                print(cambio, end='')
    print()

def hurrengoaOrdezkatu():
   #ascci taula erabili behar da
    #chr(letra+1)
    for i in testua2:
        for j in range(len(i)):
            if i[j] == " ":
                print(' ', end='')
            elif i[j] == 'z':
                hurrengoa = chr(97)
                print(str(hurrengoa), end='')
            elif i[j] == 'Z':
                hurrengoa = chr(97)
                print(str(hurrengoa), end='')
            elif i[j] != 'Z' or i[j] != 'z':
                oraingoa = ord(i[j])
                hurrengoa = chr(oraingoa+1)
                print(str(hurrengoa), end='')
    print()

print('MENUA ')
print('================')
print('a) Kontatu Hitza')
print('b) Azken esaldia pantailaratu')
print('c) Ordezkatu hitza')
print('d) Ordezkatu letrak')
print('e) Hurrengo Ordezkatu')
print('f) Irten')


aukera = input('Sartu aukera bat: ').lower()

while aukera != 'f':
    if aukera == 'a':
        hitzaBilatu()
    if aukera == 'b':
        azkenEsaldia()
    if aukera == 'c':
        hitzaOrdezkatu()
    if aukera == 'd':
        ordezkatuChar()
    if aukera == 'e':
        hurrengoaOrdezkatu()

    aukera = input('Sartu aukera bat: ').lower()

