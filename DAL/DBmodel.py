import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Commands(Base):
    __tablename__ = 'Commands'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    Cid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    Ctext = Column(String(250), nullable=False)
 
engine = create_engine('sqlite:///DB.db')
print(os.getcwd())
Base.metadata.create_all(engine)


# query='SELECT * FROM '+'"Commands"'
# print(query)
# result = cur.execute(query)
# for _r in result:
#    print(_r)