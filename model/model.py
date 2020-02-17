from sqlalchemy import Column, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, validates

from db import Engine, SessionManager

Base = declarative_base()


class Continent(Base):
    __tablename__ = 'continent'
    id = Column(Integer, primary_key=True)

    name = Column(String(50), nullable=False, unique=True, primary_key=True)
    population = Column(Integer, nullable=False)


class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)

    name = Column(String(50), nullable=False, unique=True, primary_key=True)
    population = Column(Integer, nullable=False)

    continent_id = Column(Integer, ForeignKey('continent.id'))
    continent = relationship(Continent)

    hospital_count = Column(Integer, nullable=False)
    park_count = Column(Integer, nullable=False)
    river_count = Column(Integer, nullable=False)
    school_count = Column(Integer, nullable=False)

    @validates('population')
    def validate_population(self, key, population):
        session = SessionManager.get_session()
        session.query(func.sum(Continent.population))


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)

    name = Column(String(250), nullable=False)

    country_id = Column(Integer, ForeignKey('country.id'))
    country = relationship(Country)

    road_count = Column(Integer, nullable=False)
    tree_count = Column(Integer, nullable=False)
    shop_count = Column(Integer, nullable=False)
    school_count = Column(Integer, nullable=False)


