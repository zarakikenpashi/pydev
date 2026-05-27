"""Devine le nombre mystère"""

"""
1 - factorisé counteur = counter + 1
2 - suppression des parenthèse après les if
3 - correction de l'orthographe de mot 'Dévinez'
4 - Ajouter des aides pour guider le users dans les choix : la recherche dichotomique
5 - Limites:
    -- que se passe si le user entre un nombre valide, hors bornes, comme -5 et 1005 ?
    -- est-ce que ton programme communique bien avec le user que c'est un entier qu'il doit sasisir ?
    -- qu'est-ce qui se passe si l'utilisateur veut quitter le jeu sans deviner ?
"""

import random

def generer_nombre_mystere(a,b):
    return random.randint(a, b)

def demander_reponse(mini,maxi):
    while True:
        try:
            reponse = int(input(f"Devinez le nombre mystère compris entre {mini} et {maxi}: "))
        except ValueError:
            print(f"Veuillez saisir un nombre entier, compris entre {mini} et {maxi}")
        else:
            if reponse < mini or reponse > maxi:
                print(f"Désolé, veuillez saisir un nombre entier compris entre {mini} et {maxi}")
            else:
                break
    
    return reponse


def afficher_message(reponse, nombre_mystere,mini,maxi):
    trouver = False
    if reponse > nombre_mystere:
        print(f"Trop grand ! Essayer entre {mini} et {maxi}")
    elif reponse < nombre_mystere:
        print(f"Trop petit ! Essayer entre {mini} et {maxi}")
    else:
        print("Bravo !")
        trouver = True
        
    return trouver


def mise_jour_mini_maxi(reponse,nombre, mini, maxi):        
    if reponse > nombre:
        maxi = reponse
    elif reponse < nombre:
        mini = reponse
        
    return mini, maxi

if __name__ == "__main__":
    counter = 0
    mini = 1
    maxi = 1000

    nombre = generer_nombre_mystere(mini,maxi)

    while True:
        reponse = demander_reponse(mini,maxi)
        mini, maxi = mise_jour_mini_maxi(reponse,nombre,mini, maxi)
        counter += 1
        trouver = afficher_message(reponse,nombre,mini,maxi)
        if trouver:
            print(f"Vous avez trouvé la reponse après {counter} tentative(s)")
            break            
            