from .source import WhatsApp

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class TextLoader():
    def __init__(self): logger.warning('WARNING: TextLoader only works with WhatsApp messages!')
    def load_text(self, path):
        wpp = WhatsApp()
        data = wpp.load_data(path)
        data = wpp.preprocess(data)
        return data