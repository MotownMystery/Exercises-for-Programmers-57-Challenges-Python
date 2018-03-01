path = 'http://api.open-notify.org/astros.json'
from tabulate import tabulate
import requests
r = requests.get(url=path)
data = r.json()


table = [] 
for i in range(0,data['number']):
    table.append([data['people'][i]['name'], data['people'][i]['craft']])

table.sort()

print('\nNumber of people in space are: ', data['number'])
print(tabulate(table, headers=['Name','Craft']))
