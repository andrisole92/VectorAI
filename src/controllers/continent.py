from src.db import SessionManager
from src.model.model import Continent

session = SessionManager.get_session()


def post(data):
    # print("post")
    # session = SessionManager.get_session()

    continent = Continent(name=data['name'], population=data['population'], area=data['population'])
    session.add(continent)
    session.commit()
    # session.close()
    # Insert a Person in the person table


def put(data):
    # print("put")

    # session = SessionManager.get_session()
    continent = session.query(Continent).filter(Continent.name == data['name']).first()
    if continent is None:
        raise Exception(f"No continent found with name: {data['name']}")
    for key in data:
        continent.__setattr__(key, data[key])
    session.commit()
    # session.close()


def delete(data):
    # print("delete")

    # session = SessionManager.get_session()
    obj = session.query(Continent).filter(Continent.name == data['name']).one()
    session.delete(obj)
    session.commit()
    # session.close()


sample = Continent.get_sample()
#
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
