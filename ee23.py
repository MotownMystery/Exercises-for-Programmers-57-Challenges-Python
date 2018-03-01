## Car Trouble Shot 

Actions = {'1': 'Is the car silent when turned on?',
         '2a': 'Are the Battery terminals corroded',
         '2b': 'Does the car make a clicking noise',
         '3a': 'Clean terminals',
         '3b': 'Replace cables',
         '3c': 'Replace battary',
         '3d': 'Does car crack',
         '4a': 'Check Spark plugs',
         '4c': 'Does engine start',
         '5a': 'Does your car have fuel',
         '6a': 'Check chock',
         '6b': 'Get it services'}

Steps = ['1','2a','2b','3a','3b','3c','3d','5a','6a','6b']

print(Actions['1'])

i = 1
while True:
    x = input('Y or N ')
    if x == 'Y': 
        print(Actions[Steps[i]])
        i = i + 1
    if x == 'N': 
        if i > 9:
            break
        
        print(Actions[Steps[i+1]])
        i = i + 2
    
 
    


