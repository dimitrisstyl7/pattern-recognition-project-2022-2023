import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def load_data():
    data = pd.read_csv(r'housing.csv')
    numerical_data = data.drop("ocean_proximity", axis=1)
    categorical_data = data["ocean_proximity"]
    return numerical_data, categorical_data

def one_hot_encoding(data):
    return OneHotEncoder().fit_transform(data.reshape(-1, 1)).toarray()

def normalize_data(data): # normalize data to range [0, 1]
    return MinMaxScaler((0,1)).fit_transform(data)

def calculate_pdf(data):
    pdf_list = []
    for i in range(data.shape[1]):
        column = data[:, i]
        pdf = stats.norm.pdf(column, np.mean(column), np.std(column)).mean()
        pdf_list.append(pdf)
    return pdf_list

def plot_pdf_histograms(pdf_list, normalized_numerical_data, numerical_data_columns):
    for i in range(normalized_numerical_data.shape[1]):
        column = normalized_numerical_data[:, i]
        x = np.linspace(column.min(), column.max(), 100)
        y = stats.norm.pdf(x, np.mean(column), np.std(column))
        plt.hist(column, bins=20, density=True)
        plt.plot(x, y, '-r', label='pdf')
        plt.legend()
        plt.title(numerical_data_columns[i])
        plt.show()

def _2d_scatter_plot_with_2_attributes(data_columns_names, data_columns_values):
    x = data_columns_values[data_columns_names[0]] # attribute 1
    y = data_columns_values[data_columns_names[1]] # attribute 2
    plt.scatter(x, y, c='blue')
    plt.xlabel(x)
    plt.ylabel(y)
    title = 'Scatter plot of {} - {}'.format(x, y)
    plt.title(title)
    plt.show()

def _2d_scatter_plot_with_3_attributes(data_columns_names, data_columns_values):
    x = data_columns_values[data_columns_names[0]] # attribute 1
    y = data_columns_values[data_columns_names[1]] # attribute 2
    color = data_columns_values[data_columns_names[2]] # attribute 3
    color_label = data_columns_names[2]
    cmap_value = 'viridis'
    plt.scatter(x, y, c=color, cmap=cmap_value)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.colorbar(label=color_label) # plt.colorbar().set_label(color_label)
    title = 'Scatter plot of {} - {} - {}'.format(x, y, color)
    plt.title(title)
    plt.show()
    
def _2d_scatter_plot_with_4_attributes(data_columns_names, data_columns_values):
    x = data_columns_values[data_columns_names[0]] # attribute 1
    y = data_columns_values[data_columns_names[1]] # attribute 2
    color = data_columns_values[data_columns_names[2]] # attribute 3
    size = data_columns_values[data_columns_names[3]] # attribute 4
    color_label = data_columns_names[2]
    cmap_value = 'viridis'
    plt.scatter(x, y, c=color, cmap=cmap_value, size=size)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.colorbar(label=color_label) # plt.colorbar().set_label(color_label)
    title = 'Scatter plot of {} - {} - {} - {}'.format(x, y, color, size)
    plt.title(title)
    plt.show()

if __name__ == '__main__':
    numerical_data, categorical_data = load_data()
    numerical_data_columns = numerical_data.columns
    categorical_data_encoded = one_hot_encoding(np.array(list(categorical_data.values)))
    numerical_data = numerical_data.fillna(numerical_data.median()) # fill missing values with median
    normalized_numerical_data = normalize_data(np.array(numerical_data))
    pdf_list = calculate_pdf(normalized_numerical_data) # calculate pdf for each column of numerical data
    pdf_list.append(calculate_pdf(categorical_data_encoded)) # calculate pdf for categorical data
    #plot_pdf_histograms(pdf_list, normalized_numerical_data, numerical_data_columns)
    
    ''' build again the data columns names and values '''
    data_columns_names = list(numerical_data_columns)
    data_columns_names.append("ocean_proximity")
    data_columns_values = list(normalized_numerical_data)
    data_columns_values.append(categorical_data_encoded)
    
    #_2d_scatter_plot_with_2_attributes(data_columns_names, data_columns_values)
    #_2d_scatter_plot_with_3_attributes(data_columns_names, data_columns_values)
    #_2d_scatter_plot_with_4_attributes(data_columns_names, data_columns_values)