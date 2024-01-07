import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# Read de CSV file into a DataFrame
df = pd.read_csv('cars.csv')

# Calculate the Mean and Medan of 'price_usd'
df['price_usd'].mean()
df['price_usd'].median()

# Create a Histogram Plot
#df['price_usd'].plot.hist(bins=20)

sns.displot(df, x = 'price_usd', hue = 'manufacturer_name')
sns.displot(df, x = 'price_usd', hue = 'engine_type', multiple = 'stack')

df.groupby('engine_type').count()

# Filter the DataFrame to include only rows where the manufacturer is 'Audi' and the model is 'Q7'
Q7_df = df[(df['manufacturer_name'] == 'Audi') & (df['model_name']== 'Q7')]

# Create a histogram plot using Seaborn
sns.histplot(Q7_df, x='price_usd', hue='year_produced')

plt.show()