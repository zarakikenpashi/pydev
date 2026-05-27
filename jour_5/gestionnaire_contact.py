"""Gestionnaire de contact"""
"""
valider les données : nom, phone, email
"""
import json

def charger_contacts():
    try:
        with open('contacts.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
 
def sauvegarder_contacts(contacts):
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)
        

def ajouter_contact(contacts,nouveau):
    contacts.append(nouveau)
    print(f"Le contact a bien été ajouté !")
    return contacts
    
def supprimer_contact(contacts,element_a_supprimer):
    conatct = rechercher_contact(contacts,element_a_supprimer)
    if conatct is None:
        print(f"{element_a_supprimer} n'existe pas !")
    else:
        contacts.remove(conatct)
        print(f"{element_a_supprimer} a bien été supprimé !")
        
    return contacts


def rechercher_contact(contacts,elmt_a_rechercher):
    if contacts:
        for contact in contacts:
            if contact.get('nom').lower() == elmt_a_rechercher.lower():
                print(f"Details: nom = {contact.get('nom')}, téléphone = {contact.get('phone')}, email = {contact.get('email')}")
                return contact
            
        print(f"{elmt_a_rechercher} n'existe pas")
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
    while True:
        print("""
            1 - Ajouter un contact: nom, téléphone, email
            2 - Rechercher un contact par nom
            3 - Afficher tous les contacts
            4 - Supprimer un contact
        """)
        option = input("Que souhaitez vous (1,2,3 ou 4): ")
        if option in ("1","2","3","4"):
            break
    return option

if __name__== "__main__":
    actions = {"ajouter":"1", "rechercher":"2", "afficher":"3", "supprimer":"4"}
    contacts = charger_contacts()
    print("""Bienvenu(e) dans votre repertoire de contacts""")
    while True:
        option = demander_reponse()
        if option == actions.get('ajouter'):
            nouveau = {
                "nom": input("Entrez le nom: "),
                "phone": input("Entrez le téléphone: "),
                "email": input("Entrez l'email: ")
            }
            contacts = ajouter_contact(contacts,nouveau)
            sauvegarder_contacts(contacts)
        elif option == actions.get('rechercher'):
            elmt_a_rechercher = input("Entrez le nom à rechercher: ")
            rechercher_contact(contacts,elmt_a_rechercher)
        elif option == actions.get('afficher'):
            afficher_contact(contacts)
        elif option == actions.get('supprimer'):
            element_a_supprimer = input("Entrez le nom de la personne: ")
            contacts = supprimer_contact(contacts, element_a_supprimer)
            sauvegarder_contacts(contacts)
        
        continuer = input("Continuer (oui / non): ")
        if continuer.lower() == "non":
            break
        
        
    
    
    
    