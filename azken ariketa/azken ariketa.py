# Erabiltzaileari fitxategi izena eskatu eta fitxategia irakurri
# Menua:
# Kontatu zenbatetan dagoen nik nahi dudan hitza
# Fitxategiko azken esaldia pantailaratu
# Ordeztu testuko hitz bat beste batengatik (replace)
# Ordeztu erabiltzaileak sartutako letra ez beste guztiak * batengatik
# Kodetu testua eta ordeztu letra bakoitza bere hurrengoagatik


def kontatuHitza():
    palabra = input("Diga qué palabra quiere buscar: ")
    f = open("texto.csv")
    libro = f.read()
    n = libro.count(palabra)
    f.close()
    print("En el texto la palabra ", palabra, " aparece ", n, " veces.")


def azkenEsaldia():
    with open('texto.csv', 'r') as f:
        for line in f:
            pass
        last_line = line
    print("La ultima frase es esta: ", last_line)


def ordeztuHitza():
    s = str(input("Zer nahi duzu ordeztu?"))
    z = str(input("Sartu hitz berria: "))
    with open('texto.csv', 'r') as f:
        for line in f:
            print(line.replace(s,z))
            
def ordeztuAst():
    s = str(input("Sartu nahi duzun hitza:"))
    with open ('texto.csv', 'r') as f:
        for line in f:
            for j in range(len(line)):
                if line[j]== " ":
                    print(" ",end=" ")
                elif line[j] != s:
                    print("*", end=" ")
                elif line[j]== s:
                    print(s,end=" ")
            print()

def Menua():
    print("1-Kontatu zenbatetan dagoen nik nahi dudan hitza")
    print("2-Fitxategiko azken esaldia pantailaratu")
    print("3-Ordeztu testuko hitz bat beste batengatik (replace)")
    print("4-Ordeztu sartutako letra ez beste guztiak * batengatik")
    aukera = int(input("Zer egin nahi duzu?"))
    if aukera == 1:
        kontatuHitza()
    if aukera == 2:
        azkenEsaldia()
    if aukera == 3:
        ordeztuHitza()
    if aukera == 4:
        ordeztuAst()
Menua()