


from typing import Annotated
from sqlalchemy.orm import Session
import crud
from database import engine
import models
from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr, ValidationError
from pydantic_extra_types.phone_numbers import PhoneNumberValidator


E164PhoneNumber = Annotated[str, PhoneNumberValidator(number_format='E164')]

class Contact(BaseModel):
	nom: str
	phone: E164PhoneNumber
	email: EmailStr

app = FastAPI()


# Create tables in the database
models.Base.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


@app.get('/contacts')
def get_contacts(db:Session = Depends(get_db)):
	return crud.get_contacts(db)


@app.post('/contacts')
def save_contacts(contact: Contact, db:Session = Depends(get_db)):
	try:
		contact_item = models.Contact(nom=contact.nom, email=contact.email,phone=contact.phone)
	except ValidationError as e:
		msg = []
		for error in e.errors():
			champ = error['loc'][0]

			if champ == "phone":
				msg.append("la valeur n'est pas un numéro de téléphone valide")
			elif champ == "email":
				msg.append("la valeur n'est pas une adresse e-mail valide")

		return {
			"code": 422,
			"errors": msg
		}
	else:
		return crud.create(db, contact_item)


@app.delete("/contacts/{contactItem}")
def delete_contact(contactItem: int, db:Session = Depends(get_db)):
	return crud.delete(db,contactItem)



@app.put("/contacts/{contactItem}")
def update_contact(contactItem: int, nom: str, email:str, phone:str, db:Session = Depends(get_db)):
	return crud.update(db, contactItem, {"nom":nom,"email":email, "phone":phone})


