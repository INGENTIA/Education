import numpy as np
from matplotlib import pyplot
from numpy.random import normal
from scipy.stats import norm

#sample = normal() # generator
#print(sample)
#pyplot.hist(sample, bins=30)
#pyplot.show()


#Parametric Estimation

# Generate a sample of 1000 data points from a normal distribution
# with a specified mean (mu) of 50 and a standard deviation (sigma) of 5.
sample =  normal(loc=50, scale= 5, size=1000) #mu= 50 , sigma =5 

# Calculate the sample mean and standard deviation. 
mu = sample.mean()
sigma = sample.std()

# Create a normal distribution object using the calculated mean and standard deviation
dist = norm(mu, sigma)

# Define a range of values for which to calculate the probability density function (pdf)
values = [value for value in range(30, 70)]

# Calculate the probability density function (pdf) for each value in the range 
probabilities = [dist.pdf(value) for value in values]

# Histograma de Muestra de Datos Experimentales
pyplot.hist(sample, bins = 30, density=True)

# Funcion Teorica
pyplot.plot(values, probabilities)

pyplot.show()

