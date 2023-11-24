#!/usr/bin/python3
'''
creates the State California with the City San Francisco
'''


from relationship_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    InstanceSession = sessionmaker(bind=engine)
    session = InstanceSession()

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()

    session.close()
