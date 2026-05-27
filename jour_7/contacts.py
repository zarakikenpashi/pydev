"""
Liste des fonctions qui manipulent les contacts: couche logique
"""
        
import argparse

def ajouter_contact(contacts,nouveau):
    contacts.append(nouveau)
    print(f"Le contact a bien été ajouté !")
    return contacts
    
def supprimer_contact(contacts,element_a_supprimer):
    contact = rechercher_contact(contacts,element_a_supprimer)
    if contact is None:
        print(f"{element_a_supprimer} n'existe pas !")
    else:
        confirm = input(f"Voulez vous supprimer le contact: {contact.get('nom')} {contact.get('phone')} {contact.get('email')} ? (oui / non): ")
        if confirm == "oui":
            contacts.remove(contact)
            print(f"{element_a_supprimer} a bien été supprimé !")
        else:
            print("Suppression annulée")
        
    return contacts


def rechercher_contact(contacts,elmt_a_rechercher):
    if contacts:
        for contact in contacts:
            if elmt_a_rechercher.lower() in contact.get('nom').lower():
                print(f"Details: nom = {contact.get('nom')}, téléphone = {contact.get('phone')}, email = {contact.get('email')}")
                return contact
        return None
    else:
        print(f"Désolé, le repertoire de contacts est vide, veuillez ajouter un contact et ressayer")

def afficher_contact(contacts):
    if contacts:
        for contact in contacts:
            print(f"nom = {contact.get('nom')}, téléphone = {contact.get('phone')}, email = {contact.get('email')}")
    else:
        print("La liste des contacts est vide !")

def demander_reponse():
    parser = argparse.ArgumentParser(description="Gestionnaire de contacts")
    parser.add_argument("action", help="ajouter, rechercher, afficher, supprimer")
    parser.add_argument("--nom", help="Nom du contact")
    parser.add_argument("--phone", help="Téléphone du contact")
    parser.add_argument("--email", help="Email du contact")
    
    actions = ["ajouter", "rechercher", "afficher", "supprimer"]
    args = parser.parse_args()

    if not args.action in actions:
        return None
    
    return args

def name_is_valide(nom):
    if nom == None:
        return False

    return True

def phone_is_valide(phone):
    if phone == None:
        return False

    return True

def email_is_valide(email):
    if not '@' in email:
        return False

    return True