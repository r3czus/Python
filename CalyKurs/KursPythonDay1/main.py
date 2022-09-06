import demos.demo01_print as dp#as pozwala na skrocenie sciezki odwolania do importu
from demos.demo02_types import Basic_types #import globalny
#importujemy tylko wybrana funkcje
# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#TabNine/Kite programy Atom


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from demos.demo02_types import Basic_types, Typy_Kolekcyjne, Typy_Binarne  # import lokalny
    from demos.demo03_structures import Decyzje
    from demos.demo04_file import Pliki
    from exercises.Ex03 import LudzieWSzafkach, Filmoteka

    from demos.demo5_moduly import DemosModuly, DaneKoronawirusWorld, KursyWalutNBP
    from exercises.Ex04 import ZapisInfoDoPliku, SzukanieKsiazek
    from  exercises.Ex01 import TestowanieKilkuPeseli, ObwodyPola,PoleObjetoscWalca, ObliczMetodaWyznacznikow, ObliczFunkcjeKwadratowa
    from  exercises.Ex02 import Test_RozpoczecieDnia, Test_Kolo, Test_Walec, Test_Pesel
    # print_hi('Bartosz')
    # print(dp.DemoPrint.__doc__)  # __doc__ wyciaganie dokumentacji i jeje wypisywanie
    # dp.DemoPrint()
    # Basic_types()
    # Typy_Kolekcyjne()
    # Typy_Binarne()
    # Decyzje()
    # TestowanieKilkuPeseli()
    # ObwodyPola()
    # PoleObjetoscWalca()
    # ObliczMetodaWyznacznikow()
    # ObliczFunkcjeKwadratowa()
    # Test_RozpoczecieDnia()
    # Test_Kolo()
    # Test_Walec()
    # Test_Pesel()
    # Pliki()
    # Filmoteka()
    # LudzieWSzafkach()
    # DemosModuly()
    # ZapisInfoDoPliku()
    # DaneKoronawirusWorld()
    # KursyWalutNBP()
    SzukanieKsiazek()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
