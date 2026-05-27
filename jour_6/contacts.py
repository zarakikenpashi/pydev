"""
Liste des fonctions qui manipulent les contacts: couche logique
"""
        

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