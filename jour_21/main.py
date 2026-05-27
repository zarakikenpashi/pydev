from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session


class Base(DeclarativeBase):
    pass

class Contact(Base):
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String)
    phone = Column(String)

    def __str__(self):
    	return f"{self.id} {self.nom} {self.email} {self.phone}"

if __name__ == "__main__":
	engine = create_engine("sqlite:///contacts.db")
	Base.metadata.create_all(engine)

	with Session(engine) as session:
		# contact = Contact(nom="durant", email="durant@p", phone="789654123")
		# session.add(contact)
		# session.commit()

		data = session.query(Contact).all()
		# for d in data:
		# 	print(d)

		data2 = session.query(Contact).filter_by(nom="durant").all()
		for d in data2:
			print(d)