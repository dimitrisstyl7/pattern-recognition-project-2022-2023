import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import numpy as np
import scipy.stats as stats
import math


def load_data():
    data = pd.read_csv(r'housing.csv')
    numerical_data = data.drop("ocean_proximity", axis=1)
    categorical_data = data["ocean_proximity"]
    return numerical_data, categorical_data

def one_hot_encoding(data):
    return OneHotEncoder().fit_transform(data.reshape(-1, 1)).toarray()

def normalize_data(data):
    return MinMaxScaler((0,1)).fit_transform(data.reshape(-1, 1))

def check_values(numerical_data):
    for label in numerical_data:
        column = sorted(list(numerical_data[label]))
        if len(column) % 2 == 0:
            median = (column[len(column) // 2 - 1] + column[len(column) // 2]) / 2
        else:
            median = column[len(column) // 2]
        for i in range(len(numerical_data[label])):
            if math.isnan(numerical_data[label][i]):
                    numerical_data[label][i] = median
    return numerical_data

def calculate_pdf(data):
    pdf_list = []
    for i in range(len(data)):
        column = list(data[i])
        pdf = stats.norm.pdf(column, np.mean(column), np.std(column))
        pdf_list.append(pdf)
    return pdf_list

if __name__ == '__main__':
    numerical_data, categorical_data = load_data()
    categorical_data_encoded = one_hot_encoding(np.array(list(categorical_data)))
    numerical_data = check_values(numerical_data)
    normalized_numerical_data = normalize_data(np.array(numerical_data))
    pdf_list = calculate_pdf(normalized_numerical_data)
    
    #data = list(categorical_data_encoded)
    #pdf_list.append(stats.norm.pdf(data, np.mean(data), np.std(data)))
    data = list(categorical_data_encoded)
    pdf_list.append(stats.norm.pdf(data, np.mean(data), np.std(data)))
    print(len(pdf_list))
