from fastapi import FastAPI
from pydantic import BaseModel


class Contact(BaseModel):
	nom: str
	phone: str
	email: str

app = FastAPI()

contacts = [
	{"nom": "koffi marie laure", "phone": "258", "email": "koffi@p"},
	{"nom": "kouame lahus", "phone": "741", "email": "lahus@y"}
]

@app.get('/')
def home():
	return {"message":"Bonjour"}


@app.get('/contacts')
def get_contacts():
	return contacts


@app.post('/contacts')
def save_contacts(contact:Contact):
	contacts.append(vars(contact))

	return contacts


@app.delete("/contacts/{nom}")
def delete_contact(nom: str):
    for contact in contacts:
    	if nom.lower() in contact.get('nom').lower():
    		contacts.remove(contact)

    return contacts


@app.put("/contacts/{nom}")
def update_contact(nom: str, contact: Contact):
    for c in contacts:
    	if nom.lower() in c.get('nom').lower():
    		data = vars(contact)
    		c.update(data)

    return contacts