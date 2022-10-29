#!/usr/bin/python3
"""
    Start link class to table in database.
    Creating the starting point for the application (programm).
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    # Create a new Engine instance.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1],   # username
                                   argv[2],   # password
                                   argv[3]),  # database.
                           pool_pre_ping=True)  # tests connections.
    # Create all tables stored in this metadata.
    Base.metadata.create_all(engine)

    # create a configured "Session" class.
    Session = sessionmaker(bind=engine)  # used when engine is available.
    session = Session()  # create a Session instance.

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()  # emits the UPDATE statement
    print(new_state.id)
    session.close()
