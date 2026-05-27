import database

def create(session, tbname, elmt):
	new_elemt = tbname(**elmt)
	session.add(new_elemt)
	session.commit()
	

def update(session, tbname, filter, values):
	data3 = session.query(tbname).filter_by(**filter).first()
	for v in values:
		setattr(data3, v, values.get(v))


	session.commit()

def delete(session, tbname, filter):
	data4 = session.query(tbname).filter_by(**filter).first()
	session.delete(data4)
	session.commit()

def show(session, tbname):
	data = session.query(tbname).all()
	for d in data:
		print(d)

