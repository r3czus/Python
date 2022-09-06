def ZapisInfoDoPliku():
    import platform, logging
    import os
    print(platform.system(), platform.release(), platform.architecture(), platform.uname())

    print(platform.platform())

    if platform.platform().startswith('Window'):
        log_plik = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'log.log')
    else:
        log_plik = os.path.join(os.getenv('HOME'), 'log.log')

    print(f'Tworzenie danych do ploku log {log_plik}')
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s', filename=log_plik,
                        filemode='a')
    import datetime
    logging.debug(f'start: {datetime.datetime.now()}')
    logging.debug(f'release: {platform.release()}')
    logging.debug(f'system: {platform.system()}')
    logging.debug(f'architecture: {platform.architecture()}')
    logging.debug(f'uname: {platform.uname()}')
    logging.debug(f'platform: {platform.platform()}')
    logging.debug(f'version: {platform.version()}')
    logging.debug(f'procesor: {platform.processor()}')
    logging.debug(f'branch: {platform.python_branch()}')
    logging.debug(f'machine: {platform.machine()}')
    logging.debug(f'node: {platform.node()}')
    logging.info('informacje o wykonanej operacji')
    logging.warning('ostrzezenie = dostep do danych o wyzszym stopnu..')
    logging.error('Blad w dzialaniu - zwykle jak  w try wchodzimy do except')
    with open(r"Files/log.txt", "a", encoding="UTF-8") as plik:
        print(f'release: {platform.release()}', file=plik)
        print(f'system: {platform.system()}', file=plik)
        print(f'architecture: {platform.architecture()}', file=plik)
        print(f'uname: {platform.uname()}', file=plik)
        print(f'platform: {platform.platform()}', file=plik)
        print(f'version: {platform.version()}', file=plik)
        print(f'procesor: {platform.processor()}', file=plik)
        print(f'branch: {platform.python_branch()}', file=plik)
        print(f'machine: {platform.machine()}', file=plik)
        print(f'node: {platform.node()}', file=plik)
wszystkieNazwy = []
wszyscyAutorzy = []
wszystkieKsiegi = []

def SzukanieKsiazek():
    import requests as r
    from bs4 import BeautifulSoup as bs
    url = "https://helion.pl/kategorie/ksiazki"
    dane = r.get(url)
    zupa = bs(dane.text, 'html.parser')
    info = zupa.find_all('h3', itemprop="name")
    for i in info:
        tak = i.find('a')
        wszystkieNazwy.append(tak.text)

    info2 = zupa.find_all('p', class_="author")
    for j in info2:
        tak2 = j.find("a")
        wszyscyAutorzy.append(tak2.text)

    for h in range(len(wszystkieNazwy)):
        wszystkieKsiegi.append((wszystkieNazwy[h], wszyscyAutorzy[h]))

    for k in wszystkieKsiegi:
        print(f"{k[0]}, {k[1]}")
        print(">WA<"*20)
    # info = info.find('a')
    # print(info.text)
    # print(info)