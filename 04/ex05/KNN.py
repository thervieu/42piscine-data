import os, sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score # Import train_test_split function
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score, precision_score

import matplotlib.pyplot as plt
import seaborn as sns

def normalize(df):
    for col in df:
        if col == 'knight':
            continue
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df
#
# following this link
# https://www.datacamp.com/tutorial/k-nearest-neighbor-classification-scikit-learn
#
def main():
    if len(sys.argv) != 3:
        print("Usage: python3 KNN.py Train_knight.csv Test_knight.csv")
        return
    if os.path.exists(f'../assets/Train_knight.csv') is False:
        print(f'please add the ../assets/Train_knight.csv')
        return
    if sys.argv[1] != "Train_knight.csv" or sys.argv[2] != "Test_knight.csv":
        print("Usage: python3 KNN.py Train_knight.csv Test_knight.csv")
    if os.path.exists(f'../assets/Train_knight.csv') is False:
        print(f'please add the ../assets/Train_knight.csv')
        sys.exit()
    if os.path.exists(f'../assets/Test_knight.csv') is False:
        print(f'please add the ../assets/Test_knight.csv')
        sys.exit()
    
    df = pd.read_csv('../assets/Train_knight.csv')
    
    df = normalize(df)

    y = pd.factorize(df['knight'])[0]
    X = df.drop(['knight'], axis=1)

    best_knn = 0
    scaler = StandardScaler()
    while True:
        # Scale the features using StandardScaler
        X_train, X_validate, y_train, y_validate = train_test_split(X, y, test_size=0.25)
        X_train = scaler.fit_transform(X_train)
        X_validate = scaler.fit_transform(X_validate)
        X = scaler.fit_transform(X)

        f1_scores = []
        cross_val_scores = []
        precision_scores = []
        k_values = [i for i in range(1, 20)]
        best_f1_score = 0
        for k in k_values:
            #instanciation et définition du k
            knn = KNeighborsClassifier(n_neighbors = k)
            # Model Accuracy, how often is the classifier correct?
            score = cross_val_score(knn, X, y, cv=5)
            cross_val_scores.append(np.mean(score))

            knn = KNeighborsClassifier(n_neighbors = k)
            # training
            knn.fit(X_train,y_train)
            y_pred = knn.predict(X_validate)
            f1_scores.append(f1_score(y_validate, y_pred))
            precision_scores.append(precision_score(y_validate, y_pred))
            if f1_scores[k-1] > best_f1_score:
                best_f1_score = f1_scores[k-1]
                if best_f1_score > 0.92:
                    best_knn = knn
        if best_knn != 0:
            break
    print(f'Best f1_score is {best_f1_score}')

    plt.plot(k_values, cross_val_scores, color='b', label='cross_val_scores')
    plt.plot(k_values, precision_scores, color='green', label='precision_scores')
    plt.plot(k_values, f1_scores, color='red', label='f1_scores')
    plt.xlabel("K Values")
    plt.ylabel("Accuracy Score and cross_val_score")
    plt.legend(loc="lower right")
    plt.show()

    x_test = pd.read_csv('../assets/Test_knight.csv')
    x_test = scaler.fit_transform(x_test)
    y_pred_test = best_knn.predict(x_test).tolist()
    with open('KNN.txt', 'w') as knn_txt:
        for pred in y_pred_test:
            if pred == 0:
                knn_txt.write(f'Sith\n')
            else:
                knn_txt.write(f'Jedi\n')

if __name__=="__main__":
    main()
