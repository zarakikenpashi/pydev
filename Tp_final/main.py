


from typing import Annotated
from sqlalchemy.orm import Session
import crud
from database import engine
import models
from fastapi import FastAPI, Depends, HTTPException, Request
from pydantic import BaseModel, EmailStr, ValidationError,Field
from pydantic_extra_types.phone_numbers import PhoneNumberValidator

#Gestion des erreurs
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

#Gestion des erreurs backend
from sqlalchemy.exc import SQLAlchemyError

E164PhoneNumber = Annotated[str, PhoneNumberValidator(number_format='E164')]

class Contact(BaseModel):
	nom: str = Field(min_length=3)
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


"""Gestion des erreurs: RequestValidationError"""
@app.exception_handler(RequestValidationError)
def validate_exception_handler(request: Request, exc: RequestValidationError):
	msg = []
	for error in exc.errors():
		champ = error["loc"][-1]

		if champ == "phone":
			msg.append("la valeur n'est pas un numéro de téléphone valide")
		elif champ == "email":
			msg.append("la valeur n'est pas une adresse e-mail valide")
		elif champ == "nom":
			msg.append("le nom doit contenir au moins 3 caractères")
	return JSONResponse(
        status_code=422,
        content={
            "detail": msg
        })

@app.get('/contacts')
def get_contacts(db:Session = Depends(get_db)):
	return crud.get_contacts(db)


@app.post('/contacts')
def save_contacts(contact: Contact, db: Session = Depends(get_db)):
	try:
		contact_item = models.Contact(**contact.model_dump())
		return crud.create(db, contact_item)
	except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Erreur base de données"
        )

@app.delete("/contacts/{contactItem}")
def delete_contact(contactItem: int, db:Session = Depends(get_db)):
	try:
		return crud.delete(db,contactItem)
	except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur introuvable"
        )
	except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Erreur base de données"
        )




@app.put("/contacts/{contactItem}")
def update_contact(contactItem: int, contact: Contact, db:Session = Depends(get_db)):
	try:
		return crud.update(db, contactItem, **contact.model_dump())
	except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur introuvable"
        )
	except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Erreur base de données"
        )
