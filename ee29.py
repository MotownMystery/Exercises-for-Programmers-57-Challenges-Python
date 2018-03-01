while True:
        try: 
            r = float(input("What is the rate of return? "))
            if r != 0: break
            if r == 0: print("Error 0 entered.")
        except ValueError:
            print("Sorry that isn't a valid input")


years = 72/r  
print(f"It will take {years} years to double your initial investment")  