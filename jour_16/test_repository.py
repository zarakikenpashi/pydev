import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Contact
import repository

engine = create_engine("sqlite:///:memory:")  # BDD temporaire
Base.metadata.create_all(engine)

def test_create():
	with Session(engine) as session:
		size_before = session.query(Contact).all()
		repository.create(session, Contact, {"nom":"Damas", "email":"damas@y", "phone":"89632541"})
		size_after = session.query(Contact).all()

		assert len(size_before) < len(size_after)


def test_delete():
	with Session(engine) as session:
		repository.create(session, Contact, {"nom":"Damas", "email":"damas@y", "phone":"89632541"})
		size_before = session.query(Contact).all()
		repository.delete(session, Contact, {"nom":"Damas"})
		size_after = session.query(Contact).all()

		assert len(size_before) > len(size_after)
