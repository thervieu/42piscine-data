import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    if os.path.exists('../assets/Test_knight.csv') is False:
        print('please add the ../assets/Test_knight.csv')
        sys.exit()
    if os.path.exists('../assets/Train_knight.csv') is False:
        print('please add the ../assets/Train_knight.csv')
        sys.exit()

    # get data
    df = pd.read_csv('../assets/Train_knight.csv')

    cols = ['Empowered','Prescience', 'Stims', 'Recovery',
            'Sprint', 'Strength', 'Sensitivity', 'Dexterity',
            'knight']
    
    # cols = ['Empowered','Prescience', 'Stims', 'Recovery',
    #         'Sprint', 'Strength', 'Sensitivity', 'Power',
    #         'Awareness', 'Attunement', 'Dexterity', 'knight']
    df_sim = df[cols]
    sns.pairplot(df_sim, hue='knight')
    plt.show()

    plt.close('all')

    plt.figure()
    dex_jedi = df_sim[df['knight'] == 'Jedi']['Dexterity']
    dex_sith = df_sim[df['knight'] == 'Sith']['Dexterity']
    stims_jedi = df_sim[df['knight'] == 'Jedi']['Stims']
    stims_sith = df_sim[df['knight'] == 'Sith']['Stims']
    jedi = plt.scatter(dex_jedi, stims_jedi, c='b')
    sith = plt.scatter(dex_sith, stims_sith, c='r')
    plt.legend((jedi, sith), ('Jedi', 'Sith'),
           loc='upper left')
    plt.figure()
    df2 = pd.read_csv('../assets/Test_knight.csv')
    dex = df2['Dexterity']
    stims = df2['Stims']
    scatter = plt.scatter(dex, stims, c='g')
    plt.legend((scatter,), ('knight',),
           loc='upper left')

    plt.show()

    plt.close('all')

    cols = ['Reactivity', 'Grasping', 'Repulse',
            'Friendship', 'Mass',  'Midi-chlorien',
            'Push', 'Deflection', 'Survival',
            'knight']
    df_diff = df[cols]
    sns.pairplot(df_diff, hue='knight')
    plt.show()

    plt.close('all')

    plt.figure()
    push_jedi = df_diff[df['knight'] == 'Jedi']['Push']
    push_sith = df_diff[df['knight'] == 'Sith']['Push']
    grasping_jedi = df_diff[df['knight'] == 'Jedi']['Grasping']
    grasping_sith = df_diff[df['knight'] == 'Sith']['Grasping']
    jedi = plt.scatter(grasping_jedi, push_jedi, c='b')
    sith = plt.scatter(grasping_sith, push_sith, c='r')
    plt.legend((jedi, sith), ('Jedi', 'Sith'),
           loc='upper left')
    plt.figure()
    df2 = pd.read_csv('../assets/Test_knight.csv')
    push = df2['Push']
    grasping = df2['Grasping']
    scatter = plt.scatter(push, grasping, c='g')
    plt.legend((scatter,), ('knight',),
           loc='upper left')
    plt.show()

if __name__=="__main__":
    main()