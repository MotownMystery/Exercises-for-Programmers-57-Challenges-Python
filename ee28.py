
num = int(input("How many numbers would you like to add? "))
X = 0
for i in range(0,num):
    while True:
        try: 
            x = float(input("Enter a number? "))
            break
        except ValueError:
            pass 
    X = X + x
print(f"The total is: {X}")

    