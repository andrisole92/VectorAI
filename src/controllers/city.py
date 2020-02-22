from src.db import SessionManager
from src.model.model import City

session = SessionManager.get_session()


def post(data):
    # print("post")
    # session = SessionManager.get_session()

    city = City(name=data['name'], area=data['area'],
                road_count=data['road_count'],
                tree_count=data['tree_count'], shop_count=data['shop_count'],
                school_count=data['school_count'], country_id=data['country_id'], population=data['population'])
    session.add(city)
    session.commit()
    # session.close()
    # Insert a Person in the person table


def put(data):
    # print("put")

    # session = SessionManager.get_session()
    city = session.query(City).filter(City.name == data['name']).first()
    if city is None:
        raise Exception(f"No city found with name: {data['name']}")
    for key in data:
        city.__setattr__(key, data[key])
    session.commit()
    # session.close()


def delete(data):
    # print("delete")

    # session = SessionManager.get_session()
    obj = session.query(City).filter(City.name == data['name']).one()
    session.delete(obj)
    session.commit()
    # session.close()


sample = City.get_sample()
#
# # try:
# #     delete(sample)
# # except Exception as e:
# #     print(f'except, sorry: {str(e)}')
try:
    post(sample)
except Exception as e:
    print(f'except, sorry: {str(e)}')
# try:
#     put(sample)
# except Exception as e:
#     print(f'except, sorry: {str(e)}')
