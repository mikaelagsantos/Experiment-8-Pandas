import pandas as pd
df = pd.read_csv('cars.csv')

#problem 2.a
df2 = df[df.index % 2 == 1]
print ('\n First five rows with odd-numbered columns: \n', df2[:5])

#problem 2.b
df3 = df.loc[df.Model == 'Mazda RX4']
print ('\n The row that contains the Model of Mazda RX4: \n', df3)


#problem 2.c
df4 = df.loc[(df.Model == 'Camaro Z28', ['cyl'])]
print(df4)


#problem 2.d
print (df.loc[df['Model'] == 'Camaro Z28', ['Model', 'cyl', 'gear']])
print (df.loc[df['Model'] == 'Ford Pantera L', ['Model', 'cyl', 'gear']])
print (df.loc[df['Model'] == 'Honda Civic', ['Model', 'cyl', 'gear']])





