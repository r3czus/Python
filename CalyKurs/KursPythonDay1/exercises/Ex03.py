def LudzieWSzafkach():
    import shelve
    plik = shelve.open(r'Files\dane_ludzie.dat')
    plik['Adam'] = ['Adam','Małsz',68033154914]
    plik['Kaziu'] = ['Bartosz','Kunicki',72010866459]
    plik['Nikodem'] = ['Kuba','Kowalski',51022591296]

    plik.sync()
    plik.close()
    # odczyt z plikow shelve
    p = shelve.open(r'Files\dane_ludzie.dat')
    print(f"Człek{p['Adam']}")
    print(f"Człek{p['Kaziu']}")
    print(f"Człek{p['Nikodem']}")

def Filmoteka():
    from xml.etree.ElementTree import Element, ElementTree, SubElement, parse, dump
    import os
    while True:
        print("Witma w mojej superowej aplikacji")
        wybor = input("\n1 - Dodaj Film\n2 - Wyświetl Filmy\n3 - Zabij mnie\n")
        if wybor == "1":
            rezyser = input("Prosze podac rezysera filmu\n")
            tytul = input("Prosze podac tytul filmu\n")
            rok = input("Prosze podac rok wydania filmu\n")
            gatunek = input("Prosze podac gatunek filmu\n")
            if os.path.exists(os.getcwd() + r'\Files/film.xml'):
                literatura = parse(r'Files\film.xml')
                r = literatura.getroot()
                film = SubElement(r, 'book', gatunek=gatunek)
                SubElement(film, 'rezyser').text = rezyser
                SubElement(film, 'tytuł').text = tytul
                SubElement(film, 'rok').text = rok
                SubElement(film, 'gatunek').text = gatunek
                ElementTree(r).write(r'Files\film.xml', encoding="UTF-8", xml_declaration=True, method='xml')
        elif wybor == "2":
            dane = parse(r'Files\film.xml')
            filmy = dane.getroot()
            filmy = filmy.findall('book')
            print("^*" * 50)
            for b in filmy:
                rez = b.find('rezyser').text
                ty = b.find('tytuł').text
                roczek = b.find('rok').text
                ga = b.find('gatunek').text
                print(f"Filmz gatunku {ga} pt''{ty}'' wyrezyserowany przez {rez} w:{roczek}")
        else:
            import sys
            print("Naura")
            sys.exit()