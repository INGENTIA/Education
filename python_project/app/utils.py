def get_population(country_dic):
  population_dict = {
    '2022': int(country_dic['2022 Population']),
    '2020': int(country_dic['2020 Population']),
    '2015': int(country_dic['2015 Population']),
    '2010': int(country_dic['2010 Population']),
    '2000': int(country_dic['2000 Population']),
    '1990': int(country_dic['1990 Population']),
    '1980': int(country_dic['1980 Population']),
    '1970': int(country_dic['1970 Population'])
    
  }

  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values


def population_by_country(data, country):
  result = list(filter(lambda item : item['Country/Territory'] == country, data))
  print(result)
  print(result[0])
  return result 


def world_pop(data):
  labels = list(map(lambda item : item['Country/Territory'], data))
  values= list(map(lambda item : item['World Population Percentage']  , data))
 
  
  return labels, values

