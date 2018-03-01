
rHR = float(input("Resting heart rate? "))
age = float(input("Age? "))

Rate = [] 
print("Intensity  --- Rate")
for i in range(55, 96): 
    Rate = round((((220-age)-rHR)*i/100) + rHR)
    print(f"{i}%   | {Rate} bpm")
    
    
