with open('fitxategiAriketa.txt') as f:
    lerroak = f.readlines()
    aukera = "0"

    while int(aukera) != -1:
        print("1.Hitz bat kontatu")
        print("2.Fitxategiko azken esaldia pantailaratu")
        print("3.Hitz bat ordezkatu")
        aukera = input("Sartu zenbaki bat(-1 amaitzeko): ")

        if int(aukera) == 1:
            hitza = input("Sartu kontatu nahi duzun hitza: ")
            hitzKopurua = 0
            for i in lerroak:
                hitzKopurua += i.count(hitza)
            print(hitza + " hitza " + str(hitzKopurua) + " aldiz agertzen da")
        elif int(aukera) == 2:
            print(lerroak[len(lerroak)-1])
        elif int(aukera) == 3:
            hitzBerria = input("Sartu hitz berria: ")
            hitzZaharra = input("Sartu ordezkatu nahi duzun hitza: ")
            for i in lerroak:
                print(i.replace(hitzZaharra,hitzBerria))
        print("---------------")
