#Code base to find out number of vowels. 
# Input string is already provided in this code base. 
s = 'asldfjasdwetivouasdfs'
count = 0
for x in s: 
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):        
        count += 1
print count