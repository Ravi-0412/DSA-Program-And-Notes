# sum of digits of a number
def SumDigit(n):
    sum,r,q= 0,0,0
    if 0<=n<=9:   # or if n%10== n 
        return n
    else:
        r= n%10
        q= int(n/10)
        sum1= SumDigit(q)
        return r+sum1

# print(SumDigit(234))

# 2nd method:
def SumDigit1(n):
    sum,r,q= 0,0,0
    if n< 10:   # or if n%10== n 
        return n
    return n%10 + SumDigit1(n//10)

print(SumDigit1(234))