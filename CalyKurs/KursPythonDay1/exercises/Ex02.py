def Test_RozpoczecieDnia():
    while True:
        from libs.tools.Testy import TestNumber, TestLiczb
        print("Co chesz robic")
        print("1[Policz funkcje kwadratowa]")
        print("2[Policz 2 niewiadome]")
        print("K[Wyjdz]")
        odp=input()
        if odp=="1":
            from libs.mathmath.kola import FunkcjaKwadratowa
            a=input()
            b=input()
            c=input()
            if TestLiczb(a, b, c):
                a = float(a)
                b = float(b)
                c = float(c)
                try:
                        x, y = FunkcjaKwadratowa(a, b, c)
                        print(f"x1={x:.2f}\nx2={y:.2f}")
                except Exception as e:
                    print(e)
            else:
                print("Wszystkie podane dane nie sa liczbą")
        elif odp=="2":
            from libs.mathmath.kola import MetodaWyznacznikow
            a = input()
            b = input()
            c = input()
            d = input()
            e = input()
            f = input()
            if TestLiczb(a, b, c, d, e, f):
                a = float(a)
                b = float(b)
                c = float(c)
                d = float(d)
                e = float(e)
                f = float(f)
                try:
                    x, y = MetodaWyznacznikow(a, b, c, d, e, f)
                    print(f"x1={x:.2f}\nx2={y:.2f}")
                except Exception as e:
                    print(e)
            else:
                print("Wszystkie podane dane nie sa liczbą")
        else:
            print("Do zobaczenie")
            import sys
            sys.exit()

def Test_Kolo():
    from libs.tools.Testy import TestNumber
    from libs.mathmath.kola import Kolo
    while True:
        print("Kolo")
        typ = input("co obliczamy\n1-obowd\n2-pole\n")
        try:
            promien = input("Podaj promien kola\n")
            if TestNumber(promien):
                if typ == "1":
                    print(f"Obówd koła o promieniu {promien} wynosi: {Kolo(float(promien), typ='obwod')}")
                elif typ == "2":
                    print(f"Pole koła o promieniu {promien} wynosi: {Kolo(float(promien), typ='pole')}")
                else:
                    print("koniec")
                    import sys
                    sys.exit()
        except Exception as e:
            print(e)

def Test_Walec():
    from libs.tools.Testy import TestLiczb
    from libs.mathmath.kola import Walec
    while True:
        print("Walec")
        typ = input("co obliczamy\n1-Pole\n2-obj\nK-nic\n")
        try:
            if typ == "1":
                promien = input("Podaj promien Walca\n")
                h = input("Podaj wysokosc Walca\n")
                if TestLiczb(promien, h):
                     print(f"Pole walca o promieniu {promien} i wysokosci {h} wynosi: {Walec(float(promien), float(h), typ='pole')}")
            elif typ == "2":
                promien = input("Podaj promien Walca\n")
                h = input("Podaj wysokosc Walca\n")
                if TestLiczb(promien, h):
                    print(f"Objetosc walca o promieniu {promien} i wysokosci {h} wynosi: {Walec(float(promien), float(h), typ='obj')}")
            else:
                print("koniec")
                import sys
                sys.exit()
        except Exception as e:
            print(e)

def Test_Pesel():
    from libs.tools.PersonalAnalysing import DateFromPesel, GenderFromPesel
    # pesel=input("Podaj pesel do testow\n")
    pesele = ['03321412356', '00221412345', '99012345678', '95022134567']
    for x in pesele:
        print(f"Data urodzenia osob o peselu {x} to {DateFromPesel(x)}")
        print(f"Płeć osob o peselu {x} to {GenderFromPesel(x)}")
