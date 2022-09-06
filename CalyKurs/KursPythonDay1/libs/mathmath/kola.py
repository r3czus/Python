import math


def Pole(r):
    wynik = 3.14*(r**2)
    return wynik

def Obwod(r):
    wynik = 2*3.14*r
    return wynik

#dla maniakow - dodac funkcje obliczajac pole walca, dodac funkcję obliczającą objętość walac
#tip do listy funkcji biblioteki figury dodac funkcję pole prostokata

def PoleProstokata(a,h):
    wynik=a*h
    return wynik

def PoleWalca(r,h):
    a=Obwod(r)
    podstawy=Pole(r)*2
    toduze=PoleProstokata(a,h)
    wynik=podstawy+toduze
    return wynik

def ObjetoscWalca(r,h):
    pk=Pole(r)
    wynik=pk*h
    return wynik

#dodacj funkcje obliczajace pole prostokata pole walca objetosc walca

#dodac funkcję pozwalającą rozwiać ukłąd 2 ch rownań metoda wyznaczników
#ax +by = c
#dx +ey = f

def MetodaWyznacznikow(a,b,c,d,e,f):
    W=a*e - b*d
    if W!=0:
        Wx=c*e - b*f
        Wy=a*f - c*d
        x=Wx/W
        y=Wy/W
        return (x,y)
    else:
        raise Exception("Błąd")

#dodac funkcje pozwalajacą roziwazac rownaie kwadratowe (ax2+bx+c=0)

def FunkcjaKwadratowa(a,b,c):
    from math import sqrt
    #b2-4ac
    delta=(b*b)-(4*a*c)
    if delta==0:
        x1=x2=-b/(a*2)
        return (x1,x2)
    if delta>0:
        x1=(-b-sqrt(delta))/(2*a)
        x2=(-b+sqrt(delta))/(2*a)
        return (x1,x2)
    if delta<0:
        raise Exception("to nie jest rownaie kwadratowe")

def Kolo(promien, **param):
    if param.get('typ') == "obwod":
        return 2*math.pi * promien
    elif param.get('typ') == "pole":
        return math.pi * math.pow(promien,2)
    else:
        raise Exception("należy podać parametr pole lub obwód")

def Walec(r,h,**param):
    if param.get('typ') == "pole":
        return PoleWalca(r,h)
    elif param.get('typ') == 'obj':
        return ObjetoscWalca(r,h)
    else:
        raise Exception("nalezy podac parametr pole lub obj")