def Start():
    Price = "" #detta ser jätte skumt ut men fungerar :p
    momsPercent = "" 
    print("Hej snälla skriv först ett pris")

    while not _isPriceValid(Price):
        Price = input()
        try:
            Price = float(Price)
        except:
            print("Priset : ", Price, " är antingen inte ett nummer eller så innehåler det ett mellanslag")
    
    print("skriv nu moms I percent alltså t.ex '25' för 25%")
    while not _isMomsValid(momsPercent):
        momsPercent = input()
        try:
            momsPercent = float(momsPercent)
        except:
            print("MomsProcent på  : ", momsPercent, " är antingen inte ett nummer eller så innehåler det ett mellanslag")

    appliedMomsPrice = _ApplyMoms(Price, momsPercent)

    print("Priset :", Price, " med applicerad moms av ", momsPercent, "% Är lika med : ", round(appliedMomsPrice, 2))

    input()

def _ApplyMoms(price : float, moms : float): #Även fast det inte finns privata och protected saker i python så tycker jag att det är mysigt och ger ändå lite mer information
    newMoms = _convertMomsToDecimal(moms)
    appliedMomsPrice = price * (1 + newMoms)
    return appliedMomsPrice 

def _isPriceValid(price):
    if type(price) != float:
        return False
    return True #ksk lägga till så price inte kan vara negativt?
    
def _isMomsValid(moms):
    if type(moms) != float:    
        return False
    return True

def _convertMomsToDecimal(moms):
    return moms * 0.01
