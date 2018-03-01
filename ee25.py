

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
   
PS = input("Enter your passowrd > ")    

if isAlph(PS) == False and isNum(PS) == True and isSymbol(PS) == False and len(PS) < 8:
    print('Very Weak Password')
elif isAlph(PS) == True and isNum(PS) == False and isSymbol(PS) == False and len(PS) >= 8:
    print('Weak Password')
elif isAlph(PS) == True and isNum(PS) == True and isSymbol(PS) == False and len(PS) >= 8:
    print('Strong Password')
elif isAlph(PS) == True and isNum(PS) == True and isSymbol(PS) == True and len(PS) >= 8:
    print('Very Strong Password')    
elif isAlph(PS) == True and isSymbol(PS) == False and len(PS) < 8:
    print('Weak Password')
else:
    pass
