import database
from models import Contact


def create(db, elmt):
	db.add(elmt)
	db.commit()
	db.refresh(elmt)

	response = {
		"success": True,
		"message": "Utilisateur créé",
		"data": elmt
	}

	return response
	

def update(db, contactItem, values):
	data = db.query(Contact).filter_by(id=contactItem).first()
	if data is None:
		response = {
			"errors": True,
			"message": "cet utilisateur n'existe pas",
			"data": {}
		}
	else:
		for v in values:
			setattr(data, v, values.get(v))

		db.commit()

		response = {
			"success": True,
			"message": "cet utilisateur à bien été mis à jour !",
			"data": data
		}

	return response

def delete(db, contactItem):
	data = db.query(Contact).filter_by(id=contactItem).first()
	if data is None:
		response = {
			"errors": True,
			"message": "cet utilisateur n'existe pas",
			"data": {}
		}
	else:
		db.delete(data)
		db.commit()
		response = {
			"success": True,
			"message": "cet utilisateur à bien été supprimé !",
			"data": data
		}

	return response


def get_contacts(db):
	data = db.query(Contact).all()

	response = {
		"success": True,
		"message": "Liste des utilisateurs",
		"data": data
	}

	return response

