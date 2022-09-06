def Decyzje():
    from libs.tools.PersonalAnalysing import GenderFromPesel
    pesel='03290123456'#plec na 10
    print(f"Osoba o peselu {pesel} to {GenderFromPesel(pesel)}")