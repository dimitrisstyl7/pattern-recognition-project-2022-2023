import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import numpy as np
import math


def load_data():
    data = pd.read_csv(r'housing.csv')
    numerical_data = data.drop("ocean_proximity", axis=1)
    categorical_data = data["ocean_proximity"]
    return numerical_data, categorical_data

def one_hot_encoding(data):
    return OneHotEncoder().fit_transform(data.reshape(-1, 1)).toarray()

def normalize_data(data):
    scaler = MinMaxScaler()
    return scaler.fit_transform(data)
    
if __name__ == '__main__':
    numerical_data, categorical_data = load_data()
    numerical_columns_names = numerical_data.columns
    categorical_data = list(categorical_data)
    categorical_data_encoded = one_hot_encoding(np.array(categorical_data))
    counter = 0
    
    for label in numerical_data:
        column = sorted(list(numerical_data[label]))
        if len(column) % 2 == 0:
            median = (column[len(column) // 2 - 1] + column[len(column) // 2]) / 2
        else:
            median = column[len(column) // 2]
        for i in range(len(numerical_data[label])):
            if math.isnan(numerical_data[label][i]):
                    numerical_data[label][i] = median
                    counter += 1