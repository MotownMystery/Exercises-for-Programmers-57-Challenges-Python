def isSymbol(name): 
    x = 0 
    symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
    for i in name:
        if i in symbol:
           x += 1
    if x > 0: return True
    if x == 0: return False 
    
def isNum(name):
    x = 0
    symbol = "1234567890"
    for i in name:
        if i in symbol:
           x += 1
    if x > 0: return True
    if x == 0: return False 
    
def isAlph(name):
    x = 0
    symbol = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    for i in name:
        if i in symbol:
           x += 1
    if x > 0: return True
    if x == 0: return False 
    
    
def Fnames(First): 
    BF = isAlph(First)
    if len(First) > 1 and BF: 
        return True 

def Lnames(Last): 
    BL = isAlph(Last)
    if len(Last) > 1 and BL: 
        return True 
       
def ZIP(Zip):
    if isNum(Zip):
        return True 

def EmpID(ID):
    if isAlph(ID[0:2]) and ID[2] == '-' and isNum(ID[3:5]):
        return True 

First = input("Please enter your first name? ")
Last = input("Please enter your last name? ")
Zip = input("Please enter your zip code? ")
ID = input("Please enter your ID? ")

if Fnames(First) != True: print(f"{First} is not a name. It is too short.")
if Lnames(Last) != True: print(f"{Last} is not a name. It is too short. ")
if ZIP(Zip) != True: print("The Zip is not a numeric number")
if EmpID(ID) != True: print(f"{ID} is not a valid ID")

    
    