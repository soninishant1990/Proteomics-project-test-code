#https://www.kaggle.com/kanncaa1/feature-selection-and-data-visualization

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # data visualization library  
import matplotlib.pyplot as plt
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
import time
from subprocess import check_output


data = pd.read_csv('Result_Mix3_LTQFT_Target_with_add_feature_for_cluster-1.csv')
protein = data['Protein']
#print(data.head())

# feature names as a list
col = data.columns       # .columns gives columns names in data 
#print(col)

# y includes our labels and x includes our features
y = data.Protein                          # M or B 
list = ['ID']
x = data.drop(list,axis = 1 )
#print(x.head())


ax = sns.countplot(y,label="Count")     
c, s, g = y.value_counts()
print('contaminant: ',c)
print('sp : ',s)
print('gi : ',g)
plt.show()

data2 = x.drop(['Protein'],axis = 1 )
data_dia = y
data1 = data2
data_n_2 = (data1 - data1.mean()) / (data1.std())              # standardization
print(data_n_2)
data = pd.concat([y,data_n_2.iloc[:,0:5]],axis=1)
data['Protein'] = protein
print(data)
data = pd.melt(data,id_vars="Protein",var_name="features",value_name='value')
plt.figure(figsize=(10,10))
#sns.violinplot(x="features", y="value", hue="Protein", data=data,split=True, inner="quart")
sns.boxplot(x="features", y="value", hue="Protein", data=data)
#plt.xticks(rotation=90)
plt.show()

data = pd.concat([y,data_n_2.iloc[:,5:10]],axis=1)
data['Protein'] = protein
print(data)
data = pd.melt(data,id_vars="Protein",var_name="features",value_name='value')
plt.figure(figsize=(10,10))
#sns.violinplot(x="features", y="value", hue="Protein", data=data,split=True, inner="quart")
sns.boxplot(x="features", y="value", hue="Protein", data=data)
#plt.xticks(rotation=90)
plt.show()

data = pd.concat([y,data_n_2.iloc[:,10:15]],axis=1)
data['Protein'] = protein
print(data)
data = pd.melt(data,id_vars="Protein",var_name="features",value_name='value')
plt.figure(figsize=(10,10))
#sns.violinplot(x="features", y="value", hue="Protein", data=data,split=True, inner="quart")
sns.boxplot(x="features", y="value", hue="Protein", data=data)
#plt.xticks(rotation=90)
plt.show()

data = pd.concat([y,data_n_2.iloc[:,15:20]],axis=1)
data['Protein'] = protein
print(data)
data = pd.melt(data,id_vars="Protein",var_name="features",value_name='value')
plt.figure(figsize=(10,10))
#sns.violinplot(x="features", y="value", hue="Protein", data=data,split=True, inner="quart")
sns.boxplot(x="features", y="value", hue="Protein", data=data)
#plt.xticks(rotation=90)
plt.show()

data = pd.concat([y,data_n_2.iloc[:,20:25]],axis=1)
data['Protein'] = protein
print(data)
data = pd.melt(data,id_vars="Protein",var_name="features",value_name='value')
plt.figure(figsize=(10,10))
#sns.violinplot(x="features", y="value", hue="Protein", data=data,split=True, inner="quart")
sns.boxplot(x="features", y="value", hue="Protein", data=data)
#plt.xticks(rotation=90)

plt.show()

data = pd.concat([y,data_n_2.iloc[:,25:30]],axis=1)
data['Protein'] = protein
print(data)
data = pd.melt(data,id_vars="Protein",var_name="features",value_name='value')
plt.figure(figsize=(10,10))
#sns.violinplot(x="features", y="value", hue="Protein", data=data,split=True, inner="quart")
sns.boxplot(x="features", y="value", hue="Protein", data=data)
#plt.xticks(rotation=90)
plt.show()

data = pd.concat([y,data_n_2.iloc[:,30:34]],axis=1)
data['Protein'] = protein
print(data)
data = pd.melt(data,id_vars="Protein",var_name="features",value_name='value')
plt.figure(figsize=(10,10))
#sns.violinplot(x="features", y="value", hue="Protein", data=data,split=True, inner="quart")
sns.boxplot(x="features", y="value", hue="Protein", data=data)
#plt.xticks(rotation=90)
plt.show()