import random as r

N, List = [], []
while True:
    if N != '': 
        N = input("Enter a name? ")
        List.append(N)
    if N == '':
        List.remove(N)
        break

Winner = r.randint(0,len(List))
print(f"The 1st winner is {List[Winner]}")
del List[Winner]
Winner = r.randint(0,len(List))
print(f"The 2nd winner is {List[Winner]}")

