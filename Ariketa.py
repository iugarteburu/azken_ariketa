izena = input("Sartu txt fitxategi baten izena irakurtzeko: ")

izena = "txt.txt"

f = open(izena, 'r')
mensaje = f.read()
print(mensaje)
f.close()

#Azken esaldia irakurri .rfind()
if len(mensaje) == '.':
    mensaje





    #azken ariketa: Ordeztu testuko hitz bat beste bategatik replace()