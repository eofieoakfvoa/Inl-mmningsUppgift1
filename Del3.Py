#Ett palindrom är ett ord eller en mening som blir samma sak baklänges. Ex: anna, sallad i dallas, ola salo.

#Du ska skriva  en funktion som tar emot en mening och returnerar True om meningen är ett palindrom, eller False annars.
import math

def Start():
    print("Hej skriv ett ord eller mening för att lista ut ifall det är en palindrom")
    message = input()
    CheckIfSentenceIsPalindrome(message)


def CheckIfSentenceIsPalindrome(message):
    
    messageWithoutSpaces = message.replace(" ", "")
    LengthOfString = len(messageWithoutSpaces)
    HalfRoundedDown = math.floor(LengthOfString / 2)
    print(messageWithoutSpaces)
    for i in range (HalfRoundedDown):
        if message[i] == message[LengthOfString-1-i]:
            print("Same Letter")
    
        
        
        
Start()