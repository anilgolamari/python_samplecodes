#find whether a string has vowels like aeiou
def isvowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        return True
    else:
        return False


def isvowel2(char):
    for x in char:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            return True
        elif x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
            return True
        else:
            return False
        