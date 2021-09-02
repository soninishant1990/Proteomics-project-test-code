import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import re


d = pd.read_csv('graph_denovascore.csv')
msgfscore63 = d['63MSGF_DeNovoScore']
legend = ['63MSGF_DeNovoScore', '17MSGF_DeNovoScore']
msgfscore17 = d['17MSGF_DeNovoScore']


plt.hist([msgfscore63, msgfscore17], color=['orange', 'green'], bins=20, normed=True)
plt.xlabel("score")
plt.ylabel("Frequency")
plt.legend(legend)
#plt.xticks(range(-90, 250))
#plt.yticks(range(1, 20000))
plt.title('score_frequency')
plt.show()