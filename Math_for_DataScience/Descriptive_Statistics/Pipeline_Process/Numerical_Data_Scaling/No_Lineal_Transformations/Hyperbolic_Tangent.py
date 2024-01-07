import timeit
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

df = pd.read_csv('cars.csv')

df.price_usd.hist()

p = 10000
df.price_usd.apply(lambda x : np.tanh(x/p))



plt.show()
