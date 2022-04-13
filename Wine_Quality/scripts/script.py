from scripts.variables import DATASETS

def load_data(dataset):
    import pandas as pd
    return pd.read_csv(DATASETS[dataset])