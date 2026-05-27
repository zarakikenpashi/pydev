


from sqlalchemy.orm import Session
import repository
from database import engine
from models import Contact

if __name__ == "__main__":

	with Session(engine) as session:
		""" Ajouter un nouveau contact """
		# new_elmt = {"nom":"Gontrand", "email":"gontrand@y", "phone":"89632541"}
		# repository.create(session, Contact, new_elmt)


		"""Lire les contacts en base """
		repository.show(session,Contact)


		""" Modifier un contact spécifique en """
		#repository.update(session, Contact, {"nom":"durant"}, {"email":"kevindurant@yahoo.fr"})
		# data3 = session.query(Contact).filter_by(nom="durant").first()
		# data3.email = "kevindurant@yahoo.fr"
		# session.commit()

		""" Supprimer un contact spécifique en """
		#repository.delete(session, Contact, {"nom":"durant"})
		# data4 = session.query(Contact).filter_by(nom="durant").first()
		# session.delete(data4)
		# session.commit()


