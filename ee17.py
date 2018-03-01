gen = {'men' : 0.73, 'women' : 0.66}

A = 12*float(input("How many drinks have you had? "))*.06
r = gen[input(str("What is your gender? "))]
w = float(input("What is your body weight?" )) 
H = float(input("How many hours has it been since your last drink? "))

BAC = round(A*(5.14/w)*r-(.015*H),2)

print(f"Your BAC is {BAC}")

if BAC > .08: print("It is not legal for you to drive ")
else: print("It is legal for you to drive ")



