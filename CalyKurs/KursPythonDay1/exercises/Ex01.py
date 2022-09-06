#napisac wfunkcję ktora przetwarza dane z listy peseli wypisuj
#indormacje o płci
def TestowanieKilkuPeseli():
    from libs.tools.PersonalAnalysing import GenderFromPesel
    pesele={'67050796161', '91101193663', '87020364679', '73051462792', '9006O642447', '560713819I7'}
    for x in pesele:
        print(f"Osoba o peselu {x} to {GenderFromPesel(x)}")

#dodac do tools do mathmath funkcję obliczającą polek ola oraz funkcję obliczającą obwód koła
#ww funkcję użyć dla przykładowej listy promieni i obliczyć pola i obwody
# ** potega operator
#import mathmath
#mathmath.pow(promien,2) funkcja potegi

def ObwodyPola():
    from libs.mathmath.kola import Pole, Obwod
    promienie = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    [print(f"Obwod kola o promieniu {x}: {Obwod(x)}\nPole kola o promieniu {x}: {Pole(x)}") for x in promienie]

#dla maniakow - dodac funkcje obliczajac pole walca, dodac funkcję obliczającą objętość walac
#tip do listy funkcji biblioteki figury dodac funkcję pole prostokata

def PoleObjetoscWalca():
    from libs.mathmath.kola import ObjetoscWalca, PoleWalca
    promienie = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    for x in promienie:
        print(f"Wyniki objetosc: {ObjetoscWalca(x,x)} dla {x} i {x}")
        print(f"Wyniki Pole: {PoleWalca(x,x)} dla {x} i {x}")

def ObliczMetodaWyznacznikow():
    from libs.mathmath.kola import MetodaWyznacznikow
    doPodstawienia = [(1,2,3,4,5,6), (2,3,4,5,6,7),(3,4,5,6,7,8),(4,5,6,7,8,9),(5,6,7,8,9,10)]
    try:
        for a in doPodstawienia:

            x, y = MetodaWyznacznikow(a[0],a[1],a[2],a[3],a[4],a[5])
            print(f"x={x:.2f}\ny={y:.2f}")
    except Exception as e:
        print(e)

def ObliczFunkcjeKwadratowa():
    from libs.mathmath.kola import FunkcjaKwadratowa
    doPodstawienia = [(2,5,3), (2,5,2),(3,5,2),(7,2,0),(5,6,7),(1,2,1)]
    try:
        for a in doPodstawienia:
            if a[0]!=0:
                x,y=FunkcjaKwadratowa(a[0],a[1],a[2])
                print(f"x1={x:.2f}\nx2={y:.2f}")
            else:
                print("A nie moze byc zerem")
    except Exception as e:
        print(e)


