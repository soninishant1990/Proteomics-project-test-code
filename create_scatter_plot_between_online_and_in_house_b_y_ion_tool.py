import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import re
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score

d = pd.read_csv('comparision_online and_in_house_developed_tool_fro_b_y_ion1.csv')
OT = d['online tool']
IHT = d['in house tool']

rms1 = sqrt(mean_squared_error(OT,IHT))
print(rms1)

R2 = r2_score(OT,IHT)
print(R2)

d = pd.read_csv('comparision_online and_in_house_developed_tool_fro_b_y_ion.csv')
OT = d['online tool']
IHT = d['in house tool']


plt.scatter(OT, IHT, alpha=0.5, cmap='viridis')
plt.plot(OT,IHT,c='r')

plt.xlabel("online tool m/z")
plt.ylabel("in house tool m/z")

plt.title('online and in house b y ion calculator comparision')
plt.show()










import pandas as pd
import matplotlib.pyplot as plt
#loading dataset
df = pd.read_csv('comparision_online and_in_house_developed_tool_fro_b_y_ion1.csv')
df.columns = ['online tool','in house tool']
def scatterplot(df, x_dim, y_dim):
  x = df[x_dim]
  y = df[y_dim]
  fig, ax = plt.subplots(figsize=(10, 5))
  #customizes alpha for each dot in the scatter plot
  ax.scatter(x, y, alpha=0.70)
 
  #adds a title and axes labels
  ax.set_title('online tool vs in house tool')
  ax.set_xlabel('online tool')
  ax.set_ylabel('in house tool')
 
  #removing top and right borders
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  #adds major gridlines
  ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
  plt.show()
scatterplot(df,'online tool', 'in house tool')



