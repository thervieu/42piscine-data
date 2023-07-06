
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant


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
    
    df = pd.read_csv('../assets/Train_knight.csv')
    df = df.drop(['knight'], axis=1)
    # df['knight'] = pd.factorize(df['knight'])[0]
    for col in df:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

    X = add_constant(df)
    VIF            = pd.DataFrame()
    VIF['VIF']     = pd.Series([variance_inflation_factor(X.values, i) for i in range(X.shape[1])], index=X.columns)
    VIF['tolerance'] = 1 / VIF['VIF']
    VIF['features'] = X.columns
    print(VIF)
    print()
    print(f'Features with VIF < 5.0')
    for (i, row) in enumerate(X.columns):
        # print(i, row)
        # print(VIF['features'][i])
        # print(VIF['VIF'][i])
        if VIF['features'][i] == row and VIF['VIF'][i] < 5.0:
            print(row)

if __name__=="__main__":
    main()