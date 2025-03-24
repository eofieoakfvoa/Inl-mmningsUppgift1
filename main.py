def ChooseAlternatives():
    print("Hej snälla skriv ett pris och dess moms I percent alltså t.ex '0.25' ")
    ApplyMoms()
    print("Priset :", "", " med applicerad moms av ", "", " Är lika med : ", "")
def ApplyMoms(price, moms):
    if not isPriceValid(price):
        pass
    if not isMomsValid(moms):
        pass
    newMoms = convertMomsToDecimal(moms)
    return price, moms, appliedMomsPrice 

def isPriceValid(price):
    pass
def isMomsValid(moms):
    pass
def convertMomsToDecimal(moms):
    pass