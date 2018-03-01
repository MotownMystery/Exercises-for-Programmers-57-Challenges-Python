import math as m 

def Mean(List):
    return sum(List)/len(List)
def Min(List):
    min = List[0]
    for i in range(0, len(List)):
        if List[i]< min: min = List[i]
    return min
def Max(List):
    max = List[0]
    for i in range(0, len(List)):
        if List[i]> max: max = List[i]
    return max
def STD(List):
    mean = Mean(List)
    for i in range(0, len(List)):
        List[i] = (List[i] - mean)**2
    return round(m.sqrt(Mean(List)),2)
        
access = input("Is it from a file? Yes or No")    

if access == 'No':
    X = []
    List = []
    while True: 
        X = input("Enter a number: ")
        if X != 'done':
            List.append(X)
        if X == 'done':
            break
if access == 'Yes':
    filename = input("Enter the filename: ")
    txt = open(filename)
    List = txt.read().split('\n')

List = [float(i) for i in List]

print(f"Numbers: {List}")
print("Mean: " + str(Mean(List)))
print("Min: " + str(Min(List)))
print("Min: " + str(Max(List)))
print("STD: " + str(STD(List)))
