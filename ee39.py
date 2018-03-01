def getKey(item):
    return item[2]

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

New_Map = sorted(Map, key=getKey)


for row in New_Map:                     
        if len(row) == 4:
            print(row[0] + " " + row[1] + "  " + row[2] + "  " + row[3])
        if len(row) == 3:
            print(row[0] + "  " + row[1] + "  " + row[2])
       
    
    