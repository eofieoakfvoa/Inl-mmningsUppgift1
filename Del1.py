def Start():
    #sätter variablerna tomma och så jag kan använda de senare när jag kollar ifall de är korrekta eller inte
    Price = None
    momsPercent = None 
    print("Hej snälla skriv först ett pris")
    #Tycker det är lättare att förstå och lägga till vad priset får vara, med dens egna metod istället för att ha det här
    #Något känns också fel här, där jag nog kunde gjort det på ett bättre sätt, men det fungerar 
    while not _IsPriceValid(Price):
        Price = input()
        try: #jag försöker göra det till en float ifall det fungerar så skriver den att priset är fel
            Price = float(Price)
        except:
            print("Priset : ", Price, " är antingen inte ett nummer eller så innehåler det ett mellanslag")
    
    print("skriv nu moms I percent alltså t.ex '25' för 25%")

    while not _IsMomsValid(momsPercent):
        momsPercent = input()
        try:
            momsPercent = float(momsPercent)
        except:
            print("MomsProcent på  : ", momsPercent, " är antingen inte ett nummer eller så innehåler det ett mellanslag")

    appliedMomsPrice = _ApplyMoms(Price, momsPercent)

    #från vad jag kunde hitta så avrundas priser till närmsta andra decimal, och detta hjälper också med problemet att floats inte är exakta och kan göra så det är jätte många 0:or sen några nummer 
    print("Priset :", Price, " med applicerad moms av ", momsPercent, "% Är lika med : ", round(appliedMomsPrice, 2)) 

def _ApplyMoms(price : float, moms : float): #Även fast det inte finns privata och protected saker i python så tycker jag att det är mysigt och ger ändå lite mer information
    newMoms = _ConvertMomsToDecimal(moms)
    appliedMomsPrice = price * (1 + newMoms)
    return appliedMomsPrice 

def _IsPriceValid(price):
    if type(price) != float:
        return False
    return True #ksk lägga till så price inte kan vara negativt?
    
def _IsMomsValid(moms):
    if type(moms) != float:    
        return False
    return True

def _ConvertMomsToDecimal(moms): #gör så att när t.ex 25 blir till 0.25 så man faktiskt kan göra matten för att räkna ut 
    return moms * 0.01
