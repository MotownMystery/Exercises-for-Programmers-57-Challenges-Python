import random as r

Num = r.randint(1,4)
L = {1 : "Yes", 2 : "No", 3 : "Maybe", 4 : "Ask again later"}

Ans = L[Num] 
Q = input("What is your question? ")
print(Ans)

