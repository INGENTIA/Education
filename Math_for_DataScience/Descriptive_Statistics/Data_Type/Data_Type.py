import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# Read de CSV file into a DataFrame
df = pd.read_csv('cars.csv')

# Calculate the Mean and Medan of 'price_usd'
df['price_usd'].mean()
df['price_usd'].median()

# Create a Histogram Plot
df['price_usd'].plot.hist(bins=20)

sns.displot(df, x = 'price_usd', hue = ' manufacturer_name')

plt.show()