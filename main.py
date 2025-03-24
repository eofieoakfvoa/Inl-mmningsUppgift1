def ChooseAlternatives():
    Price = "" #detta ser jätte skumt ut???
    momsPercent = "" 
    print("Hej snälla skriv först ett pris")
    while not isPriceValid(Price):
        try:
            Price = float(input())
        except:
            continue
    
    print("skriv nu moms I percent alltså t.ex '25'")
    while not isMomsValid(momsPercent):
        try:
            momsPercent = float(input())
        except:
            continue

    print(Price, momsPercent)
    appliedMomsPrice = ApplyMoms(Price, momsPercent)
    print("Priset :", Price, " med applicerad moms av ", momsPercent, "% Är lika med : ", appliedMomsPrice)

def ApplyMoms(price : float, moms : float):
    if not isPriceValid(price):
        print("aa ",type(price))
        return 
    if not isMomsValid(moms):
        
        return
    newMoms = convertMomsToDecimal(moms)
    appliedMomsPrice = price * (1 + newMoms)
    return appliedMomsPrice 

def isPriceValid(price):
    if type(price) != float:
        return False
    return True #ksk lägga till så price inte kan vara negativt?
    
def isMomsValid(moms):
    if type(moms) != float or int:    
        return False
    return True
def convertMomsToDecimal(moms):
    return moms * 0.01
ChooseAlternatives()