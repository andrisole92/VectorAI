import json
import random
from src.model.model import Continent, Country, City

from kafka import KafkaProducer

values = [
    {'entity': 'countrys', 'method': 'post', 'data': {
        'population': 2000,
        'area': 3001
    }},
    {'entity': 'country', 'method': 'post', 'data': {
        'population': 2000,
        'area': 3002
    }},
    {'entity': 'country', 'method': 'post', 'data': {
        'population': 2000,
        'area': 3003
    }},
    {'entity': 'country', 'method': 'post', 'data': {
        'population': 2000,
        'area': 3004
    }},
    {'entity': 'country', 'method': 'post', 'data': {
        'population': 2000,
        'area': 3005
    }},
    {'entity': 'country', 'method': 'post', 'data': {
        'population': 2000,
        'area': 3001
    }},
    {'entity': 'country', 'method': 'post', 'data': {
        'population': 2000,
        'area': 3001
    }},
    {'entity': 'country', 'method': 'post', 'data': {
        'population': 2000,
        'area': 3001
    }},
    {'entity': 'country', 'method': 'post', 'data': {
        'population': 2000,
        'area': 3001
    }},
    {'entity': 'country', 'method': 'post', 'data': {
        'population': 2000,
        'area': 3001
    }},
    {'entity': 'country', 'method': 'post', 'data': {
        'population': 2000,
        'area': 3001
    }},
    {'entity': 'country', 'method': 'post', 'data': {
        'population': 2000,
        'area': 3001
    }},

]


producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         bootstrap_servers=['159.203.2.190:9092'])

for value in range(300):
    print(value)
    producer.send('main', random.choice(
        [
            {'entity': 'continent', 'method': random.choice(['post', 'put', 'delete']), 'data': Continent.get_sample()},
            {'entity': 'country', 'method': random.choice(['post', 'put', 'delete']), 'data': Country.get_sample()},
            {'entity': 'city', 'method': random.choice(['post', 'put', 'delete']), 'data': City.get_sample()},
        ]))
    producer.flush()
