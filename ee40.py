txt = "ee39_data.txt"

with open(txt) as f:
    content = f.readlines()
content = [x.strip() for x in content] 

Map = []
for i in range(0,len(content)):
     List = content[i].split(' ')
     try: 
         Data = (List[0], List[1], List[2] , List[3])
     except IndexError: 
         Data = (List[0], List[1], List[2])
     Map.append(Data)

key = input("Enter a key word? ")

for i in range(0,len(Map)):
    match, match2 = False, False 
    name = str(Map[i][0])
    name2 = str(Map[i][1])
    match = key in name[0:len(key)] 
    match2 = key in name2[0:len(key)] 
    if match == match2: 
        if match == True: print(Map[i])   
    if match != match2:
        if match == True: print(Map[i])
        if match2 == True: print(Map[i]) 
        

import pandas 
import MySQLdb


