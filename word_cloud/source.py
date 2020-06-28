from .dataloader import WhatsAppDataLoader
from .preprocessors import WhatsAppPreprocessor

class Source():
    def load_data(self, path):
        return self.dataloader.load_data(path)

    def preprocess(self, data):
        return self.preprocessor.preprocess(data)

class WhatsApp(Source):
    def __init__(self):
        self.dataloader = WhatsAppDataLoader()
        self.preprocessor = WhatsAppPreprocessor()