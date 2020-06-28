import nltk


class Preprocessor:
    def __init__(self):
        nltk.download("stopwords")
        self.stopwords = list(nltk.corpus.stopwords.words("portuguese"))

    def preprocess_nlp(self, data):
        data = self.remove_stopwords(data)
        return data

    def remove_stopwords(self, data):
        data["message"] = data.message.apply(self.filter_sentences)
        return data

    def filter_sentences(self, sentence):
        words = sentence.split(" ")
        words = [word for word in words if word not in self.stopwords and word != ""]
        return " ".join(words)


class WhatsAppPreprocessor(Preprocessor):
    def preprocess(self, data):
        data_preprocessed = self.preprocess_data(data)
        data_nlp_preprocessed = self.preprocess_nlp(data_preprocessed)
        return data_nlp_preprocessed

    def preprocess_data(self, data):
        data = data.rename(columns={"message": "total", 0: "name", 1: "message"})
        data = self.drop_garbage_fields_if_exists(data)
        data = self.filter_messages(data)
        return data

    def drop_garbage_fields_if_exists(self, data):
        try:
            data = data.drop("total", axis=1)
        except:
            pass
        try:
            data = data.drop(0)
        except:
            pass
        return data

    def filter_messages(self, data):
        data.loc[data.time.str.contains(r"[a-zA-Z]") == True, "message"] = data[
            data.time.str.contains(r"[a-zA-Z]") == True
        ].time
        data = data.fillna(" ")
        data = data[data.name.str.contains("adicionou|mudou|criou|saiu") == False]
        return data
