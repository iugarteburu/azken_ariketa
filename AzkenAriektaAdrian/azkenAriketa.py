"""
Leer un archivo txt y decir lo siguiente:
    - pedirle al usuario que especifique el nombre del fitxero que se va a leer

    - contar cuántas veces aparece la palabra qye nosotros digamos
    - imprimir la última fila del fichero
    - sustituir una palabra por otra (replace)
"""

import csv

from csv import reader

with open('employee.txt', mode='r') as f:   #with oper -> sartu fitxategiaren izena
    lerroak = f.readlines()
    aukera = "0"

    while not (aukera == -1):
        print("\n1. Contar X palabra en el fichero: ")
        print("2. Imprimir la última fila del fichero: ")
        print("3. Sustituir una palabra por otra. ")
        aukera = int(input("\nSartu aukera bat:"))

        if aukera == 1:
            palabra = input("\nQué palabra quieres buscar? ")
            numPalabra = 0
            for i in lerroak:
                numPalabra += i.count(palabra)
            print("La palabra elegida aparece " + str(numPalabra) + " veces. ")
        elif (aukera == 2):
            print(lerroak[len(lerroak) - 1])
        elif (aukera == 3): #buscar soldataAldatu()
            ordezkatu = input("Zein hitz nahi duzu aldatu? ")

            text = text.replace("Ermua", "Paris")



"""
ver todos los datos -> una vez cambiados
line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'\nColumn names are {", ".join(row)}')
                line_count += 1
            print(
                f'\t{row["Zbki"]}, Bere adina: {row["Adina"]}, {row["Generoa"]}, {row["Soldata"]}, {row["Hileko_gastuak"]}, {row["Lanpostua"]}, {row["Kirola"]}, {row["Izena"]}, {row["Abizeba"]}, {row["Herria"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')
"""