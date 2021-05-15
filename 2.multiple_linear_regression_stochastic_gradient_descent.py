import pandas as pd


def predict(arr, coef):
    yhat = coef[0]

    for col_index in range(len(arr) - 1):
        yhat += arr[col_index] * coef[col_index + 1]

    return yhat


def coefficients_sgd(df, l_rate, n_epoch):
    coef = [0.0 for _ in range(0, df.shape[1])]

    for n in range(0, n_epoch):
        sum_error = 0.0

        for row in df.values:
            yhat = predict(row, coef)
            y = row[-1]
            error = yhat - y
            sum_error += error ** 2

            coef[0] = coef[0] - error * l_rate

            for col_index in range(len(row) - 1):
                coef[col_index + 1] = coef[col_index + 1] - (row[col_index] * l_rate * error)

        print(f"Epoch# = {n} lrate = {l_rate}, error = {sum_error}")

    return coef


def min_max_normalise(df):
    df = (df - df.mean()) / (df.max() - df.min())
    return df


def main():
    df = pd.read_csv('/Users/ritabrata/Learn/ML_Algo_From_Scratch/data/WineQuality.csv')
    df_1 = min_max_normalise(df)
    # print(df_1)

    l_rate = 0.01
    n_epoch = 1000

    coef = coefficients_sgd(df_1, l_rate, n_epoch)
    print(coef)


if __name__ == '__main__':
    main()
