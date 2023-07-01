import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler


def open_data(path="data/cars.csv"):
    df = pd.read_csv(path)
    return df


def fieldSrt2float(x: str):
    return float(x.split()[0])


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df.dropna(inplace=True)
    df.drop(['name', 'fuel', 'seller_type', 'engine', 'torque', 'mileage'], axis=1, inplace=True)
    df = df[(df['km_driven'] <= 1000000)]
    df['owner'] = df['owner'].map({'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Fourth & Above Owner': 4,
                                   'Test Drive Car': 0})
    df['transmission'] = df['transmission'].map({'Manual': 1, 'Automatic': 0})
    df['max_power'] = df['max_power'].map(fieldSrt2float)
    print(f'preprocess_data: {df.shape}')
    print(f'preprocess_data: {list(df.columns)}')
    return df


def split_data(df: pd.DataFrame):
    X = df.drop(['selling_price'], axis=1)
    y = df['selling_price']
    print(f'split_data: {X.shape} {y.shape}')
    return X, y


def get_ready_forecast():
    df = open_data()
    df = preprocess_data(df)
    X, _ = split_data(df)
    scalar_num = MinMaxScaler()
    scalar_num.fit(X)
    return scalar_num


def scalar_data(df: pd.DataFrame, ss: MinMaxScaler) -> pd.DataFrame:
    return pd.DataFrame(ss.transform(df), columns=df.columns)
