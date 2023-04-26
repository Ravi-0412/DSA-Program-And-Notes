# This Q is only observation in detail.
# solution in Notes. page no: 94

# LOGIC: Target the index directly and observe.
# time: O(1)
def goodBinaryString(s):
    n= len(s)
    if s[0]!=  s[n-1]:
        return 2
    return n-2

s= "10100"
# s= "11111"

print(goodBinaryString(s))


# for codechef
tc = int(input())  # no of test cases
for t in range(tc) :
    s = input()      # each test case input
    n= len(s)
    if s[0]!= s[-1]:
        print(2)
    else:
        print(n-2)