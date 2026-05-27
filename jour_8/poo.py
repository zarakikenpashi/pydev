import json

class Contact:
	def __init__(self,nom,email,phone):
		if Contact.name_is_valide(nom) and Contact.email_is_valide(email) and Contact.phone_is_valide(phone):
			self.nom = nom
			self.email = email
			self.phone = phone
		else:
			raise ValueError("Erreur: vous devez saisir un nom, un numéro de téléphone et une adresse email valident, veuillez ressayer !")

	def __str__(self):
		return f"{self.nom},{self.email},{self.phone}"


	
	def to_dict(self):
		return {"nom": self.nom, "email":self.email, "phone":self.phone}

	@classmethod
	def from_dict(cls, data):
		return cls(nom=data['nom'], email=data['email'], phone=data['phone'])

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

if __name__== "__main__":
	c1 = Contact(nom="koffi", email="koffi@p", phone="01589632147")
	c2 = Contact(nom="durant", email="durant@p", phone="789654123")
	c3 = Contact(nom="dupont", email="dupont@y", phone="123654789")

	#print(c4)

	r = Repertoire()

	#r.ajouter(c1)
	#r.ajouter(c2)
	#r.ajouter(c3)
	# print(r)

	# r.rechercher("koffi")
	# r.supprimer("koffi")
	# print(r)

	#r.sauvegarder()
	r.charger()
	print(r)


 
