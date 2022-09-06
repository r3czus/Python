def DemoPrint():
    """
    dokumentacja
    opis dzialania
    opis parametru
    :return:opis zwracanej wartosci
    """
    for i in range(5):
        print("Witaj", "świecie")
    print(["witaj", "świecie"])
    print("witam")
    print("Witaj", 'cyt "Adam malysz"', sep=", ")#separator sluzy do okreslenia czym beda odzielane wypisywane tresci

    imiona = ['Kamil', 'Oskar', 'Bartek', 'Miłosz']
    print(imiona, sep=", ")
    #print(argumenty wprowadzane, argumenty nazwane(dzieki temu ze zaczyna sie na sep to jest odpowiednio traktowane)

    print(*imiona, sep=", ")#pytonizm *rozbija strukture pozwala na uzycie separator

    [print(x) for x in imiona]#for w jednej linice

    print("-*-"*20)
    print("""
    tekst wielolinijkowy
    tutaj kolejna linika
        tutaj wciecie
        a tutaj kolejne wciecie
        mozna uzywac jako komentarz wielolinijkowy
    """)
    #tekst wielolinjowy mozna uzyc jako komentarz wielkolinjowy
    for x in imiona:
        print(x)

    print(*imiona, sep=", ", end=".\n")
    #argument nazwany end decyduje o tym co jest na koncu

    plik = open(r'files/dane.txt', 'w', encoding='utf-8')
    #otwieranie pliku typ w=write encoding=typ kodowania znakow
    print(*imiona, sep=";", file=plik)
    #zapsujemy dane w pliku sep=separtaor to czym maja byc odzielone zmienne file=wybrany otwarty plik
    plik.close()
    #zamykamy plik