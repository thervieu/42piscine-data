import os, sys
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculatio

from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus

def normalize(df):
    for col in df:
        if col == 'knight':
            continue
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df
#
# following this link
# https://www.datacamp.com/tutorial/decision-tree-classification-python
#
def main():
    if len(sys.argv) != 3:
        print("Usage: python3 Tree.py Train_knight.csv Test_knight.csv")
        return
    if os.path.exists(f'../assets/Train_knight.csv') is False:
        print(f'please add the ../assets/Train_knight.csv')
        return
    if sys.argv[1] != "Train_knight.csv" or sys.argv[2] != "Test_knight.csv":
        print("Usage: python3 Tree.py Train_knight.csv Test_knight.csv")
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

    clf = DecisionTreeClassifier()
    while True:
        X_train, X_validate, y_train, y_validate = train_test_split(X, y, test_size=0.25)

        # Create Decision Tree classifer object
        clf = DecisionTreeClassifier()

        # Train Decision Tree Classifer
        clf = clf.fit(X_train,y_train)

        #Predict the response for test dataset
        y_pred = clf.predict(X_validate)
        if metrics.f1_score(y_validate, y_pred) > 0.9:
            break

    # Model Accuracy, how often is the classifier correct?
    print("f1_score of the Decision Tree:", metrics.f1_score(y_validate, y_pred))
    print("Accuracy of the Decision Tree:", metrics.accuracy_score(y_validate, y_pred))

    dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data,  
                    filled=True, rounded=True,
                    special_characters=True,
                    feature_names=X.columns,
                    class_names=['Sith','Jedi'])
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_png('Tree.png')
    Image(graph.create_png())

    x_test = pd.read_csv('../assets/Test_knight.csv')
    x_test = normalize(x_test)
    y_pred_test = clf.predict(x_test).tolist()

    with open('Tree.txt', 'w') as tree_txt:
        for pred in y_pred_test:
            if pred == 0:
                tree_txt.write(f'Sith\n')
            else:
                tree_txt.write(f'Jedi\n')

if __name__=="__main__":
    main()
