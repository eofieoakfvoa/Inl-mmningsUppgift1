#Ett palindrom är ett ord eller en mening som blir samma sak baklänges. Ex: anna, sallad i dallas, ola salo.

#Du ska skriva  en funktion som tar emot en mening och returnerar True om meningen är ett palindrom, eller False annars.


def Start():
    print("Hej skriv ett ord eller mening för att lista ut ifall det är en palindrom")
    message = input()

    resultTupel = GetUpperAndLowerCaseAmount(message)
    print("antal små bokstäver är : ",resultTupel[0], "(Med mellanslag) antal stora är : ", resultTupel[1])
