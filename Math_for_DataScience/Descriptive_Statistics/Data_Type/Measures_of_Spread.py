import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =  pd.read_csv('cars.csv')

# Standard Deviation
df['price_usd'].std()

# Range = max value - min value
range = df['price_usd'].max() -df['price_usd'].min()

# Quartiles
median = df['price_usd'].median()
Q1= df['price_usd'].quantile(q=0.25)
Q3 = df['price_usd'].quantile(q=0.75)
min_val = df['price_usd'].quantile(q=0)
max_val = df['price_usd'].quantile(q=1.0)
print(min_val, Q1, Q3, max_val)

#IQR
iqr = Q3 - Q1

# Limites de Detección de los outliers (datos simetricamente distribuidos)

minlimit = Q1 - 1.5*iqr
maxlimit = Q3 + 1.5*iqr

# Boxplot
sns.boxplot(x = 'engine_fuel', y = 'price_usd', data = df)

plt.show()