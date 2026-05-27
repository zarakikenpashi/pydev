"""Devine le nombre mystère"""
import random

nombre = random.randint(1, 1000)
counter = 0
while True:
    try:
        reponse = int(input(f"Dévinez le nombre mystère compris entre 1 et 1000: "))
    except ValueError:
        print("Veuillez saisir un nombre entier, compris entre 1 et 1000")
    else:
        if(reponse > nombre):
            print("Trop grand")
            counter = counter + 1
        elif (reponse < nombre):
            counter = counter + 1
            print("Trop petit")
        else:
            print("Bravo !")
            print(f"Vous avez trouvé la reponse après {counter} tentative(s)")
            break
    
    
    