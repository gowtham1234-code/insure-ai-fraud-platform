import pandas as pd

def load_claims(path):
    return pd.read_csv(path)

def load_history(path):
    return pd.read_csv(path)

def load_requirements(path):
    return pd.read_csv(path)