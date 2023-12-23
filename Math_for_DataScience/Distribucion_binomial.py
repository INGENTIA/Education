import numpy as np 
from numpy.random import binomial
from scipy.stats import binom
from math import factorial
import matplotlib.pyplot as plt

def my_binomial(k, n, p) :
    return factorial(n)/(factorial(k)*factorial(n-k))*pow(p, k)*pow(1-p, n-k)

b1 = my_binomial(2, 3, 0.5)
dist = binom(3, 0.5)
#Probability Mass Function [pmf]
b2 = dist.pmf(2)
#print(b1)
#print(b2)

#Cumulative density function
b3 = dist.cdf(2)
#print(b3)

#Generadores aleatorios
p = 0.5
n = 3
b4 = binomial(n,p)
#print(b4)

#Many 
arr = []
for _ in range (100):
    arr.append(binomial(n,p))

#print(arr)

values = [0, 1, 2, 3]
theoric = [binom(3,0.5).pmf(k) for k in values ] 
result = np.unique(arr, return_counts=True)

#This calculates the relative frequency of each unique element in the array. It does so by dividing the count of each unique element by the total number of elements in the array.
sim = np.unique(arr,return_counts=True)[1]/len(arr)
#print(sim)


theoric = [binom(3,0.5).pmf(k) for k in values ] 

def plot_hist(num_trials):
    values = [0, 1, 2, 3]
    arr = []
    for _ in range(num_trials):
        arr.append(binomial(n,p))
    sim = np.unique(arr,return_counts=True)[1]/len(arr)
    theoric = [binom(3,0.5).pmf(k) for k in values ] 
    plt.bar(values, sim, color = 'red')
    plt.bar(values, theoric, alpha= 0.5, color = 'blue')
    plt.title('{} experimentos'.format(num_trials))
    plt.show()

plot_hist(20000)
