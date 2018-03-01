
def Cel_Feh(x):
    F = (x*9.5)+32
    return F

def Feh_Cel(x):
    C = (x-32)*(5/9)
    return C

print("""
Press C to convert fahrenheit to Celsius 
Press F to convert Celsius to Farrenheit
""")

SI = input("Your choice? ")
Units = {'F' : 'Fahrenheit', 'C' : 'Celsius'}
Unit = {'F' : 'Celsius', 'C' : 'Fahrenheit'}
while True:
    try: 
        Temp = float(input(f"Please enter the temp in {Unit[SI]} "))
        break
    except ValueError:
        print('Error')

if SI == 'C': print(f"The temp in {Units[SI]} is ", str(Feh_Cel(Temp)))
if SI == 'F': print(f"The temp in {Units[SI]} is ", str(Cel_Feh(Temp)))

