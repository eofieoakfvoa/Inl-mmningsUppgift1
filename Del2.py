
#Skriv en funktion som undersöker hur många små resp. stora bokstäver som finns i en text. Resultaten ska ges i en tupel. 

def Start():
    print("Hej skriv en mening för att lista ut hur många stora och små bockstäver den har")
    message = input()

    resultTupel = GetUpperAndLowerCaseAmount(message)
    print("antal små bokstäver är : ",resultTupel[0], "(Med mellanslag) antal stora är : ", resultTupel[1])

def GetUpperAndLowerCaseAmount(message : str):
    AmountOfUpper = 0
    AmountOfLower = 0
    for char in message:
        if char.isupper():
            AmountOfUpper = AmountOfUpper + 1
            continue
        AmountOfLower = AmountOfLower + 1
    return (AmountOfLower, AmountOfUpper)