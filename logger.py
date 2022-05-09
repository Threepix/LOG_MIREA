import logging
from logging import StreamHandler, Formatter
import sys

logger = logging.getLogger(__name__)


class Debug:
    def __init__(self,message):
        self.message = message
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        handler = StreamHandler(stream=sys.stdout)
        handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
        logger.addHandler(handler)
        logger.debug(message)

