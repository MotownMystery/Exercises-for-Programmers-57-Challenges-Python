import random as r 
def RLetters(L):
    char = "qwertyuiopasdfghjklzxcvbnm"
    List = []
    for i in range(0,L):
        RandC = char[r.randint(0,25)]
        List.append(RandC)
    return List

def RSChar(List,SC,L):
     char = "~!@#$%^&*?><"
     ID = []
     i = 0 
     while i <= (SC-1):
         try: 
             index = r.randint(0,L)
             match = index in ID
             ID.append(index)
             if match == False:
                 List[index] = char[r.randint(0,11)]
                 i += 1 
         except:
                 pass
     return List, ID
 
def RNum(List,NN,L,Id):
     char = "1234567890"
     ID = Id
     i = 0 
     while i < (NN):
         try: 
             index = r.randint(0,L)
             match = index in ID
             ID.append(index)
             if match == False:
                 List[index] = char[r.randint(0,9)]
                 i += 1 
         except:
                 pass
     return List    

L = int(input("Enter the password length: "))
SC = int(input("Enter the number of special characters: "))
NN = int(input("Enter the number of numbers: "))

List, ID = RSChar(RLetters(L),SC,L)
List = RNum(List,NN,L,ID)
L = ''.join(List)
print(L)