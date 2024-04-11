#!/usr/bin/python3
'''file that contains the class definition of a City'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    '''declerative City class'''
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")

    def __repr__(self):
        return f'({self.id}, {self.name}, {self.state.name})'


State.cities = relationship(
    'City', back_populates="state", cascade="all, delete, delete-orphan")
