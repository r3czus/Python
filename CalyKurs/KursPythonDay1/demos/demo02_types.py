def Basic_types():
    print("demo typów prostych - podstawowy")
    #teksty
    imie="Janusz"
    print(type(imie))

    #liczby
    liczba = 3
    print(type(liczba))
    liczba = 3.0
    print(type(liczba))
    liczba = 3.0+4.7j
    print(type(liczba))
    print(liczba.real, liczba.imag, type(liczba))

    import math # biblioteka mathmath dla normalnych liczb

    import cmath # biblioteka mathmath dla liczb urojonych

    #boolean
    info = True
    print("jestem bogaty" if info else "nie jestem bogaty") #operator tenarny zazwyczaj sie pisze w 1 linice
    # funkcja if w jednej linice jeszcze w princie

def Typy_Kolekcyjne():
    #listy
    imiona = [] #deklaracja pustego elementu
    imiona2 = list(("Paweł", "Mikołaj")) #deklaracja pustej listy - przez konstuktor/konwerter
    imiona3 = list({'Dawid R', 'Dawid K', 'Dawid L'})
    print(imiona2)
    print(*imiona2, sep=", ")

    osoba=["Darek", "Pieter", 1.87, 95,('Python','C#', 'SQL')]

    for x in osoba:
        print(f"{x} jest typu {type(x)}")#f formatuje

    print(imiona3)
    print(*imiona3)
    imiona3.append("Bartosz")
    print(*imiona3, sep=", ")
    print(imiona3[3])


    #krotki - tuple
    imiona = ('Kamil', )
    skills = tuple({'kurier', 'gamer', 'muzyka'})
    print(skills, type(skills))

    #set - zbiory
    imionaL = {"Ola", "Agnieszka ", "Bogumiła"}
    print(imionaL, type(imionaL))

    imionaP = {"Bogumiła", "Anna", "Martyna"}
    imionaP.add("Sylwia")
    print(imionaP, type(imionaP))
    #set to zbior
    #dodawanie do zbioru
    print(imionaL.intersection(imionaP))

    #frozenset = statycznyzbior
    imionaP_F = frozenset(imionaP)
    imionaL_F = frozenset(imionaL)
    print(*imionaP_F, type(imionaP_F))

    #typ mapujacy
    osoba ={'imię':'Grazyna',
            'dzieci':['Pioter','Karyna']}
    #slownik ma klucze zamiast indeksow slownik=dictionary

    print(osoba,type(osoba))

    # one line code
    [print(x) for x in osoba.keys()]#keys wypisuje dostepne klucze slownika
    print('\n')
    [print(x) for x in osoba.values()]#values wypisuje wszystkie wartosci slownika

def Typy_Binarne():
    tekstBin = b'Hello' # zmiennna binarna
    print(tekstBin)

    tekstBinArr =bytearray(56)#tablica binarna
    print(tekstBinArr)

    tekstPamięć = memoryview(bytes(56))#miejsce w pamieci
    print(tekstPamięć)

    print(id((tekstBin)))#id zwraca numery pamieciowe gdzie znajduje sie obiekt