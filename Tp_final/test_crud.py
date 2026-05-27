import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Contact
import crud

engine = create_engine("sqlite:///:memory:")  # BDD temporaire
Base.metadata.create_all(engine)

def test_create():
	with Session(engine) as session:
		size_before = session.query(Contact).all()
		contact = Contact(nom="Damas", email="damas@gmail.com", phone="+2250796321456")
		crud.create(session, contact)
		size_after = session.query(Contact).all()

		assert len(size_before) < len(size_after)


def test_delete():
	with Session(engine) as session:
		contact = Contact(nom="Damas", email="damas@gmail.com", phone="+2250796321456")
		crud.create(session, contact)
		size_before = session.query(Contact).all()
		crud.delete(session, contact.id)
		size_after = session.query(Contact).all()

		assert len(size_before) > len(size_after)



def test_update():
	with Session(engine) as session:
		contact = Contact(nom="Damas", email="damas@gmail.com", phone="+2250796321456")
		crud.create(session, contact)
		contact_before = session.query(Contact).filter_by(id=contact.id).first()
		crud.update(session, contact.id, {"nom":"Olive and tom", "email":"olive.tom@yahoo.fr","phone":"+2250796321458"})
		contact_after = session.query(Contact).filter_by(id=contact.id).first()

		assert contact_after.nom == "Olive and tom"
		assert contact_after.email == "olive.tom@yahoo.fr"
		assert contact_after.phone == "+2250796321458"
