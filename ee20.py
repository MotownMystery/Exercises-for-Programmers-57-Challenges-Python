## State Tax Calc
from babel.numbers import format_currency
St = {'WI' : .05, 'wi': .05, 
      'IL' : .04,'il': .04}

Amt = float(input("What is the amount? "))
Sta = St[input("What state do you live in?")]
tax = Amt*Sta 
tot = tax+Amt

T = format_currency(tax, 'USD', locale='en_US')
TT = format_currency(tot, 'USD', locale='en_US')
print(f"The tax is: {T}\nThe total is: {TT}")


