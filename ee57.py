import json
import random as r 
data = json.load(open('JEOPARDY_QUESTIONS1.json'))
count = 0
while True: 
    R_id = r.randint(0,len(data))
    print(data[R_id]['category'])
    print(data[R_id]['question'])
    ASW = input('Answer ---> ')
    if ASW == '': 
        print("Your score was: ", count)
        break
    else:
        if ASW.lower() == data[R_id]['answer'].lower():
            print('Correct!')
            count += 1
        if ASW.lower() != data[R_id]['answer'].lower():
            print("Nope, the answer was: ", data[R_id]['answer'])
    
    
    
    



