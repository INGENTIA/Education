import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris =  sns.load_dataset('iris')

# ScatterPlot
sns.scatterplot(data=iris, x = 'sepal_length', y = 'petal_length', hue = 'species')

# joint plot
sns.jointplot(data=iris, x = 'sepal_length', y = 'petal_length')

plt.show()