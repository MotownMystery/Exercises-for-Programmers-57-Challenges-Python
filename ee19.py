## Body mass index

w = float(input("What is your weight in lbs? "))
h = input("What is your height? feet-inch "); data = h.split("-")
H = float(data[0])*12+float(data[1])
bmi = round((w/(H**2))*703,2)

print(f"You BMI is: {bmi}")
if bmi > 25 and bmi < 18: print("You're not healthy")
else: print("You're good")