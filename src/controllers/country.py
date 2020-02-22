from sqlalchemy import func

from src.db import SessionManager
from src.model.model import Country, Continent

session = SessionManager.get_session()


def post(data):
    print(f"post: {str(data)}")
    continent_population = session.query(Continent).filter(Continent.id == data['continent_id']).first().population
    country_population_sum = session.query(func.sum(Country._population).label('pop')).filter(
        Country.continent_id == data['continent_id']).scalar()
    print(continent_population)
    print(country_population_sum)
    country = Country(name=data['name'], area=data['area'],
                      river_count=data['river_count'],
                      park_count=data['park_count'],
                      hospital_count=data['hospital_count'],
                      school_count=data['school_count'], continent_id=data['continent_id'],_population=data['_population'])
    session.add(country)
    session.commit()


def put(data):
    # print("put")

    country = session.query(Country).filter(Country.name == data['name']).first()
    if country is None:
        raise Exception(f"No country found with name: {data['name']}")
    for key in data:
        country.__setattr__(key, data[key])
    session.commit()


def delete(data):
    # print("delete")

    obj = session.query(Country).filter(Country.name == data['name']).one()
    session.delete(obj)
    session.commit()


sample = Country.get_sample()

# try:
#     delete(sample)
# except Exception as e:
#     print(f'except, sorry: {str(e)}')
try:
    post(sample)
except Exception as e:
    print(f'except, sorry: {str(e)}')
# try:
#     put(sample)
# except Exception as e:
#     print(f'except, sorry: {str(e)}')
# post(sample)
