#Ett palindrom är ett ord eller en mening som blir samma sak baklänges. Ex: anna, sallad i dallas, ola salo.

#Du ska skriva  en funktion som tar emot en mening och returnerar True om meningen är ett palindrom, eller False annars.
import math

def Start():
    print("Hej skriv ett ord eller mening för att lista ut ifall det är en palindrom")
    message = input()
    if _CheckIfSentenceIsPalindrome(message):
        print("Ja '", message, "' Är en palindrom :)")
    else:
        print("Nej :(")


def _CheckIfSentenceIsPalindrome(message):
    
    messageWithoutSpaces = message.replace(" ", "").lower() # vi vill ha utan spaces för t.ex ola salo, Lower() för t.ex annars hade Anna inte fungerat
    #ingentligen borde jag ta bort alla täcken som inte är bokstäver där ifall man skriver t.ex!., kommer det returna false
    #men då behöver jag göra sån där skum filter sak med massa symboler som ser komplicerad och läskigt ut
    LengthOfString = len(messageWithoutSpaces)
    HalfRoundedDown = math.floor(LengthOfString / 2) #ifall den har en single mitten så är den automatisk samma bokstav så finns ingen poäng att kolla den
    for i in range (HalfRoundedDown):
        if messageWithoutSpaces[i] != messageWithoutSpaces[LengthOfString-1-i]: #den sa out of range så jag tog -1 och det fungerar jag gissar det är för båda räknar inte från 0 i början eller nått
            return False #såfort någon är false så finns det ingen poäng att att kolla rästen 
        
    return True
    
