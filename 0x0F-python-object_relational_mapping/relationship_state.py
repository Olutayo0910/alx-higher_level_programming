#!/usr/bin/python3
"""
Python file that Contains State class and Base,
an instance of declarative_base()
"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base(metadata=mymeta)


class State(Base):
    """
    Defines class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            back_populates="state",
            cascade="all,
            delete-orphan")
