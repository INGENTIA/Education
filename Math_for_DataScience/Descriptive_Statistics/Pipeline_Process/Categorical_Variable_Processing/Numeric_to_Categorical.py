import pandas as pd 
import matplotlib.pyplot as pyplot
import sklearn.preprocessing as preprocessing

df = pd.read_csv('cars.csv')
encoder = preprocessing.OneHotEncoder(handle_unknown='ignore')
encoder.fit(df[['year_produced']].values)

lt = encoder.transform([[2016], [2009], [1990]]).toarray()

print(lt)
