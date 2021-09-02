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


d4 = pd.read_csv('combined_csv.csv')

plt.figure(figsize=(10,5))
sns.set_context("paper", rc={"axes.labelsize":35, 'xtick.labelsize':35,'ytick.labelsize':35})
ax = sns.boxplot(x="data", y='r_value_square', data=d4, hue='Tools', palette="Set3", width=.50) #, labels=['ms2pip_PXD009369','pDeep_PXD009369','deepmassprism_PXD009369','ms2pip_PXD010260','pDeep_PXD010260','deepmassprism_PXD010260','ms2pip_PXD010762','pDeep_PXD010762','deepmassprism_PXD010762','ms2pip_PXD011545','pDeep_PXD011545','ms2pip_PXD012548','pDeep_PXD012548','deepmassprism_PXD012548'])
plt.tight_layout()
ax.legend(fontsize=0.0001, ncol=4)
sns.despine(offset=10, trim=True)
plt.ylim(0,1.16)
plt.title('HCD Fragmentation Instruments', fontname='Arial', fontsize=40)
plt.xlabel("Instrument type", fontname='Calibri', fontsize=40)
plt.ylabel("r square", fontname='Calibri', fontsize=40)

plt.savefig('boxplot.png', dpi=600,bbox_inches='tight', pad_inches=0.1, orientation='landscape')

plt.show()
