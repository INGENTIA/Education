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
max_raw = max(raw)
min_raw = min(raw)
MinMaxScaled = (2*raw - max_raw -min_raw)/(max_raw - min_raw)

# Plot histogram of the min-max scaled data
axs[1].hist(MinMaxScaled)
axs[1].set_title('Min-Max Scaled Data') # Set subplot title

# Train linear regression model using raw data
def train_raw():
    linear_model.LinearRegression().fit(raw, y)

# train linear regression model using min-max scaled data 
def train_MinMax_Scaled():
    linear_model.LinearRegression().fit(MinMaxScaled,y)

# Measure the time taken to train the model with raw data
raw_time = timeit.timeit(train_raw, number=100)

# Measure the time taken to train the model with min-max scaled data
MinMaxScaled_time = timeit.timeit(train_MinMax_Scaled, number=100)

# Print the results
print('Train Waw: {}'.format(raw_time))
print('Train Min-Max Scaled: {}'.format(MinMaxScaled_time))

# Display the plots
plt.show()
