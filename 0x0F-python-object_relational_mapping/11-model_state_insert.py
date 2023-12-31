#!/usr/bin/python3
'''
script tha adds the State object Louisiana
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    InstSession = sessionmaker(bind=engine)
    session = InstSession()

    newState = State(name='Louisiana')
    session.add(newState)
    session.commit()
    print(newState.id)
    session.close()
