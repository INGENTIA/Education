import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris =  sns.load_dataset('iris')

# joint plot
#sns.jointplot(data=iris, x = 'sepal_length', y = 'petal_length')

sns.jointplot(data=iris, x = 'sepal_length', y = 'petal_length', hue='species')
plt.show()