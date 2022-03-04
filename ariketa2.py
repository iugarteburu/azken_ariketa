
fitxategia = input('Zein fitxategi nahi duzu irakurri? ')
testua2 = 'Kaixo markel naiz'
#automatikoki fitxategia.txt
with open('Fitxategia1.txt', mode='r') as f:
    testua = f.readlines()
    testua3 = list(testua)

#Zuk aukeratzeko fitxategia
#with open(fitxategia, mode='r') as f:
#    testua = f.readlines()


def deskodetu():
    # ascci taula erabili behar da
    for i in testua3:
        for j in range(len(i)):
            if i[j] == " ":
                print(' ', end='')
            elif i[j] == 'a':
                hurrengoa = chr(122)
                print(str(hurrengoa), end='')
            elif i[j] == 'A':
                hurrengoa = chr(122)
                print(str(hurrengoa), end='')
            elif i[j] != 'A' or i[j] != 'a':
                oraingoa = ord(i[j])
                hurrengoa = chr(oraingoa - 1)
                print(str(hurrengoa), end='')
    print()


def kodetu():
    for i in testua3:
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


def gordeAldaketak():
    with open('fitxategia1.txt', mode='w') as g:
        write = g.write()
        write.writerows(testua3)

print('MENUA ')
print('================')
print('a) Dekodetu')
print('b) Kodetu')
print('c) Gorde')
print('f) Irten')


aukera = input('Sartu aukera bat: ').lower()

while aukera != 'f':
    if aukera == 'a':
        deskodetu()
    if aukera == 'b':
        kodetu()
    if aukera == 'c':
        gordeAldaketak()

    aukera = input('Sartu aukera bat: ').lower()