import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm

###Theorical
def gaussian ( x, mu, sigma):
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*pow((x-mu)/sigma,2))

x = np.arange(-4, 4, 0.1)
y = gaussian(x, 0.0, 1.0)

plt.plot(x, y)



###Simulation
dist = norm(0, 1)
x = np.arange(-4, 4, 0.1)
y = [dist.pdf(value) for value in x]
plt.plot(x, y)


###Acumulative
dist = norm(0, 1)
x = np.arange(-4, 4, 0.1)
y= [dist.cdf(value) for value in x]
plt.plot(x,y)


plt.show()
