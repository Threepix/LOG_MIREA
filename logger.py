import logging
from logging import StreamHandler, Formatter
import sys


class Debug:
    def __init__(self,message):
        self.message = message
        logger = logging.getLogger('logger')
        logger.setLevel(logging.DEBUG)
        handler = StreamHandler(stream=sys.stdout)
        handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
        logger.addHandler(handler)
        logger.debug(message)

class Info:
    def __init__(self,message):
        self.message = message
        ligger = logging.getLogger('ligger')
        ligger.setLevel(logging.INFO)
        handler = StreamHandler(stream=sys.stdout)
        handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
        ligger.addHandler(handler)
        ligger.info(message)

class Error:
    def __init__(self,message):
        self.message = message
        lagger = logging.getLogger('lagger')
        lagger.setLevel(logging.ERROR)
        handler = StreamHandler(stream=sys.stdout)
        handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
        lagger.addHandler(handler)
        lagger.error(message)
