import sys
from json import loads

from kafka import KafkaConsumer

from src.controllers.controllers import controllers
from src.db.Engine import Engine
from src.logger import logger
from src.model.model import Base

Base.metadata.create_all(Engine.get_engine())

print("Hello World")

consumer1 = KafkaConsumer('main', value_deserializer=lambda x: loads(x.decode('utf-8')),
                          bootstrap_servers=['159.203.2.190:9092'])

for msg in consumer1:
    data = msg.value

    logger.info(f"{data['method']} {data['entity']}: {data['data']}")
    print(f"{data['method']} {data['entity']}: {data['data']}")
    try:
        getattr(controllers[data['entity']], data['method'])(data['data'])
    except Exception as e:
        print(f'except, sorry: {str(e)}')
        # logger.exception('Oops!', str(sys.exc_info()[0]), 'happened.')
