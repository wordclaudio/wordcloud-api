from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from .preprocessors import Preprocessor

class NLP():
    def __init__(self):
        self.preprocessor = Preprocessor()
        self.tfidf = TfidfVectorizer(stop_words=self.preprocessor.stopwords, max_features=100)

    def get_keywords(self, data):
        self.tfidf.fit_transform(data["message"])
        keywords = [word[0] for word in self.tfidf.vocabulary_.items() if word[1] < 30]
        return keywords