def Pliki():
    while(True):
        odp = input("Zapis do pliku txt danych podanych w konsoli\n1 - podaj dane do zapisu\n2-odczytaj dane z txt\n3 - zapis danych do CSV\n4 - odczyt danych CSV\n5 - Proste pliki binarne\n6 - Pliki binarne - pickle, shelve\n7 - Pliki .xml\nK-koniec\n")
        if odp=="1":
            print("^*"*30)
            dane = input("Podaj dane do zapisu w pliku\n")
            plik = open(r'Files/dane_osobowe.txt','a',encoding="UTF-8")
            plik.write(dane+"\n")
            plik.close()
        elif odp=="2":
            print("^*" * 30)
            with open(r'Files/dane_osobowe.txt','r',encoding="UTF-8") as plik:
                for l in plik:
                    print(l.rstrip("\n"))
        elif odp=="3":
            print("^*" * 30)
            import os, csv
            # print(os.__doc__)
            if os.path.exists(os.getcwd()+r'\Files/dane_firmowe'):
                pass
            else:
                os.mkdir(os.getcwd() + r'\Files/dane_firmowe')

            imie = input("Podaj imie\n")
            nazwisko = input("Podaj nazwisko\n")
            pesel = input("Podaj pesel\n")
            with open(r'Files\dane_firmowe\osoby.csv', 'a', encoding="UTF-8") as plik:
                print(imie, nazwisko, pesel, sep=":", file=plik)
            print("^*" * 30)
            with open(r'Files\dane_firmowe\osoby_lib_csv.csv', 'a', encoding="UTF-8") as plik_csv:
                zapis_csv = csv.writer(plik_csv, delimiter=",")
                zapis_csv.writerow([imie,nazwisko,pesel])
            if os.path.exists(r"\Files\dane_firmowe\osoby_lib_dict"):
                nowy_plik=True
            else:
                nowy_plik=False
            print("^*" * 30)
            with open(r'Files\dane_firmowe\osoby_lib_dict.csv', 'a', encoding="UTF-8") as plik_dict:
                nazwy_kolumn = ["imie","nazwisko","pesel"]
                csv_writer = csv.DictWriter(plik_dict, fieldnames=nazwy_kolumn)
                if nowy_plik==True:
                    csv_writer.writeheader()
                csv_writer.writerow({'imie':imie,'nazwisko':nazwisko,'pesel':pesel})
        elif odp=="4":
            print("^*" * 30)
            from libs.tools.PersonalAnalysing import GenderFromPesel, DateFromPesel
            import os, csv
            if os.path.exists(os.getcwd()+r'\Files/dane_firmowe/osoby.csv'):
                print("test")
                with open(r'Files/dane_firmowe/osoby.csv', 'r', encoding="UTF-8") as plik:
                    for l in plik:
                        dane = l.split(":")
                        try:
                            pesel = dane[2].rstrip('\n')
                            print(f"{dane[0]} {dane[1]} to {GenderFromPesel(pesel)}")
                            print(f"{'urodzona' if GenderFromPesel(pesel) == 'dziewczynka' else 'urodzony'}")
                            print(f"{DateFromPesel(pesel)}")
                        except Exception as e:
                            print(e)
            print("^*" * 30)
            if os.path.exists(os.getcwd()+r'\Files/dane_firmowe/osoby_lib_csv.csv'):
                print("test")
                with open(r'Files/dane_firmowe/osoby_lib_csv.csv', 'r', encoding="UTF-8") as plik:
                    csv_reader = csv.reader(plik, delimiter=',')

                    for dane in csv_reader:
                        if(len(dane)) > 0:
                            try:
                                pesel = dane[2].rstrip('\n')
                                print(f"{dane[0]} {dane[1]} to {GenderFromPesel(pesel)}")
                                print(f"{'urodzona' if GenderFromPesel(pesel) == 'dziewczynka' else 'urodzony'}")
                                print(f"{DateFromPesel(pesel)}")
                            except Exception as e:
                                print(e)
            print("^*" * 30)
            if os.path.exists(os.getcwd()+r'\Files/dane_firmowe/osoby_lib_dict.csv'):
                with open(r'Files\dane_firmowe\osoby_lib_dict.csv', 'r', encoding="UTF-8") as plik_dict:
                    csv_reader = csv.DictReader(plik_dict)
                    for w in csv_reader:
                        try:
                            pesel = w['pesel'].rstrip('\n')
                            print(f"{w['imie']} {w['nazwisko']} to {GenderFromPesel(pesel)}")
                            print(f"{'urodzona' if GenderFromPesel(pesel) == 'dziewczynka' else 'urodzony'}")
                            print(f"{DateFromPesel(pesel)}")
                        except Exception as e:
                            print(e)
        elif odp=="5":
            plik = open(r'Files/dane_binarne.bin','wb')
            liczba = [123 , 56.6, '123.5', ' exit', ' open', 'run', {'Skills':['czta','muwi','je']}]
            plik.write(f"{bytes(liczba[0])};{liczba[1]}'{liczba[2]}".encode("UTF-8"))
            plik.close()
            plik_odczyt = open(r'Files/dane_binarne.bin','rb')
            print(plik_odczyt)
            for w in plik_odczyt:
                print(w)
        elif odp=="6":
            import pickle
            print("zapisz przepisó na przetwory domowe")
            sposób = ['kwaszenie', "kiszenie", "konserwowanie", "marynowanie"]
            kształt_warzywa = ['całe', "ćwiartki", "plasterki"]
            producent = ["swoje", "pudzliszki", "rolnik", "motyl", "dawtona"]
            with open(r"Files/przetwory.dat", "wb") as plik:
                pickle.dump(sposób,plik)
                pickle.dump(kształt_warzywa,plik)
                pickle.dump(producent,plik)

            with open(r"Files/przetwory.dat", "rb") as plik:
                spos = pickle.load(plik)
                kszt = pickle.load(plik)
                prod = pickle.load(plik)
                print("Sposoby:", end=' ')
                print(*spos, sep=', ')
                print("Ksztalt:", end=' ')
                print(*kszt, sep=', ')
                print("Producent:", end=' ')
                print(*prod, sep=', ')

            import shelve
            plik=shelve.open(r'Files\dane_sh.dat')#zapis w plikach shelve
            print("zapis przepisó na przetwory domowe - shelve")
            plik['sposob'] = ['kwaszenie', "kiszenie", "konserwowanie", "marynowanie"]
            plik['ksztalt_warzywa'] = ['całe', "ćwiartki", "plasterki"]
            plik['producent'] = ["swoje", "pudzliszki", "rolnik", "motyl", "dawtona"]
            plik.sync()
            plik.close()
            #odczyt z plikow shelve
            p= shelve.open(r'Files\dane_sh.dat')
            print(f"Ksztalty warzyw{p['ksztalt_warzywa']}")
            print(f"Sposob{p['sposob']}")
            print(f"producent{p['producent']}")
        elif odp=="7":
            from  xml.etree.ElementTree import Element, ElementTree,SubElement,parse,dump
            root = Element("books")
            book = SubElement(root,'book', kategoria="lektora")
            SubElement(book, 'tytuł').text = "Wesele"
            cena = SubElement(book, "cena")
            cena.text='30'
            cena.attrib['waluta'] = "PLN"
            SubElement(book, 'autor').text = "Stanisław Wyspiański"

            book = SubElement(root, 'book', kategoria="sf")
            SubElement(book, 'tytuł').text = "Player One"
            cena = SubElement(book, "cena")
            cena.text = '12.5'
            cena.attrib['waluta'] = "EUR"
            SubElement(book, 'autor').text = "Ernest Cline"
            ElementTree(root).write(r'Files\books.xml',encoding="UTF-8",xml_declaration=True,method='xml')
            daneXML= parse(r'Files\books.xml')
            ksiazki=daneXML.getroot()
            # print(ksiazki)
            # for i in ksiazki.iter():
            #     dump(i)
            for i in ksiazki:
                # print(i.tag, i.attrib,i.text)
                autor = ""
                tytul = ""
                for k in i:
                    # print(k.tag, k.attrib, k.text)
                    if k.tag=="autor":
                        autor = k.text
                    if k.tag=="tytuł":
                        tytul = k.text
                print(f"{autor} napisał {tytul}")
            ksiazki = ksiazki.findall('book')
            print("^*"*50)
            for b in ksiazki:
                tytul = b.find('tytuł').text
                autor = b.find('autor').text
                cena = b.find('cena')
                wartosc = cena.text
                waluta = cena.get('waluta')
                print(f"{autor} napisał {tytul} ktore kosztuje:{wartosc}{waluta}")
            literatura = parse(r'Files\books.xml')
            r=literatura.getroot()
            book = SubElement(r, 'book', kategoria="fantsy")
            SubElement(book, 'tytuł').text = "Wiedzmin"
            cena = SubElement(book, "cena")
            cena.text = '11'
            cena.attrib['waluta'] = "EUR"
            SubElement(book, 'autor').text = "Andrzej Sapkowski"
            ElementTree(r).write(r'Files\books.xml', encoding="UTF-8", xml_declaration=True, method='xml')

        else:
            import sys
            print("do widzenia")
            sys.exit()