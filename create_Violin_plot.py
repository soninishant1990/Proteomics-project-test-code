import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import re
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score
from scipy import stats
import seaborn as sns
from matplotlib import pyplot
import matplotlib.pyplot as plt

d1 = pd.read_csv('ms2pip_PXD000421.csv')
d2 = pd.read_csv('ms2pip_PXD003651.csv')
d3 = pd.read_csv('ms2pip_PXD004798.csv')
d4 = pd.read_csv('ms2pip_PXD009369.csv')
d5 = pd.read_csv('ms2pip_PXD010260.csv')
d6 = pd.read_csv('ms2pip_PXD010762.csv')
d7 = pd.read_csv('ms2pip_PXD011545.csv')
d8 = pd.read_csv('ms2pip_PXD012548.csv')
d9 = pd.read_csv('pDeep_PXD000421.csv')
d10 = pd.read_csv('pDeep_PXD003651.csv')
d11 = pd.read_csv('pDeep_PXD004798.csv')
d12 = pd.read_csv('pDeep_PXD009369.csv')
d13 = pd.read_csv('pDeep_PXD010260.csv')
d14 = pd.read_csv('pDeep_PXD010762.csv')
d15 = pd.read_csv('pDeep_PXD011545.csv')
d16 = pd.read_csv('pDeep_PXD012548.csv')
d17 = pd.read_csv('PeptideART_PXD003651.csv')
d18 = pd.read_csv('PeptideART_PXD004798.csv')
d19 = pd.read_csv('PeptideART_PXD000421.csv')


#pDeep = d['r_value_square']
ms2pip_PXD000421 = d1['r_value_square']
ms2pip_PXD003651= d2['r_value_square']
ms2pip_PXD004798= d3['r_value_square']
ms2pip_PXD009369= d4['r_value_square']
ms2pip_PXD010260= d5['r_value_square']
ms2pip_PXD010762= d6['r_value_square']
ms2pip_PXD011545= d7['r_value_square']
ms2pip_PXD012548= d8['r_value_square']
pDeep_PXD000421= d9['r_value_square']
pDeep_PXD003651= d10['r_value_square']
pDeep_PXD004798= d11['r_value_square']
pDeep_PXD009369= d12['r_value_square']
pDeep_PXD010260= d13['r_value_square']
pDeep_PXD010762= d14['r_value_square']
pDeep_PXD011545= d15['r_value_square']
pDeep_PXD012548= d16['r_value_square']
PeptideART_PXD003651= d17['r_value_square']
PeptideART_PXD004798= d18['r_value_square']
PeptideART_PXD000421= d19['r_value_square']

data = [ms2pip_PXD000421,pDeep_PXD000421,PeptideART_PXD000421,ms2pip_PXD003651,pDeep_PXD003651,PeptideART_PXD003651,ms2pip_PXD004798,pDeep_PXD004798,PeptideART_PXD004798,ms2pip_PXD009369,pDeep_PXD009369,ms2pip_PXD010260,pDeep_PXD010260,ms2pip_PXD010762,pDeep_PXD010762,ms2pip_PXD011545,pDeep_PXD011545,ms2pip_PXD012548,pDeep_PXD012548]#,MS2PIP,deepmass_prism,peptide_ART]
#ms2pip_PXD010260,pDeep_PXD010260,ms2pip_PXD010762,pDeep_PXD010762,ms2pip_PXD011545,pDeep_PXD011545,ms2pip_PXD012548,pDeep_PXD012548


#fig, ax = pyplot.subplots(figsize =(9, 7)) 
#ax = sns.violinplot(x='Intrument_type',y='r_square',hue="comparision",data = data) #, x = 'r_square', y = 'Intrument type')
ax = sns.violinplot(data = data) #, x = 'r_square', y = 'Intrument type')
ax.set_xticklabels(['ms2pip_PXD000421','pDeep_PXD000421','PeptideART_PXD000421','ms2pip_PXD003651','pDeep_PXD003651','PeptideART_PXD003651','ms2pip_PXD004798','pDeep_PXD004798','PeptideART_PXD004798','ms2pip_PXD009369','pDeep_PXD009369','ms2pip_PXD010260','pDeep_PXD010260','ms2pip_PXD010762','pDeep_PXD010762','ms2pip_PXD011545','pDeep_PXD011545','ms2pip_PXD012548','pDeep_PXD012548'], rotation=20)

#print(data)
#plt.boxplot(data,labels=['pDeep'])
#violinplot(data)

#plt.xlabel("pdeep_PXD010762")
#plt.ylabel("r_square")
plt.xlabel("Intrument type")
plt.ylabel("r_square")
plt.savefig('violin.png', dpi=1200)
plt.show()
