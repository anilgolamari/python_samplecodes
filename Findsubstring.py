#code base to print repeated word in a string.
s = 'azcbobobegghakl'
total = 0
for i in range(len(s)-2):
    if s[i:i+3] == 'bob':
        total += 1
print 'number of times bob occurs is: ', total