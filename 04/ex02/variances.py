
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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
    
    variances = []
    for col in get_numeric_cols(df):
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
        variances.append(df[col].var() * 100)
    variances = sorted(variances)[::-1]
    print(variances)
    print()
    var_per = variances / sum(variances) * 100
    print(var_per)
    print()
    sum_var = 0
    for i in range(len(variances)):
        sum_var += var_per[i]
        print(sum_var)

if __name__=="__main__":
    main()