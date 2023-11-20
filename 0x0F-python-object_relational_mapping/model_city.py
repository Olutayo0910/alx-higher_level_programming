#!/usr/bin/python3
'''
 Python file that contains the class definition of a City
'''


from model_state import State, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ City Class """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
