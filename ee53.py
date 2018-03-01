## To Do List App

def add_task(list):
    task = []
    while True: 
        if task != '':
            task = input("Enter a Task: ")
            list.append(task)
        else: 
            del list[-1] 
            return list
        
def del_task(list):         
    task = []
    while True: 
        task = input("Enter a Taskm to remove: ")
        if task != '':
            id = list.index(task)
            del list[id]   
        else:  
            return list

filename = "ee53.txt"
data  = open(filename).read()
list = data.split()

while True: 
    switch = input("Enter the ask you would like to do (Add, Remove, Print or Exit): ")
    if switch.lower() == 'add':
        list = add_task(list)
    if switch.lower() == 'remove':
        list = del_task(list)
    if switch.lower() == 'print':
        print('Task: ')
        for i in list:
            print(i)
    if switch.lower() == 'exit':
        print("Shutting down...")
        break
    else:
        pass
    
str1 = ' '.join(list)

data = open(filename,'w')
data.write(str1)
data.close()