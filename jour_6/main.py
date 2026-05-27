"""Gestionnaire de contact : Interface"""
import contacts as repertoire
import stockage

if __name__== "__main__":
    actions = {"ajouter":"1", "rechercher":"2", "afficher":"3", "supprimer":"4"}
    contacts = stockage.charger_contacts()
    print("""Bienvenu(e) dans votre repertoire de contacts""")
    while True:
        option = repertoire.demander_reponse()
        if option == actions.get('ajouter'):
            nouveau = {
                "nom": input("Entrez le nom: "),
                "phone": input("Entrez le téléphone: "),
                "email": input("Entrez l'email: ")
            }
            contacts = repertoire.ajouter_contact(contacts,nouveau)
            stockage.sauvegarder_contacts(contacts)
        elif option == actions.get('rechercher'):
            elmt_a_rechercher = input("Entrez le nom à rechercher: ")
            repertoire.rechercher_contact(contacts,elmt_a_rechercher)
        elif option == actions.get('afficher'):
            repertoire.afficher_contact(contacts)
        elif option == actions.get('supprimer'):
            element_a_supprimer = input("Entrez le nom de la personne: ")
            contacts = repertoire.supprimer_contact(contacts, element_a_supprimer)
            stockage.sauvegarder_contacts(contacts)
        
        continuer = input("Continuer (oui / non): ")
        if continuer.lower() == "non":
            print("Au revoir, à la prochaine !")
            break
        
        
    
    
    
    