import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm

# Read Excel file into DataFrame
df = pd.read_excel('s057.xls')

#Extract the 'Normally Distributed Housefly Wing Lengths' column and remove the first 4 values 
arr = df['Normally Distributed Housefly Wing Lengths'].values[4:]

# Calculate unique values and their count from data
values, dist =np.unique(arr, return_counts=True)
#plt.bar(values,dist)


# Estimation of Distribution Parameters

## Calculate mean and standard deviation of the data
mu = arr.mean()
sigma = arr.std()

# Generate x values from 30 to 60 with a step of 0.1
x = np.arange(30, 60, 0.1)

# Create a normal distribution object with the calculated mean and standard deviation
dist = norm(mu, sigma)

# Calculate de probability density function (pdf) for each x value
y=[dist.pdf(value) for value in x]

#Plot the probability density function
plt.plot(x, y, label='Normal Distribution Function (PDF)', color='red')

# Show the plot with labels and legend
plt.xlabel('Values')
plt.ylabel('Frequency/Probability')
values, dist = np.unique(arr, return_counts=True)
plt.bar(values, dist/len(arr))
plt.show()