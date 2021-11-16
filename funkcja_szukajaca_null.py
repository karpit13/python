import pandas as pd

"""#data = pd.read_csv('Data/medals.csv')
print(data.isnull().sum().sum())"""

def licz_null(plik):
    data = pd.read_csv(plik)
    print(data.isnull().sum().sum())
