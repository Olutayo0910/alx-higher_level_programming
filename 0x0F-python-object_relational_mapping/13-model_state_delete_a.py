#!/usr/bin/python3
'''
 script that deletes all State objects with a name containing the letter a
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    InstSession = sessionmaker(bind=engine)
    session = InstSession()

    states = session.query(State).filter(State.name.contains('a')).all()
    for element in states:
        session.delete(element)

    session.commit()
    session.close()
