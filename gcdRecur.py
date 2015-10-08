def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

    If b = 0, then the answer is a

    Otherwise, gcd(a, b) is the same as gcd(b, a % b)
    
    Recursive= n * (n-1) *..... 1
    base = a
    exp = b
    '''
    # Your code here
    guess = min(a,b)
    
    while guess >=1:
        if b == 0:
            guess = a
        else:
            guess = gcdRecur(b, a % (b-1))
    return guess
        
    