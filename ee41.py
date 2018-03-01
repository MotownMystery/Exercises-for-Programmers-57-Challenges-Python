def getKey(item):
    return item[0]

filename = 'ee41.txt'
txt = open(filename)


content = txt.readlines()
content = [x.strip() for x in content] 

Map = sorted(content, key=getKey)

print("Total number of names: ", len(Map))
for i in Map:
    print(i)