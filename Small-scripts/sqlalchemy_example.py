import sqlalchemy as db


engine = db.create_engine('sqlite:///test.db')
conn = engine.connect()

metadata = db.MetaData()
customers = db.Table('customers', metadata, autoload=True, autoload_with=engine)

print(customers.columns.keys())