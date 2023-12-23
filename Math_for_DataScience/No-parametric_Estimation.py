import numpy as np
from matplotlib import pyplot
from numpy.random import normal
from scipy.stats import norm
from numpy import hstack
from sklearn.neighbors import KernelDensity

# Generate two normal distributions and combine the into a simple sample
sample1 = normal(loc=20, scale=5, size=300)
sample2 = normal(loc=40, scale=5, size=700)
sample = hstack((sample1,sample2))

# Create a Kernel Density Estimation (KDE) model
model = KernelDensity(bandwidth=2, kernel='gaussian')

# Reshape the sample for compatibility with the KDE model
sample = sample.reshape((len(sample),1))

# Fit the KDE model to the sample data
model.fit(sample)

# Generate value for which we want to estimate the probability density
values = np.asarray([value for value in range (1, 60)])
values = values.reshape((len(values),1))

# Calculate the log likelihood of each value using the KDE model
# and convert it to probabilities by exponentiating the log likelihood
probabilities =  model.score_samples(values) 
probabilities = np.exp(probabilities)

# Plot the histogram of the sample and the KDE estimate
pyplot.hist(sample, bins=50, density=True)
pyplot.plot(values, probabilities)
pyplot.legend()
pyplot.xlabel('Value')
pyplot.ylabel('Probability Density')
pyplot.title('Kernel Density Estimation')
pyplot.show()
