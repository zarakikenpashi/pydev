"""
Liste des fonctions qui intéragissent avec la base de données: couche persistance
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