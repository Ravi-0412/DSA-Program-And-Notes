# submitted on codeStudio but give incorrect ans for one test case(6th decimal place incorrect only)

def findNthRootOfM(n,m):
    low, up= 1, m
    precision= 10**-7 # we have to find till  6 decimal places
    while up - low> precision:    # just like while low< up => while up-low>0 instead of '0' we are comapring with precision.
        mid= float(low + (up-low)/2)
        if multiply(mid, n) >= m:
            up= mid
        else:
            low= mid+ precision
    return ('%.6f' % low)   # to return ans with '6' decimal places

def multiply(number, n):
    ans= 1
    for i in range(n):
        ans*= number
    return ans

# can use the same logic to find the square root of a number with decimal places.
