#Method1 Recursive method to calculate base ^ exp by multiplying base exp number of times.

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here 
    if exp <= 0:        
        return 1
    else:
        return base * recurPower(base, exp-1)
        
        
    
#Method2 Use exponential method to calculate recurpower. Below are conditional statements to be used.
# base ** exp = (base ** 2) exp/2  if exp >0 and exp is even
# base ** exp = base * base ** exp-1  if exp >0 and exp is odd
# base ** exp = 1 if exp == 0


def recurPowerNew(base, exp):
    if exp == 0:
        return 1
    elif exp > 0 and exp % 2 == 0:
        return (base ** 2) ** (exp /2)
    else: 
        return base * (base ** (exp -1))
        

def recurPowerNew(base,exp):
    if exp <= 0:
        return 1
    elif exp % 2 == 0:
        return  recurPowerNew(base * base, exp/2)
    else:
        return base * recurPowerNew(base, exp-1)
    
        
    
  