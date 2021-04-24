from math import sqrt

import numpy as np
import pandas as pd


def load_and_examine_data():
    df = pd.read_csv('/Users/ritabrata/Learn/ML_Algo_From_Scratch/data/AutoInsurance.csv')
    print("Sample data \n", df.head())
    print("Data types \n", df.dtypes)
    return df


def mean(arr):
    temp_sum = 0

    for i in arr:
        temp_sum = temp_sum + i

    return temp_sum / len(arr)


def covariance(x, x_mean, y, y_mean):
    covariance_x_y = 0

    for i in range(0, len(x)):
        covariance_x_y += (x[i] - x_mean) * (y[i] - y_mean)

    return covariance_x_y


def variance(arr, arr_mean):
    variance_arr = 0

    for elem in arr:
        variance_arr += (elem - arr_mean) ** 2

    return variance_arr


def estimate_parameters(df):
    x = df['X'].values
    y = df['Y'].values

    x_mean = mean(x)
    y_mean = mean(y)
    covariance_x_y = covariance(x, x_mean, y, y_mean)

    b1 = covariance_x_y / variance(x, x_mean)
    b0 = y_mean - b1 * x_mean

    return b0, b1


def train_test_split(df, split_ratio):
    df['rand_index'] = np.random.randint(0, 100, len(df))

    train_df = df[df['rand_index'] < split_ratio * 100].drop(columns='rand_index')
    test_df = df[df['rand_index'] >= split_ratio * 100].drop(columns='rand_index')

    return train_df, test_df


def predict_for_test_data(test_data, b0, b1):
    test_data['predicted_Y'] = b0 + test_data['X'] * b1
    return test_data


def calculate_rmse(predictions):
    predictions['error'] = predictions['predicted_Y'] - predictions['Y']
    predictions['sq_error'] = predictions['error'] ** 2

    mean_error = np.mean(predictions['sq_error'])
    return sqrt(mean_error)


def main():
    df = load_and_examine_data()
    train_data, test_data = train_test_split(df, 0.6)
    print(df.shape, train_data.shape, test_data.shape)

    b0, b1 = estimate_parameters(train_data)

    predictions = predict_for_test_data(test_data, b0, b1)
    rmse = calculate_rmse(predictions)
    print(rmse)


if __name__ == '__main__':
    main()
