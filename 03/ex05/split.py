import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def get_numeric_cols(df):
    numeric_cols = []
    for col_name in df.columns:
        try:
            float(df[col_name][0])
            numeric_cols.append(col_name)
        except ValueError:
            continue
    return numeric_cols


def main():
    if os.path.exists(f'../assets/Train_knight.csv') is False:
        print(f'please add the ../assets/Train_knight.csv')
        return

    # get data
    df = pd.read_csv(f'../assets/Train_knight.csv')

    # df = df.sample(frac=1)

    training, validation = train_test_split(df, test_size=0.2)
    print(len(training))
    print(len(validation))
    print(validation)
    training.to_csv('../assets/Training_knight.csv')
    validation.to_csv('../assets/Validation_knight.csv')

if __name__=="__main__":
    main()