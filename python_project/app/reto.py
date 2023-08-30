import read_csv

data = read_csv.read_csv('./app/data.csv')

Population = list(filter(lambda x : x.keys(),data ))

#print(data)
print(Population[0])

'''

