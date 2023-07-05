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
    if len(sys.argv) != 2:
        print("Please tell with which dataset to work with: train or test")
        return
    if sys.argv[1] not in ["Train", 'Test']:
        print("Please tell with which dataset to work with: train or test")
        return

    if os.path.exists(f'../assets/{sys.argv[1]}_knight.csv') is False:
        print(f'please add the ../assets/{sys.argv[1]}_knight.csv')
        return

    # get data
    df = pd.read_csv(f'../assets/{sys.argv[1]}_knight.csv')

    print(df)
    plt.figure()
    if sys.argv[1] == 'Train':
        dex_jedi = df[df['knight'] == 'Jedi']['Dexterity']
        dex_sith = df[df['knight'] == 'Sith']['Dexterity']
        stims_jedi = df[df['knight'] == 'Jedi']['Stims']
        stims_sith = df[df['knight'] == 'Sith']['Stims']
        jedi = plt.scatter(dex_jedi, stims_jedi, c='b')
        sith = plt.scatter(dex_sith, stims_sith, c='r')
        plt.legend((jedi, sith), ('Jedi', 'Sith'),
            loc='upper left')
    else:
        dex = df['Dexterity']
        stims = df['Stims']
        scatter = plt.scatter(dex, stims, c='g')
        plt.legend((scatter,), ('knight',),
            loc='upper left')
    for col in get_numeric_cols(df):
        max = df[col].max()
        min = df[col].min()
        df[col] = (df[col] - min) / (max - min)
    print()
    print()
    print()
    print(df)
    plt.figure()
    if sys.argv[1] == 'Train':
        dex_jedi = df[df['knight'] == 'Jedi']['Dexterity']
        dex_sith = df[df['knight'] == 'Sith']['Dexterity']
        stims_jedi = df[df['knight'] == 'Jedi']['Stims']
        stims_sith = df[df['knight'] == 'Sith']['Stims']
        jedi = plt.scatter(dex_jedi, stims_jedi, c='b')
        sith = plt.scatter(dex_sith, stims_sith, c='r')
        plt.legend((jedi, sith), ('Jedi', 'Sith'),
            loc='upper left')
    else:
        dex = df['Dexterity']
        stims = df['Stims']
        scatter = plt.scatter(dex, stims, c='g')
        plt.legend((scatter,), ('knight',),
            loc='upper left')

    plt.show()

if __name__=="__main__":
    main()