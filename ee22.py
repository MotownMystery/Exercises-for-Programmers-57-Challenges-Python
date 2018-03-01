
def Max(X):
    Max = 0
    for i in range(0, len(X)):
        if X[i] > Max: Max = X[i]
    return Max

Num = input("Enter numbers? # # # #")
list = Num.split(" ")
XX = [float(x) for x in list]

print(Max(XX))

    
