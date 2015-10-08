#s = 'abcbcd'
#groups = []
#cur_longest = ''prev_char = ''
#count = 0
#for c in s.lower():
#    if prev_char and c < prev_char:        
#        groups.append(cur_longest)
#        cur_longest = c
#    else:
#        cur_longest += c
#    prev_char = c
#print max(groups, key = len)


s = 'zyxwvutsrqponmlkjihgfedcba'
maxx = ''
for i in xrange(len(s)):
    for j in xrange(i+1, len(s)):
        str = s[i:j+1]
        if ''.join(sorted(str)) == str:
            maxx = max(maxx, str, key=len)
        else:
            break
print maxx