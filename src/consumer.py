import sys
from json import loads

from db import Engine
from model.model import Base
from kafka import KafkaConsumer

from src.controllers.controllers import controllers
from src.logger import logger

Base.metadata.create_all(Engine.get_engine())
print(getattr(controllers['city'], 'post'))

consumer1 = KafkaConsumer('main', value_deserializer=lambda x: loads(x.decode('utf-8')))

for msg in consumer1:
    logger.info(f'Received: {msg.value}')
    value = msg.value
    print(value)
    try:
        getattr(controllers[value['entity']], value['method'])(value['data'])
    except:
        logger.exception('Oops!', str(sys.exc_info()[0]), 'happened.')
