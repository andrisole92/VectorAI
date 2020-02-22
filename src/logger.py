import logging
import logstash

logger = logging.getLogger('test')

logger.setLevel(logging.INFO)
logger.addHandler(logstash.LogstashHandler('159.203.2.190', 5000, version=1))
logger.addHandler(logstash.TCPLogstashHandler('159.203.2.190', 5000, version=1))
#
#
# logger.basicConfig(filename="logFile.txt",
#                    filemode='a',
#                    format='%(asctime)s %(levelname)s-%(message)s',
#                    datefmt='%Y-%m-%d %H:%M:%S',
#                    level=logging.DEBUG)
# logger.error('python-logstash: test logstash error message.')
# logger.info('python-logstash: test logstash info message.')
# logger.warning('python-logstash: test logstash warning message.')

# add extra field to logstash message
extra = {
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}
# logger.info('python-logstash: test extra fields', extra=extra)
# logger.info('python-logstash: test extra fields', extra=extra)
# logger.info('python-logstash: test extra fields', extra=extra)
# logger.info('python-logstash: test extra fields', extra=extra)
# logger.info('python-logstash: test extra fields', extra=extra)
# logger.info('python-logstash: test extra fields', extra=extra)
# logger.info('python-logstash: test extra fields', extra=extra)