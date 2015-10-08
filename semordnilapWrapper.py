def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
    
    
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
        # String 1 Properties
    s1 = str1.lower()
    count1 = len(str1)
    
    # string 2 properties
    
    s2 = str2.lower()
    count2 = len(str2)
    
    if count1 != count2:
        return False
    
    if count1 == 1:
        return str1 == str2  
    
    if s1[0] == s2[-1]:
        return semordnilap(s1[1:], s2[:-1])
    else:
        return False

              
    

         

    
            