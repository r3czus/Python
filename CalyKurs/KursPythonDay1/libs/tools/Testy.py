def TestNumber(value):
    try:
        x=float(value)
        return True
    except:
        return False

def TestLiczb(*liczby):
    test = True
    for l in liczby:
        test = TestNumber(l)
        if test == False:
            return False
    return test