# Just same as '3. Longest Substring Without Repeating Characters'.
# Here we only have to count the number.

# After each character check for valid substring then no of new substring formed
# will be equal to the length of substring.
# Because for that valid substring all combination will be part of answer.

from collections import defaultdict 
def countSub(s):
    n = len(s)
    count = defaultdict(int)
    ans = 0
    i, j = 0, 0
    while j < n:
        count[s[j]] += 1 
        while j- i + 1 > len(count):
            count[s[i]] -=  1 
            if count[s[i]] == 0:
                del count[s[i]]
            i += 1 
        ans += j - i + 1
        j += 1
    return ans

# s = "gffg"
s = "gfg"
print("no of substring is : ", countSub(s))


