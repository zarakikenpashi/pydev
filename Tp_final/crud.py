import database
from models import Contact
from sqlalchemy.exc import SQLAlchemyError

def create(db, elmt):
	try:
		db.add(elmt)
		db.commit()
		db.refresh(elmt)

		return elmt
	except SQLAlchemyError as e:
		db.rollback()
		raise e

def update(db, contactItem, values):
	data = db.query(Contact).filter_by(id=contactItem).first()
	if not data:
		raise ValueError(
			"Utilisateur introuvable"
		)
	try:
		for v in values:
			setattr(data, v, values.get(v))
		db.commit()
		db.refresh(data)

		return data
	except SQLAlchemyError as e:
		db.rollback()
		raise e

def delete(db, contactItem):
	data = db.query(Contact).filter_by(id=contactItem).first()
	if data is None:
		raise ValueError(
			"Utilisateur introuvable"
		)
	try:
		db.delete(data)
		db.commit()
		
		return {
		    "message": "Utilisateur supprimé"
		}
	except SQLAlchemyError as e:
		db.rollback()
		raise e

def get_contacts(db):
	return db.query(Contact).all()
