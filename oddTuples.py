def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTup = ()
    count = len(aTup)
    
    while count > 0:
        newTup += (aTup[count],)
        count += 2   
    return newTup