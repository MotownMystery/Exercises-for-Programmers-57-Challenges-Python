import json
data = json.load(open("ee56.json"))

while True: 
    try: 
        name = input("Enter name: ")
        SN = input("Enter serial number: ")
        Val = input("Enter the value: ")
        new_data = {"name":name,"serial number":SN,"value":int(Val)}
        data["inventory"].append(new_data)
        if name == '' or SN == '' or Val == '':
            break 
    except ValueError:
        break 

print("Lets search for an item now! ")
names = []
for x in range(0,len(data)+1):
    names.append(data['inventory'][x]["name"]) 
item = input("Name the item: ")
id = names.index(item)


    
print(data['inventory'][id]['value'])

import codecs
with codecs.open('ee56.json', 'w', 'utf8') as f:
     f.write(json.dumps(data, sort_keys = True, ensure_ascii=False))