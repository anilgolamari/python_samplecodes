x = "pi"
y = "pie"

x, y = y, x


def f(x):
    while x > 3:
        f(x+1)
        
        
d = {'Name': 'Zara', 'Age': 7, 'Class': 'First', 'age1': 7};


def f(L):
    L.append(4)


x = [1,2,3]



def find(x):
    for thing in x:
        if thing == 'iPad':
           print "Found it"
           
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    guess = 0    
    while x >= b ** guess:
        temp = guess
        guess += 1       
    return temp
    
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    bList = []
    for i in aList:        
        if len(i) <4: 
            bList.append(i)
    return bList

def sumDigits(N):
        '''
        N: a non-negative integer
        '''
        # Your code here
        if N == 0:
            return 0
        else:
            return (N%10) + sumDigits(N/10)


def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here 
    alist = []
    if len(aDict) == 0:
        return alist
    else:        
        for key, value in aDict.items():
            if value == target:
                alist.append(key)
                alist.sort()
        return alist
        
def satisfiesF(L):

   count= len(L)
   alist = []

   for i in range(0,count):
       if(f(L[i])==False):
           alist.append(L[i])   
   if(alist):
       for j in alist:
           L.remove(j)
   return len(L)
run_satisfiesF(L, satisfiesF) 
    
    



