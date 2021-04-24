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


def main():
    df = load_and_examine_data()

    linear_regression_parameters = estimate_parameters(df)
    print(linear_regression_parameters)


if __name__ == '__main__':
    main()
