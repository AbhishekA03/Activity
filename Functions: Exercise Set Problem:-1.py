"""
Suppose you are buying something online on amazon.com 

On the website, you get
a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.

Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.
"""
def discount(amount,prime_member,friday):
    if prime_member and friday:
        return (amount-((23*amount)/100))
    elif prime_member:
        return (amount-((15*amount)/100))
    else:
        return 'No discount'
        
print(discount(1200,True,False))
