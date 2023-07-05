import os, sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

def confusion_matrix(truth, predictions):
    cm = np.array([[0, 0], [0, 0]])
    for t, p in zip(truth, predictions):
        if t == 'Jedi':
            if p == 'Jedi':
                cm[0][0] += 1
            else:
                cm[0][1] += 1
        else:
            if p == 'Jedi':
                cm[1][0] += 1
            else:
                cm[1][1] += 1
    print(f'       precision   recall  f-score  total')
    print(f'')
    pJedi = cm[0][0]/(cm[0][0]+cm[1][0])
    pSith = cm[1][1]/(cm[1][1]+cm[0][1])
    rJedi = cm[0][0]/(cm[0][0]+cm[0][1])
    rSith = cm[1][1]/(cm[1][1]+cm[1][0])
    print(f'Jedi        {pJedi:.2}     {rJedi:.2}     {2*(rJedi*pJedi)/(rJedi+pJedi):.2}     {cm[0][0]+cm[0][1]}')
    print(f'Sith        {pSith:.2}     {rSith:.2}     {2*(rSith*pSith)/(rSith+pSith):.2}     {cm[1][0]+cm[1][1]}')
    print()
    print(f'accuracy                      {(cm[0][0]+cm[1][1])/(cm[0][0]+cm[1][0]+cm[0][1]+cm[1][1])}    {cm[0][0]+cm[1][0]+cm[0][1]+cm[1][1]}')
    print()
    return cm

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 Confusion_Matrix.py predictions.txt truth.txt")
        return
    if sys.argv[1] != "predictions.txt" or sys.argv[2] != "truth.txt":
        print("Usage: python3 Confusion_Matrix.py predictions.txt truth.txt")
    if os.path.exists(f'../assets/predictions.txt') is False:
        print(f'please add the ../assets/predictions.txt')
        sys.exit()
    if os.path.exists(f'../assets/truth.txt') is False:
        print(f'please add the ../assets/truth.txt')
        sys.exit()

    fpred = open(f"../assets/predictions.txt", "r")
    ftruth = open(f"../assets/truth.txt", "r")
    lpred = fpred.read().splitlines()
    ltruth = ftruth.read().splitlines()
    fpred.close()
    ftruth.close()
    # cm = metrics.confusion_matrix(ltruth, lpred)
    cm = confusion_matrix(ltruth, lpred)
    print(cm)
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm)
    cm_display.plot()
    plt.show()

if __name__=="__main__":
    main()