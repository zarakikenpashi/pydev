"""Gestionnaire de contact : Interface"""
import contacts as repertoire
import stockage

if __name__== "__main__":
    contacts = stockage.charger_contacts()
    args = repertoire.demander_reponse()

    if args != None:
        if args.action == "ajouter":
            if repertoire.name_is_valide(args.nom) and repertoire.phone_is_valide(args.phone ) and repertoire.email_is_valide(args.email):
                nouveau = {"nom": args.nom, "phone": args.phone, "email": args.email}
                contacts = repertoire.ajouter_contact(contacts,nouveau)
                stockage.sauvegarder_contacts(contacts)
            else:
               print("Erreur: vous devez saisir un nom, un numéro de téléphone et une adresse email valident, veuillez ressayer !")
        elif args.action == "rechercher":
            if repertoire.name_is_valide(args.nom):
                repertoire.rechercher_contact(contacts,args.nom)
            else:
                print("Erreur: vous devez saisir un nom valide, veuillez ressayer !")
        elif args.action == "afficher":
            repertoire.afficher_contact(contacts)
        elif args.action == "supprimer":
            if repertoire.name_is_valide(args.nom):
                contacts = repertoire.supprimer_contact(contacts, args.nom)
                stockage.sauvegarder_contacts(contacts)
            else:
                print("Erreur: vous devez saisir un nom valide, veuillez ressayer !")
    else:
        print("Choix invalide, veuillez ressayer")

    
    
    
    