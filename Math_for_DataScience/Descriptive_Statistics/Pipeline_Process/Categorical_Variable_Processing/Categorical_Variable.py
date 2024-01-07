import pandas as pd 
import matplotlib.pyplot as pyplot
import sklearn.preprocessing as preprocessing

# Read the CSV file into a DataFrame
df = pd.read_csv('cars.csv')

# Use get_dummies to create one-hot encoded columns
one_hot_encoded = pd.get_dummies(df['engine_type'])

encoder = preprocessing.OneHotEncoder(handle_unknown='ignore')
encoder.fit(df[['engine_type']].values)

lt =encoder.transform([['gasoline'],['diesel'],['aceite']]).toarray()
print(lt)