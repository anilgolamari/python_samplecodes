def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    guess = min(a,b)
    
    while guess >= 1:
        if a % guess == 0 and b % guess == 0:
            return guess
        else:
            guess -= 1
    return guess
        
    