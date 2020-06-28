import pandas as pd

class DataLoader():
    pass

class WhatsAppDataLoader(DataLoader):
    def load_data(self, path):
        df_raw = pd.read_csv(path, sep=r'-', names=['time', 'message'])
        df_splitted_messages = df_raw['message'].str.split(":", expand=True, n=1)
        return pd.concat([df_raw, df_splitted_messages], axis=1)