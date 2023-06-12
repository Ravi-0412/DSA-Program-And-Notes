# reverse a number

# method 1:



# method 1: Iterative
def reverse(n):
    ans= 0
    while n >0:
        r= n%10
        ans= ans*10 + r
        n= n//10
    return ans
print(reverse(234))


# method 2:
def reverse(n):
    if n<10:
        print(n)
    else:
        print(n%10,end="")
        reverse(int(n/10))
# print("reversed no is: ",end="")
# reverse(234)


# method3: traeting as string 
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

# shorter of above
def reverse(n):
    ans= ""
    if n<10:
        return str(n)
    return str(n%10) + reverse(n//10)
print(reverse(234))


#method 4
import math
def reverse(n,x):
    sum=0
    if n<10:
        return n
    r= n%10
    sum+= r*pow(10,x) 
    smallAns= reverse(int(n/10),x-1)
    sum+= smallAns
    return sum
# num= int(input("enter the number"))

# digits= int(math.log(num,10))   # to start multiplying 10 with power of ('no of digits in num'-1)
                                # and this log will give the same only no need to subtract '-1'
# print(reverse(num,digits)) 


# shorter version of above
import math
def reverse(n,x):
    if n<10:
        return n
    r= n%10   
    return r*pow(10,x) + reverse(int(n/10),x-1)
    
# num= int(input("enter the number: "))

# digits= int(math.log(num,10))   # to start multiplying 10 with power of ('no of digits in num'-1)
#                                 # and this log will give the same only no need to subtract '-1'
# print(reverse(num,digits)) 

# method 5: by taking only one argument
# Not able to convert above iterative method into recursive method by passing the 'ans' inside the function(not as argument).
