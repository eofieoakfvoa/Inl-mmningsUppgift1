
#Skriv en funktion som undersöker hur många små resp. stora bokstäver som finns i en text. Resultaten ska ges i en tupel. 

def Start():
    print("Hej skriv en mening för att lista ut hur många stora och små bockstäver den har")
    message = input()

    resultTupel = _GetUpperAndLowerCaseAmount(message)
    print("antal små bokstäver är : ",resultTupel[0], "(Med mellanslag, och andra tecken som .,-) antal stora är : ", resultTupel[1])

def _GetUpperAndLowerCaseAmount(message : str):
    AmountOfUpper = 0 #har 2 variablar som for loopen lägger till ifall den är stor eller inte 
    AmountOfLower = 0
    for char in message:
        if char.isupper():
            AmountOfUpper = AmountOfUpper + 1
            continue #Continue eftersom den kan barak komma hit ifall den är stor, så den skippar att lägga till den i AmountOfLower och går till nästa index
        AmountOfLower = AmountOfLower + 1
    return (AmountOfLower, AmountOfUpper)