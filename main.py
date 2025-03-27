import Del1
import Del2
import Del3
def main():
    running = True
    featuresList = {"1" :Del1, "2" :Del2, "3" :Del3}
    while running:
        validAlterantive = None
        print(
            "Skriv en av de följande \n"
            "[1] = Momskalkylator \n"
            "[2] = Kolla hur många stora och små bokstäver I en text \n"
            "[3] = Kolla Ifall ett ord är en palindrom \n"
            "[x] = gå ut ur programmet"
            )
        
        while validAlterantive != True:
            Alternative = input().lower()
            if Alternative == "x":
                running = False
                break
            for index in range(1, len(featuresList)+1): #jag gör så att den börjar på 1 för det blir lättare i nästa del, sen måste jag göra +1 på len() så den fortfarande gör 3 gånger
                if Alternative == str(index):
                    validAlterantive = True
                    
        featuresList[Alternative].Start()
        input("Klicka Enter för att fortsätta")
main()