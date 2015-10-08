def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    c = aStr.lower()
    result = ''
    count = 0
    for s in c: 
        if s in 'abcdefghijklmnopqrstuvwxyz':
            result = result + s
            count += 1
    return count
    
    
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr using recursive method
    '''
    # Your code here
    if aStr == '':
        return 0

    # Recursive case: If the string is not zero-length, then remove the first
    #  character and the length is 1 + the length of the rest of the string
    return 1 + lenRecur(aStr[1:])
    
    
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False
    
         
    s= aStr.lower()
    count = len(aStr)/2
    middlechar = s[count]
    if lenIter(aStr) == 1:
        return char == aStr
    
    if char == middlechar:
        return True
    elif char < middlechar:
        return isIn(char, s[: count])
    else:
        return isIn(char, s[count+1:])
            
            
        
    
    
    
    
            
            
    