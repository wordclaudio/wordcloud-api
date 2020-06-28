from PIL import Image
from os import path
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud


class WordCloudGenerator:
    def __init__(self, image_path: str = None):
        self.image_mask = (
            np.array(Image.open(image_path)) if image_path is not None else None
        )

    def generate_wordcloud_from_text(self, text, uuid):
        wc = WordCloud(
            background_color="white",
            max_words=200,
            mask=self.image_mask,
            colormap="RdBu",
        )
        wc.generate(text)
        wc.to_file(uuid + ".png")
