
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def main():
    if os.path.exists(f'../assets/Train_knight.csv') is False:
        print(f'please add the ../assets/Train_knight.csv')
        return
    
    df = pd.read_csv('../assets/Train_knight.csv')
    df['knight'] = pd.factorize(df['knight'])[0]
    # calculate the correlation matrix on the numeric columns
    corr = df.select_dtypes('number').corr()

    # plot the heatmap
    sns.heatmap(corr)
    plt.show()

if __name__=="__main__":
    main()