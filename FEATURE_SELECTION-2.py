#https://www.kaggle.com/kanncaa1/feature-selection-and-data-visualization

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # data visualization library  
import matplotlib.pyplot as plt
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
import time
from subprocess import check_output


data = pd.read_csv('Result_Mix3_LTQFT_Target_with_add_feature.csv')

protein = data['PSM']
#print(data.head())

# feature names as a list
col = data.columns       # .columns gives columns names in data 
#print(col)

# y includes our labels and x includes our features
y = data.PSM                          # M or B 
list = ['ID']

x = data.drop(list,axis = 1 )
#print(x.head())


ax = sns.countplot(y,label="Count")     
P, F = y.value_counts()
print('Pass PSM: ',P)
print('Fail PSM: ',F)
plt.show()

data2 = x.drop(['PSM'],axis = 1 )
data_dia = y
data1 = data2
#data_n_2 = (data1 - data1.mean()) / (data1.std())              # standardization
data_n_2 = data1
print(data_n_2)


e = int('0')
colums = 0
colums1 = len(data.columns)
print(colums1)
try:
	while colums  <= colums1:
		data = pd.concat([y,data_n_2.iloc[:,e]],axis=1)
		data['PSM'] = protein
		print(data)
		data = pd.melt(data,id_vars="PSM",var_name="features",value_name='value')
		plt.figure(figsize=(10,10))
		#sns.violinplot(x="features", y="value", hue="PSM", data=data,split=True, inner="quart")
		sns.violinplot(x="features", y="value", hue="PSM", data=data, inner="quart")
		#plt.xticks(rotation=90)
		colums+=1
		e+=1
		#plt.show()
except IndexError:
	pass


#correlation map
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(x.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score,confusion_matrix
from sklearn.metrics import accuracy_score

# split data train 70 % and test 30 %
data2 = x.drop(['PSM'],axis = 1 )

x_train, x_test, y_train, y_test = train_test_split(data2, y, test_size=0.3, random_state=42)


from sklearn.ensemble import RandomForestClassifier
clf_rf = RandomForestClassifier(random_state=43)      
clr_rf = clf_rf.fit(x_train,y_train)
from sklearn.feature_selection import RFECV
clf_rf_5 = RandomForestClassifier()      
clr_rf_5 = clf_rf_5.fit(x_train,y_train)
importances = clr_rf_5.feature_importances_
std = np.std([tree.feature_importances_ for tree in clf_rf.estimators_], axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")
feature_rank = []
for f in range(x_train.shape[1]):
	feature_rank.append("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))
	print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))


plt.figure(1, figsize=(14, 13))
plt.title("Feature importances")
plt.bar(range(x_train.shape[1]), importances[indices],
       color="g", yerr=std[indices], align="center")
plt.xticks(range(x_train.shape[1]), x_train.columns[indices],rotation=70)#
plt.xlim([-1, x_train.shape[1]])
plt.show()