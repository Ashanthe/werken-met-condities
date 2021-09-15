#Kaas, kaas en nog eens kaas




# Startvraag en ja/nee
kaas = input("is de kaas geel?    ")

#wie is het
if kaas == "ja":
    gaten = input("Zitten er gaten in?     ")
    if gaten == "ja":
        duur = input("Is de kaas belachelijk duur?    ")
        if duur == "ja":
            print("De kaas is Emmenthaler!")
        elif duur == "nee":
            print("De kaas is Leerdammer!")
    elif gaten == "nee":
        hard == input("Is de kaas hard als steen?       ")
        if hard == "ja":
            print("De kaas is een Pammigiano Reggiano!")
        elif hard == "nee":
            print("De kaas is een Goudse kaas!       ")
elif kaas == "nee":
    blauwe = input("Heeft de kaas blauwe schimmels?      ")
    if blauwe == "ja":
        korst = input("Heeft de kaas een korst?     ")
        if korst == "ja":
            print("De kaas is Bleu de Rochbaron")
        elif korst == "nee":
            print("De kaas is een Foume d'Ambert")
    elif blauwe == "nee":
        korst = input("Heeft de kaas een korst?     ")
        if korst == "Ja":
            print("De kaas is een Camembert")
        elif korst == "nee":
            print("De kaas is een Mozzerella")






    

