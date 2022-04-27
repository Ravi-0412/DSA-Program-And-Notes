# sum of 1st n natural number: By recursion
def sum(n):
    if n==1:
        return 1
    else:
        # smallAns= sum(n-1)
        # return n+smallAns
        return n + sum(n-1)

# print(sum(5))

#2nd method
def sum1(n):
    ans= ""
    if n==0:
        return 0
    ans= n+ sum1(n-1)
    return ans

print(sum1(5))
    