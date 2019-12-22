# -*- coding: utf-8 -*-
"""DawaniSonam_HW2_Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dFi_LKXZ3xOj2-cKgzcbpJt2q88_NyqC

Task 2: Read the data from your Quantitative.csv file to a new Panda’s data frame and generate all info that you may need to create Summary Table in Data Quality Report for Continuous Features. Then show equal‐width histograms (make sure to pick the right number of bins to show accurately the data distribution), and horizontal violin plots. Then move on to pair‐wise analyses: show scatter plot matrix, covariance and correlation tables, and heat maps for both of these tables. Are the heat maps of the covariance and correlation tables any different? Should they be? Can you tell me about any observations I made about quantitative attributes so far? Which of the generated results helped you made those observations?
"""

#Task 2
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

#Copying Task 1, so that even if Task 1 is not executed before this, Task 2 can have Quantitative.csv
#Task 1
dataPreP = pd.read_csv("dataPreP.csv") 
Quantitative=dataPreP[['Attr 4','Attr 5','Attr 6','Attr 7','Attr 8','Attr 9','Attr 10','Attr 11','Attr 12',]]
Quantitative.to_csv('Quantitative.csv',index=False)
Others=dataPreP[['Attr 0','Attr 1','Attr 2','Attr 3','Labels',]]
Others.to_csv('Others.csv',index=False)
#Task 1 ends


Quantitative=pd.read_csv("Quantitative.csv") 
Quantitative_DQR=Quantitative.describe().T
missPer=Quantitative[['Attr 4','Attr 5','Attr 6','Attr 7','Attr 8','Attr 9','Attr 10','Attr 11','Attr 12']].isna().sum()/Quantitative.count()
card=Quantitative.nunique()
Quantitative_DQR['miss%']=missPer
Quantitative_DQR['card']=card
cols=['count', 'miss%','card','min','25%','mean', '50%','75%', 'max','std']
Quantitative_DQR=Quantitative_DQR[cols] #rearranging
print('Quantitative_DQR:')
print(tabulate(Quantitative_DQR, headers='keys', tablefmt='psql'))


Quantitative.hist(bins=20,figsize=(20,20))

a4_dims = (12, 12)
fig, axes = plt.subplots(3,3,figsize=a4_dims)
sns.violinplot(data=Quantitative['Attr 4'],ax=axes[0, 0])
sns.violinplot(data=Quantitative['Attr 5'],ax=axes[0, 1])
sns.violinplot(data=Quantitative['Attr 6'],ax=axes[0, 2])
sns.violinplot(data=Quantitative['Attr 7'],ax=axes[1, 0])
sns.violinplot(data=Quantitative['Attr 8'],ax=axes[1, 1])
sns.violinplot(data=Quantitative['Attr 9'],ax=axes[1, 2])
sns.violinplot(data=Quantitative['Attr 10'],ax=axes[2, 0])
sns.violinplot(data=Quantitative['Attr 11'],ax=axes[2, 1])
sns.violinplot(data=Quantitative['Attr 12'],ax=axes[2, 2])

sns.pairplot(Quantitative).savefig('Quantitative.png')

print('covariance matrix: ')
Quantitative_cov=Quantitative.cov()
#print(Quantitative_cov)
print(tabulate(Quantitative_cov, headers='keys', tablefmt='psql'))

print('corelation matrix: ')
Quantitative_corr=Quantitative.corr()
#print(Quantitative_corr)
print(tabulate(Quantitative_corr, headers='keys', tablefmt='psql'))

a4_dims = (20, 30)
fig, axes = plt.subplots(2,figsize=a4_dims)

sns.heatmap(Quantitative_cov, annot=True, ax=axes[0])
sns.heatmap(Quantitative_corr, annot=True, ax=axes[1])