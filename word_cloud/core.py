from .text import TextLoader
from .nlp import NLP
from .wordcloud import WordCloudGenerator


def generate_wordcloud_from_chat(uuid):
    preprocessed_text = TextLoader().load_text(uuid + ".txt")
    keywords = NLP().get_keywords(preprocessed_text)
    text = " ".join(keywords)
    return WordCloudGenerator().generate_wordcloud_from_text(text, uuid)
