naam = input ("Wat is uw naam? ")


ErvaringDierendressuur = int (input ("Hoeveel jaar praktijk ervaring heeft u met dierendressuur? "))

ErvaringJongleren = int (input ("Hoeveel jaar ervaring heeft u met jongleren? "))

ErvaringAcrobatiek = int (input ("Hoeveel jaar ervaring heeft u met acrobatiek? "))

Diploma = input ("Bent u in bezit van een Diploma MBO-4? (j/n) ").lower()

Rijbewijs = input ("Bent u in bezit van een geldig Vrachtwagen rijbewijs? (j/n) ").lower()

Hoed = input ("Bent u in bezit van een hoge hoed? (j/n) ").lower()

Gender = input ("Bent u een man of vrouw? (m/v) ").lower()
if Gender == "m":
    Snor = int (input ("Hoe breed is uw snor? (cm) "))
else : 
    Haar = int (input ("Hoe lang is u haar? (cm) ")) 

Lengte = int (input ("Hoe lang bent u? (cm) "))

Gewicht = int (input ("Hoeveel weegt u? (kg) "))

Certificaat = input ("Heeft u een certificaat 'Overleven met gevaarlijk personeel' (j/n) ").lower()

Moeder = int (input ("Hoe oud is uw moeder? "))

Vuilnisbak = input ("Heeft u thuis een vuilnisbak? (j/n) ").lower()

Lepel = input ("Heeft u een komisch grote lepel? (j/n) ").lower()

BingChilling = input ("Bing chilling? (j/n) ").lower()


if ErvaringDierendressuur > 4 and ErvaringJongleren > 5 and ErvaringAcrobatiek > 3 and Diploma == "j" and Rijbewijs == "j" and Hoed == "j" and Lengte > 150 and Gewicht > 90 and Certificaat == "j" and Moeder < 34 and Vuilnisbak == "j" and Lepel == "j" and BingChilling == "j" :
    print("U bent geschikt")
else :
    print ("U bent niet geschikt")
