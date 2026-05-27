import csv
import json
import time

def logger(fonction):
	def wrapper(*args, **kwards):
		print(f"LOG: {fonction.__name__} appelé")
		resultat = fonction(*args, **kwards)

		return resultat

	return wrapper

import time
def timer(fonction):
	def wrapper(*args, **kwards):
		print(f"LOG: {fonction.__name__} à appelé")
		start = time.time()
		resultat = fonction(*args, **kwards)
		end = time.time()

		print(f"TEMPS D'EXECUTION: {end - start}")

		return resultat

	return wrapper


class JsonMixin:
	def to_dict(self):
		return vars(self)

	@classmethod
	def from_dict(cls, data):
		return cls(**data)

class Contact(JsonMixin):
	def __init__(self,nom,email,phone):
		if Contact.name_is_valide(nom) and Contact.email_is_valide(email) and Contact.phone_is_valide(phone):
			self.nom = nom
			self.email = email
			self.phone = phone
		else:
			raise ValueError("Erreur: vous devez saisir un nom, un numéro de téléphone et une adresse email valident, veuillez ressayer !")

	def __str__(self):
		return f"{self.nom},{self.email},{self.phone}"


	@staticmethod
	def name_is_valide(nom):
	    if not nom:
	        return False

	    return True


	@staticmethod
	def phone_is_valide(phone):
	    if not phone:
	        return False

	    return True

	@staticmethod
	def email_is_valide(email):
	    if not email or not '@' in email:
	        return False

	    return True

class Repertoire:
	def __init__(self):
		self.contacts = []

	def __str__(self):
		repertoire = ""
		for contact in self.contacts:
			repertoire += f"{contact.nom},{contact.email},{contact.phone}\n"

		return repertoire

	@timer
	@logger
	def ajouter(self,contact):
		self.contacts.append(contact)

	def supprimer(self,element_a_supprimer):
	    contact = self.rechercher(element_a_supprimer)
	    if contact is None:
	        print(f"{element_a_supprimer} n'existe pas !")
	    else:
	        confirm = input(f"Voulez vous supprimer le contact: {contact.nom} {contact.phone} {contact.email} ? (oui / non): ")
	        if confirm == "oui":
	            self.contacts.remove(contact)
	            print(f"{element_a_supprimer} a bien été supprimé !")
	        else:
	            print("Suppression annulée")
	        
	    return self.contacts

	def rechercher(self,nom):
	    if self.contacts:
	        for contact in self.contacts:
	            if nom.lower() in contact.nom.lower():
	                print(f"Details: nom = {contact.nom}, téléphone = {contact.phone}, email = {contact.email}")
	                return contact

	        return None
	    else:
	        print(f"Désolé, le repertoire de contacts est vide, veuillez ajouter un contact et ressayer")

	def sauvegarder(self):
		repertoire = [item.to_dict() for item in self.contacts]
		with open("repertoire.json","w") as f:
			json.dump(repertoire,f)


	def charger(self):
	    try:
	        with open('repertoire.json', 'r') as f:
	        	repertoire = [Contact.from_dict(item) for item in json.load(f)]
	        	self.contacts = repertoire
	        	return self.contacts
	    except FileNotFoundError:
	        return self.contacts
	        
	    except json.JSONDecodeError:
	        return self.contacts


class ContactPro(Contact):
	def __init__(self,entreprise, poste,nom,email,phone):
		self.entreprise = entreprise
		self.poste = poste
		super().__init__(nom,email,phone)

	def __str__(self):
		return f"{super().__str__()},{self.entreprise},{self.poste}"


def lire_contacts_csv(fichier):
	with open(fichier,"r") as f:
		for ligne in csv.DictReader(f):
			yield Contact(**ligne)

if __name__== "__main__":
	for item in lire_contacts_csv("contacts.csv"):
		print(item)
