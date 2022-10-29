#!/usr/bin/python3
"""
    Start link class to table in database.
    Creating the starting point for the application (programm).
    Make a query.
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City


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

    # Query with a join between State and City.
    my_query = session.query(State, City)\
                      .filter(State.id == City.state_id)\
                      .order_by(City.id)\
                      .all()
    for state, city in my_query:
        print("{}: ({}) {}".format(state.name,
                                   city.id,
                                   city.name))

    session.close()
