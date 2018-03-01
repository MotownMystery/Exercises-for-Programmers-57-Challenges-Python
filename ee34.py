
txt = open('names.txt')
List = txt.read().split('\n')

while True:
    try: 
        print(f"There are {len(List)} employees: ")
        for i in range(0,len(List)):
            print(List[i])
        R = input("Enter the name to remove: ")
        List.remove(R)
        break
    except ValueError:
        print('Error')
    

for i in range(0,len(List)):
    print(List[i])

