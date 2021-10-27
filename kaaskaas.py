antwoord = input ("Is de kaas geel? (j/n) ").lower()

if antwoord == "j":
    print ("De kaas is geel")
    antwoord = input ("Zitten er gaten in? (j/n) ").lower()

    if antwoord == "j":
        print ("Er zitten gaten in")
        antwoord = input ("Is de kaas belachelijk duur? (j/n) ").lower()
        if antwoord == "j":
           print ("Emmenthaler")
        
        else:
            print ("Leerdammer")

    else:
        print ("Er zitten geen gaten in")
        antwoord = input ("Is de kaas hard als steen? (j/n) ").lower()
        if antwoord == "j":
            print ("Panmigiano Reggiano")
        else:
            print ("Goudse Kaas")

else:
    print ("De kaas is niet geel")
    antwoord = input ("Heeft de kaas blauwe schimmels? (j/n) ").lower()
    if antwoord == "j":
        print ("De kaas heeft blauwe schimmels")
        antwoord = input ("Heeft de kaas een korst? (j/n) ").lower()
        if antwoord == "j":
            print ("Bleu de Rochbaron")
        else:
            print ("Foume d'Ambert")
    else:
        print ("De kaas heeft geen blauwer schimmels")
        antwoord = input ("Heeft de kaas een korst? (j/n) ")
        if antwoord == "j":
            print ("Camembert")
        else: 
            print ("Mozzarella")
    