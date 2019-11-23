import pandas as pd
df = pd.read_csv('cars.csv')
print ('\n First five rows of resulting cars \n', df.head())
print ('\n Last five rows of resulting cars \n', df.tail())