"""
We have three categories to check. If the sum of divisors is greater than a number, the number is
abundant. If the sum of divisors is less than a number, the number is deficient. Otherwise, it must
be perfect design control structure for this problem statement

#Nint=28 # Number to be validated 
#Div=1    #Divisor
#while Div<Nint:
#   if Nint % Div==0:
#        print(Div) # Suit1
#Div=Div+1  # Suit 2
"""
Nint = 28
Div = 1
sum_of_divisors = 0
while Div < Nint:
    if Nint % Div == 0:
        sum_of_divisors += Div
    Div += 1
if sum_of_divisors > Nint:
    category = "abundant"
elif sum_of_divisors < Nint:
    category = "deficient"
else:
    category = "perfect"
print("The number", Nint, "is", category)
