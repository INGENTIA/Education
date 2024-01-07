import timeit
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

# Load the diabetes dataset and extract a specific feature (column 2)
X, y = datasets.load_diabetes(return_X_y= True)
raw = X[:, None, 2]

# Create subplots for raw and scaled histograms
fig, axs = plt.subplots(2, 1, sharex= True)

#Plot histogram of the raw data
axs[0].hist(raw)
axs[0].set_title('Raw Data') # Set subplot title


# Z-score Normalization
avg = np.average(raw)
std = np.std(raw)
z_scaled = (raw - avg)/std

# Plot histogram of the min-max scaled data
axs[1].hist(z_scaled)
axs[1].set_title('Z-Score Normalization') # Set subplot title

# Train linear regression model using raw data
def train_raw():
    linear_model.LinearRegression().fit(raw, y)

# train linear regression model using min-max scaled data 
def train_ZScore():
    linear_model.LinearRegression().fit(z_scaled,y)

# Measure the time taken to train the model with raw data
raw_time = timeit.timeit(train_raw, number=100)

# Measure the time taken to train the model with min-max scaled data
ZScore_time = timeit.timeit(train_ZScore, number=100)

# Print the results
print('Train Waw: {}'.format(raw_time))
print('Train Z-Score: {}'.format(ZScore_time))

# Display the plots
plt.show()
