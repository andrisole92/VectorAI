import logging
import random

logger = logging

logger.basicConfig(filename="logFile.txt",
                   filemode='a',
                   format='%(asctime)s %(levelname)s-%(message)s',
                   datefmt='%Y-%m-%d %H:%M:%S',
                   level=logging.DEBUG)
