## 

switch = {1 : 'Jan',
          2 : 'Feb',
          3 : 'Mar',
          4 : 'Apr',
          5 : 'May',
          6 : 'Jun',
          7 : 'Jul',
          8 : 'Aug',
          9 : 'Sep',
          10 : 'Oct',
          11 : 'Nov',
          12 : 'Dec'}

M = switch[int(input("Please enter the number of the month? "))]
print(f"The name of the month is: {M}")