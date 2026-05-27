from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

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