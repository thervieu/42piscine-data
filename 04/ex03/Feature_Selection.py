
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor


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
    for col in df:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    
    VIF            = pd.DataFrame()
    VIF['feature'] = df.columns
    VIF['VIF']     = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
    VIF['tolerance'] = 1 / VIF['VIF']
    print(VIF)

if __name__=="__main__":
    main()