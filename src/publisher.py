import json

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

producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for value in values:
    print(value)
    producer.send('main', value)
    producer.flush()
