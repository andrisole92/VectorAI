from src import SessionManager
#
session = SessionManager.get_session()
#
#
# def validate_country_population(city, population):
#     return True
#
#
# def validate_city_population(city, population):
#     country = session.query(Country).filter(Country.id == city.country_id).first()
#     country_population = country._population
#
#     # sum of population of cities in the continent
#     city_population_sum = session.query(func.sum(City.population).label('pop')).filter(
#         City.country_id == city.country_id).scalar() or 0
#
#     return city_population_sum + int(population) > country_population


def validate_country_area(city, population):
    return True


def validate_city_area(city, population):
    return True
