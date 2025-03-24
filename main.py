def ChooseAlternatives():
    print("Hej snälla skriv först ett pris")
    Price = input()
    print("moms I percent alltså t.ex '25'")
    momsPercent = input()
    print(Price, momsPercent)
    appliedMomsPrice = ApplyMoms(Price, momsPercent)
    print("Priset :", "", " med applicerad moms av ", "", " Är lika med : ", "")
def ApplyMoms(price : float, moms : float):
    if not isPriceValid(price):
        print("aa ",type(price))
        return 
    if not isMomsValid(moms):
        
        return
    newMoms = convertMomsToDecimal(moms)
    appliedMomsPrice = price * (1 + newMoms)
    return price, moms, appliedMomsPrice 

def isPriceValid(price):
    if type(price) != float or int:
        print("The price of : ", price, " is not a valid number :(")
        return False
    return True #ksk lägga till så price inte kan vara negativt?
    
def isMomsValid(moms):
    if type(moms) != float or int:    
        return False
    return True
def convertMomsToDecimal(moms):
    return moms * 0.01
ChooseAlternatives()