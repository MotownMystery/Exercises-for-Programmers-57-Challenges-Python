import random as r

print("Let's play a guessing game! ")
level = float(input("What level of difficulty (1,2 or 3)? "))

L = {1 : 10, 2 : 100, 3 : 1000}
count = 0 
Num = r.randint(1,L[level])
List = []
while True: 
    while True: 
        try: 
            G = float(input(f"Guess a number from 1 to {L[level]}? "))
            List.append(G)
            match = G in List
            if match == True: 
                print(f"You have already done {G}")
                break 
        except ValueError: 
            print("Error")
        
    count += 1
    if G == Num: break
    elif G > Num: print(f"Number less than {G}")  
    elif G < Num: print(f"Number greater than {G}")
    else: pass
    
print(f"Correct! The number was {Num}. It took you {count} ties")
if count == 0: print("Mind reader!")
if count >= 2 and count <= 4: print("Impressive guess")
if count >= 3 and count <= 6: print("You can do better")
if count >= 7: print("Better luck next time!")


