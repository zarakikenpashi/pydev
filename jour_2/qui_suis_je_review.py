"""Devine le nombre mystère"""

"""
1 - factorisé counteur = counter + 1
2 - suppression des parenthèse après les if
3 - correction de l'orthographe de mot 'Dévinez'
4 - Ajouter des aides pour guider le users dans les choix : la recherche dichotomique
5 - Limites:
    --Pas de validation des bornes — -5 et 1500 sont acceptés
    --Règles du jeu pas communiquées clairement dès le départ
    --Aucune limite de tentatives — le jeu peut tourner indéfiniment
"""

import random


counter = 0
mini = 1
maxi = 1000
nombre = random.randint(mini, maxi)
while True:
    try:
        reponse = int(input(f"Devinez le nombre mystère compris entre {mini} et {maxi}: "))
    except ValueError:
        print(f"Veuillez saisir un nombre entier, compris entre {mini} et {maxi}")
    else:
        counter += 1
        if reponse > nombre:
            maxi = reponse
            print(f"Trop grand ! Essayer entre {mini} et {maxi}")
        elif reponse < nombre:
            mini = reponse
            print(f"Trop petit ! Essayer entre {mini} et {maxi}")
        else:
            print("Bravo !")
            print(f"Vous avez trouvé la reponse après {counter} tentative(s)")
            break