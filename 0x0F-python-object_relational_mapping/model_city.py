#!/usr/bin/python3
"""
    Link a class with a database using sqlalchemy ORM
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()


class City(Base):
    """ Table. """
    __tablename__ = 'cities'  # The name of the table.

    # Creating columns.
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto")

    name = Column(String(128),
                  nullable=False)

    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
