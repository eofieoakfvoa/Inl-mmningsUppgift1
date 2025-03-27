import Del1
import Del2
import Del3
running = None
def main():
    running = true
    featuresList = {"1" :Del1, "2" :Del2, "3" :Del3}
    while running:
        print(
            "Skriv en av de följande \n"
            "[1] = Momskalkylator \n"
            "[2] = Kolla hur många stora och små bokstäver I en text \n"
            "[3] = Kolla Ifall ett ord är en palindrom \n"
            "[x] = gå ut ur programmet"
            )
        Alternative = input().lower()
        #Det hade nog varit smartare att sätta alternativen i en Dictionary sen göra Dictionary[alternativ].Start() som skulle kunna runna coden men jag lowkey pallar inte
        #Där Dictionary innehåller en index som går till modulen och callar start, då alla filer förväntar innehålla en start() function
        #och eftersom jag vet att jag inte behöver expandera projectet mer än 3 så borde det vara okej att hard coda in detta och att uppgiften är på E nivå :P
        featuresList[Alternative].Start()
        input("Klicka Enter för att fortsätta")
main()