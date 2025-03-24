import Del1
import Del2
import Del3
def main():
    print(
        "Skriv en av de följande \n"
        "[1] = Momskalkylator \n"
        "[2] = Kolla hur många stora och små bokstäver I en text \n"
        "[3] = Kolla Ifall ett ord är en palindrom "
        )
    Alternative = input()
    #Det hade nog varit smartare att sätta alternativen i en Dictionary sen göra Dictionary[alternativ].Start() som skulle kunna runna coden men jag lowkey pallar inte
    #Där Dictionary innehåller en index som går till modulen och callar start, då alla filer förväntar innehålla en start() function
    #och eftersom jag vet att jag inte behöver expandera projectet mer än 3 så borde det vara okej att hard coda in detta och att uppgiften är på E nivå :P
    if Alternative == "1": 
        from Del1 import ChooseAlternatives
        ChooseAlternatives()
    if Alternative == "2":
        pass
    if Alternative == "3":
        pass
main()