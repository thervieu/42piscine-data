import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_numeric_cols(df):
    numeric_cols = []
    for col_name in df.columns:
        try:
            float(df[col_name][0])
            numeric_cols.append(col_name)
        except ValueError:
            continue
    return numeric_cols

def get_grades_colum(df, col):
    dfGrades = df[col]
    return dfGrades

def get_grades_knight_column(df, house_name, col):
    dfGrades = df[df['knight'] == house_name][col]
    return dfGrades

def normal():
    # check exists
    if os.path.exists('../assets/Test_knight.csv') is False:
        print('please add the ../assets/Test_knight.csv')
        sys.exit()

    # get data
    df = pd.read_csv('../assets/Test_knight.csv')
    num_cols = get_numeric_cols(df)

    # print each histo and normalized data
    for col in num_cols:
        plt.figure()
        plt.hist(get_grades_colum(df, col), bins=40)

        plt.title(col)
    plt.show()

def main():
    print(len(sys.argv))
    if len(sys.argv) != 2:
        print("Please input the mode you want: normal or compare")
        return
    if sys.argv[1] == "normal":
        normal()
        return
    elif sys.argv[1] != "compare":
        print("Please input the mode you want: normal or compare")
        return

    if os.path.exists('../assets/Train_knight.csv') is False:
        print('please add the ../assets/Train_knight.csv')
        sys.exit()
        
    plt.rcParams.update({'figure.max_open_warning': 0})

    # get data
    df = pd.read_csv('../assets/Train_knight.csv')
    num_cols = get_numeric_cols(df)
    for col in num_cols:
        plt.figure()
        plt.hist(get_grades_knight_column(df, "Sith", col), bins=40, alpha=0.5, label = 'Sith', color = 'r')
        plt.hist(get_grades_knight_column(df, "Jedi", col), bins=40, alpha=0.5, label = 'Jedi', color = 'b')
        plt.title(col)
    plt.show()

if __name__=="__main__":
    main()