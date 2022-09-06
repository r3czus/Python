def GenderFromPesel(pesel):
    if len(pesel) == 11 and pesel.isnumeric():#jezeli wszystkie wartosci pesela sa cyframi
        gender = int(pesel[9])
        return "dziewczynka" if gender % 2 == 0 else "chlopczyk"
    else:
        return "zle podany pesel"

def DateFromPesel(pesel):
    if len(pesel) == 11 and pesel.isnumeric():
        import datetime as dt
        rok = int(pesel[:2])
        miesiac = int(pesel[2:4])
        dzien = int(pesel[4:6])
        if miesiac > 12:
            miesiac -= 20
            rok += 2000
        else:
            rok += 1900
        return dt.date(rok,miesiac,dzien)
    else:
        raise Exception("zle podany pesel")