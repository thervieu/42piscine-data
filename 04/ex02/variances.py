
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import preprocessing


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

    data_scaled = pd.DataFrame(preprocessing.scale(df),columns = df.columns) 
    #
    # Instantiate PCA
    #
    pca = PCA()
    #
    # Determine transformed features
    #
    pca.fit_transform(data_scaled)
    #
    # Determine explained variance using explained_variance_ration_ attribute
    #
    exp_var_pca = pca.explained_variance_ratio_
    #
    # Cumulative sum of eigenvalues; This will be used to create step plot
    # for visualizing the variance explained by each principal component.
    #
    cum_sum_eigenvalues = np.cumsum(exp_var_pca)
    #
    # Print PCA variances
    #
    print(f'Variances (Percentage):\n{pca.explained_variance_ratio_}\n')
    print(f'Cumulative Variances (Percentage):\n{cum_sum_eigenvalues}\n')
    #
    # Find how many features to have 90% of variance
    #
    for i in range(len(cum_sum_eigenvalues)):
        if cum_sum_eigenvalues[i] > 0.90:
            print(f'Cumulative sum of variance is superior to 90% at the {i+1}th value')
            break
    #
    # Create the visualization plot
    #
    plt.bar(range(0,len(exp_var_pca)), exp_var_pca, alpha=0.5, align='center', label='Individual explained variance')
    plt.step(range(0,len(cum_sum_eigenvalues)), cum_sum_eigenvalues, where='mid',label='Cumulative explained variance')
    plt.ylabel('Explained variance ratio')
    plt.xlabel('Principal component index')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    main()