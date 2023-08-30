import charts
import read_csv
import utils
import pandas as pd

def run():

  df = pd.read_csv('data.csv')
  df = df[df['Continent']== 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('./data.csv')
  country  = input('Type Country => ')
  
  result =utils.population_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels,values)
    charts.generate_pie_chart(labels,values)

if __name__ == '__main__':
  run()

'''
def run1():

  data = read_csv.read_csv('./app/data.csv')
  print(data[0])
  data = list(filter(lambda item: item['Continent'] == 'Asia',data))
  
  labels = list(map(lambda item : item['CCA3'], data))
  values= list(map(lambda item : item['World Population Percentage']  , data))
 
  

  

if __name__ == '__main__':
  run()
  run()
'''