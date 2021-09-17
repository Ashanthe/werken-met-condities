#Solicitatie
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Vacature: Circusdirecteur voor Circus HotelDeBotel")
print("Er wordt u een aantal relevante vragen gesteld...")
print("Gelieve die naar eer en geweten in te vullen")
print("Als blijkt dat u aan de criteria voldoet dan komt u in aanmerking voor een serieus sollicitatiegesprek")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


print("Vooraf kijken wij aan de hand van een tal van vragen of de persoon daadwerkelijk in aanmerkink komt voor een solicitatieformulier")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#Vragen vooraf
geslacht = input("Wat is uw geslacht?       ")
if geslacht == "vrouw":
    roodhaar = input("Draagt u rood krulhaar?       ") 
    if roodhaar == "nee":     
        print("Sorry u komt niet in aanmerking voor de solicitatie.")
        exit()  
    elif roodhaar == "ja":
        lengtrood = ("Wat is de lengte van uw haar in cm        ?")
        if int(lengtrood)<20:
            print("Sorry u komt niet in aanmerking voor de solicitatie.")
            exit() 
elif geslacht == "man":
    snor = input("Heeft u een snor?     ")
    if snor == "ja":
        lengtesnor = input("Wat is de lengte van de snor in centimers?    ")
        if int(lengtesnor) <8 :
            print("Sorry u komt niet in aanmerking voor de solicitatie.")
            exit() 
        lengte = input("Hoe lang bent u in centimeters?     ")
        if int(lengte) <150 :
                print("Sorry u komt niet in aanmerking voor de solicitatie.")
                exit() 
        gewicht = input("Wat is uw gewicht in kg?     ")
        if int(gewicht) <50:
            print("Sorry u komt niet in aanmerking voor de solicitatie.")
            exit()
           


#solicitatie
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("U kunt nu het solicitatieformulier invullen, veel succes!")

ervaring_dieren = input("Hoeveel jaar praktijkervaring heeft u met dierendressuur?      ")
jongleren = input("Hoeveel jaar praktijkervaring heeft u met jongleren?   ")
acrobatiek = input("Hoeveel jaar praktijkervaring heeft u met acrobatiek?       ")

if int(ervaring_dieren) < 4 and int(jongleren) < 5 and int(acrobatiek) < 3:
    print("U voldoet niet aan de criteria voor de functie circusdirecteur")
else:
    diploma = input("Bent u in het bezit van een MBO Niveau 4 'Ondernemen' diploma?     ")
    if diploma == "nee":
        print("U voldoet niet aan de criteria voor de functie circusdirecteur")
    if diploma == "ja":
        rijbew = input("Bent u in het bezit van een geldig Vrachtwagen rijbewijs?   ")
        if rijbew == "nee":
            print("U voldoet niet aan de criteria voor de functie circusdirecteur")
        elif rijbew == "ja":
            hoog = input("Bent u in het bezit van een hoge hoed?       ")
            if hoog == "nee":
              print("U voldoet niet aan de criteria voor de functie circusdirecteur")
            elif hoog == "ja":
                certificaat = input("Heeft u het certificaat 'Overleven met gevaarlijk personeel'?      ")
                if certificaat == "nee":
                    print("U voldoet niet aan de criteria voor de functie circusdirecteur")
                elif certificaat == "ja":
                    print("gefeliciteerd u komt in aanmerking voor de functie Circusdirecteur voor Circus HotelDeBotel")


 





    







    
  
       




















    
