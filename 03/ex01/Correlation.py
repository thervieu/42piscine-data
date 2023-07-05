import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    if os.path.exists('../assets/Train_knight.csv') is False:
        print('please add the ../assets/Train_knight.csv')
        sys.exit()

    # get data
    df = pd.read_csv('../assets/Train_knight.csv')
    df.knight = pd.Categorical(df.knight)
    df['knight'] = pd.factorize(df['knight'])[0]
    print(df.corr()['knight'].sort_values()[::-1])

if __name__=="__main__":
    main()