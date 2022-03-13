# reverse a number
# mwthod 1:
def reverse(n):
    if n%10== n:
        return n
    else:
        r= n%10
        sum1= sum1*10 + r
        reverse(int(n/10))
# print(reverse(234))

# method 2:
def reverse(n):
    if n<10:
        print(n)
    else:
        print(n%10,end="")
        reverse(int(n/10))
print("reversed no is: ",end="")
# reverse(234)


# method3:
def reverse(n):
    ans= ""
    if n<10:
        ans= ans+ str(n)
        return ans
    else:
        r= n%10
        ans+= str(r)
        smallAns= reverse(int(n/10))
        ans+= str(smallAns)
    return ans
# print(reverse(234))


#method 4
import math
def reverse(n,x):
    sum=0
    if n<10 or x==0:
        return n
    else:
        r= n%10
        sum+= r*pow(10,x) 
        smallAns= reverse(int(n/10),x-1)
        sum+= smallAns
    return sum
num= int(input("enter the number"))

digits= int(math.log(num,10))   # to start multiplying 10 with power of (no of digits in num-1)
                                # and this log will give the same only no need to subtract '-1'
print(reverse(num,digits)) 
