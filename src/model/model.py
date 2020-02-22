import random
from sqlalchemy import Column, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, validates
from src.validators import validate_city_area
from src.db import Engine, SessionManager
from faker import Faker as sampler


sampler = sampler()

Base = declarative_base()

session = SessionManager.get_session()


class Continent(Base):
    __tablename__ = 'continent'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True, primary_key=True)

    population = Column(Integer, nullable=False)
    area = Column(Integer, nullable=False)

    @staticmethod
    def get_sample():
        return {
            'name': sampler.name(),
            'population': sampler.numerify(text='#####'),
            'area': sampler.numerify(text='#####'),
        }


class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True, primary_key=True)

    continent_id = Column(Integer, ForeignKey('continent.id'))
    continent = relationship(Continent)

    _population = Column(Integer, nullable=False)
    area = Column(Integer, nullable=False)

    hospital_count = Column(Integer, nullable=False)
    park_count = Column(Integer, nullable=False)
    river_count = Column(Integer, nullable=False)
    school_count = Column(Integer, nullable=False)

    @validates('_population')
    def validate_population(self, key, population):
        # continent populationn
        continent = session.query(Continent).filter(Continent.id == self.continent_id).first()
        continent_population = continent.population

        # sum of population of cities in the continent
        country_population_sum = session.query(func.sum(Country._population).label('pop')).filter(
            Country.continent_id == self.continent_id).scalar() or 0
        if country_population_sum is None:
            return population
        if country_population_sum + int(population) > continent_population:
            raise AssertionError(
                f"Population is too large, can't add one more city... Continent({continent.name}) population: {continent_population},"
                f" resulting population with {self.name} country: {country_population_sum + int(population)}")
        return population

    @staticmethod
    def get_sample():
        cont = session.query(Continent)[random.randrange(0, session.query(Continent).count())]
        return {
            'name': sampler.name(),
            '_population': sampler.numerify(text='####'),
            'area': sampler.numerify(text='####'),
            'river_count': sampler.numerify(text='####'),
            'park_count': sampler.numerify(text='####'),
            'hospital_count': sampler.numerify(text='####'),
            'school_count': sampler.numerify(text='####'),
            'continent_id': cont.id
        }


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(250), nullable=False, unique=True, primary_key=True)

    country_id = Column(Integer, ForeignKey('country.id'))
    country = relationship(Country)

    population = Column(Integer, nullable=False)
    area = Column(Integer, nullable=False)

    road_count = Column(Integer, nullable=False)
    tree_count = Column(Integer, nullable=False)
    shop_count = Column(Integer, nullable=False)
    school_count = Column(Integer, nullable=False)

    @validates('population')
    def validate_population(self, key, population):
        # continent population
        country = session.query(Country).filter(Country.id == self.country_id).first()
        country_population = country._population

        # sum of population of cities in the continent
        city_population_sum = session.query(func.sum(City.population).label('pop')).filter(
            City.country_id == self.country_id).scalar() or 0

        if city_population_sum + int(population) > country_population:
            raise AssertionError(
                f"Population is too large, can't add one more city... Country({country.name}) population:"
                f" {country_population},"
                f" resulting population with {self.name} city: {city_population_sum + int(population)}")
        return population

    @staticmethod
    def get_sample():
        try:
            # sess = SessionManager.get_session()
            rand = random.randrange(0, session.query(Country).count())
            country = session.query(Country)[rand]
            # sess.close()
            return {
                'name': sampler.name(),
                'population': sampler.numerify(text='###'),
                'area': sampler.numerify(text='###'),
                'road_count': sampler.numerify(text='####'),
                'tree_count': sampler.numerify(text='####'),
                'shop_count': sampler.numerify(text='####'),
                'school_count': sampler.numerify(text='####'),
                'country_id': country.id
            }
        except Exception as e:
            print(e)


Base.metadata.create_all(Engine.get_engine())


def object_has_keys(obj, keys):
    res = True
    for key in keys:
        if key not in obj:
            res = False
    return res

# val = object_has_keys({
#     'name': sampler.name(),
#     'population': sampler.numerify(text='###'),
#     'area': sampler.numerify(text='###'),
#     'road_count': sampler.numerify(text='####'),
#     'tree_count': sampler.numerify(text='####'),
#     'shop_count': sampler.numerify(text='####'),
#     'school_count': sampler.numerify(text='####'),
# }, ['name', 'population', 'area', 'road_count', 'tree_count', 'shop_count', 'school_count'])
#
# print(City.get_sample())
# print(City.get_sample())
# print(City.get_sample())
# print(City.get_sample())
# print(City.get_sample())
# print(City.get_sample())
