import pandas as pd
data = pd.read_csv('Result_Mix3_LTQFT_Target_with_add_feature.csv')
#print(data)
d = data.dropna()
#data.dropna().to_csv('Result_Mix3_LTQFT_Target_with_add_feature_remove_colume+row.csv')
print(d)
