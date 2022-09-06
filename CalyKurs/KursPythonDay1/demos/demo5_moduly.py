from demos import dane, FunkcjaModul

def DemosModuly():
    print(*dane, sep=", ")
    FunkcjaModul()
    import os
    print(os.getcwd())
    print(os.getcwdb())
    print(os.getlogin())
    path = os.getcwd()+"/Files/archiwum"
    if not os.path.exists(path):
        print(path)
        os.mkdir(path)
    # open(r"Files/foldery.txt","w", encoding='UTF-8').close()
    # open(r"Files/pliki.txt","w", encoding='UTF-8').close()
    #rekurencja przez foldery i pliki
    with open(r"Files/foldery.txt", "w", encoding="UTF-8") as plik:
        for root,foldery,pliki in os.walk(os.getcwd()):
            for nazwa in foldery:
                print(os.path.join(root,nazwa), file=plik)
        print(os.path.getsize(r"Files\foldery.txt"))
        print(os.path.getatime(r"Files\foldery.txt"))

    with open(r"Files/pliki.txt", "w", encoding="UTF-8") as plik:
        for root,foldery,pliki in os.walk(os.getcwd()):
            for nazwa in foldery:
                print(os.path.join(root,nazwa), file=plik)

    import shutil

    shutil.make_archive(r'Files\archiwum\arch', 'zip', os.path.join(os.getcwd(), r'Files\dane_firmowe'))

    import platform, logging
    print(platform.system(), platform.release(), platform.architecture(), platform.uname())

    print(platform.platform())

    if platform.platform().startswith('Window'):
        log_plik = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'log.log')
        print(log_plik)
    else:
        log_plik = os.path.join(os.getenv('HOME'), 'log.log')

    print(f'Tworzenie danych do ploku log {log_plik}')
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s', filename=log_plik,
                        filemode='a')
    import datetime
    logging.debug(f'start: {datetime.datetime.now()}')
    logging.info(' informacje o wykonanej operacji')
    logging.warning('ostrzezenie = dostep do danych o wyzszym stopnu..')
    logging.error('Blad w dzialaniu - zwykle jak  w try wchodzimy do except')

    import re
    tekst = """gdzie w tym teskcei jest kod pin 1234 , ktory trzeba znalesc i g oodczytac"""
    pattern = '\d{4}'
    szukamPin = re.search(pattern, tekst)
    if szukamPin:
        print(szukamPin.group())

    pattern = "(Len|Neverm)ore"
    with open(r"Files/raven.txt", "r") as plik:
        for l in plik:
            if re.search(pattern, l):
                print(l.strip("\n").strip(" "))

def DaneKoronawirusWorld():
    from bs4 import BeautifulSoup as bs
    import requests as r
    url = "https://www.worldometers.info/coronavirus/"
    dane = r.get(url)
    zupa = bs(dane.text, 'html.parser')
    info = zupa.find_all('div', class_="maincounter-number")
    print(info)
    zarazonych = (info[0].text).strip("\n").replace(","," ")
    zmarlo = (info[1].text).strip("\n").replace(","," ")
    wyzrowialo = (info[2].text).strip("\n").replace(","," ")

    print(f"zarażonych - {zarazonych}\nzmarlo - {zmarlo}\n ozdrowiencow - {wyzrowialo}")

walutyNBP=[]

def KursyWalutNBP():
    import requests as r, json
    url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=JSON"
    dane = r.get(url)
    daneJ = json.loads(dane.text)
    waluty = daneJ[0].get("rates")
    print(waluty)
    for i, k in enumerate(waluty):
        print(f"{i+1} - {k.get('code')}: {k.get('mid')} - {k.get('currency')}")
        walutyNBP.append((k.get('code'), k.get('mid')))

    while True:
        odp = input("Podaj jkaą kwotę w pln chcesz przeliczyc lub wcisnik k zeby zakocnzyc\n")
        if odp.upper() == "K":
            break
        else:
            wal = input("na ktora walute chcesz przeliczyc wart osz PLN podaj z menu\n")
            print(f"Cena w {walutyNBP[int(wal)-1][0]} wynosi {float(odp)/float(walutyNBP[int(wal)-1][1]) :.2f}")