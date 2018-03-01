
from babel.numbers import format_currency
#File = open("ee42.txt")
#import csv 
#Reader = csv.reader(File)
#Data = list(Reader)
#
#print("Last    Frist    Salary\n-----------------")
#for i in range(0,6):
#        print(Data[i][0] + " " + Data[i][1] + " " + Data[i][2])
with open("ee42.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
Data = [x.split(',') for x in content] 

print("Last    Frist    Salary\n-----------------")
for i in range(0,6):
        print(Data[i][0] + " " + Data[i][1] + " " + format_currency(Data[i][2], 'USD', locale='en_US'))
