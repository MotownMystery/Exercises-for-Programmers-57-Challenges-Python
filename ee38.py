
def FilterEvenNumbers(Array):
    Even = []
    for i in Array:
        if i%2 == 0: 
            Even.append(i)
    return Even

IN = input('Enter of File? ')

if IN == 'Enter':
    Num = input("Enter a list of numbers, separated by spaces: ")
    List = Num.split()
if IN == 'File':
    file = input('Enter file name: ')
    Num = open(file)
    List = Num.read().split(' ')
    

Array = [float(i) for i in List]

print("The even numbers are: ", FilterEvenNumbers(Array))