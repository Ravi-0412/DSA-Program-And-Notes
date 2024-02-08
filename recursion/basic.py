# example 1:
# class Numbers:
#     # write a function that takes a number and prints it
#     # print 5 numbers: 1 2 3 4 5 
#     def print1(self,n):
#         print(n)
#         self.print2(2)
    
#     def print2(self,n):
#         print(n)
#         self.print3(3)
#     def print3(self,n):
#         print(n)
#         self.print4(4)
#     def print4(self,n):
#         print(n)
#         self.print5(5)
#     def print5(self,n):
#         print(n)
    
# l1= Numbers()
# l1.print1(1)


# recursive way 

def show(n):
    if n>5:   # base condition: where the recursion will stop
        return  # no base condition will give "stackoverflow error["
    print(n)
    show(n+1)
show(1)




# increasing order from 1 to n.
# Note: pass kiye h 'n' input me but ans chahiye hmko reverse order me i.e from '1 to n', 
# isliye jb fn call return hoga sbse lowest ke liye tb print karbana start karenge like phle function ko call karna h then print karbana h.

# Pattern 2
def show(n):
    if n==1:
        print(n)
        return 
    show(n-1)
    print(n)
    # return   # whether you write this or not, 
               # after doing all operation it will automatically return to the fn which has called it if there is no return statement.
               # and even if there is return statement ,it will automatially return to the fn which has called it.

show(10)

# decreasing order
# # Note: pass kiye h 'n' input me and ans chahiye hmko same order me i.e from 'n to 1', 
# isliye phle print karbana h then fn to call karna h.

# Pattern 2.
def show(n):
    if n==1:
        print(n)
        return 
    print(n)
    show(n-1)

show(10) 


#find factorial
# Pattern 2.
def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)
print(fact(5)) 

# find nth fibonacii number
# Patetrn 1.
def fibonacii(n):
    if n==0 or n==1:
        return n
    return fibonacii(n-1) + fibonacii(n-2)

print(fibonacii(9))

# fibonacii using DP
def fibonacii(n):
    fib= [0,1]   # base case value are stored initially in the array
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# print(fibonacii(9))


#  sum of 1st n natural number: By recursion
# pattern 2
def sum(n):
    if n==1:
        return 1
    # smallAns= sum(n-1)
    # return n+smallAns
    return n + sum(n-1)  # wherever there is format like 'smallAns'
                             # you may directly write the return combining all.
# print(sum(5))


#2nd method
# Note: Jahan pe bhi hmko 'smallAns' ko include karna pad rha ho current ans me, 
# wahan direct return kar do sbko combine karke in same order.
def sum1(n):
    ans= 0
    if n==0:
        return 0
    ans= n+ sum1(n-1)
    return ans

print(sum1(5))


# reverse an array
# Pattern 2

# can do by passing a single variable also.
def reverse(arr,i,n):
    if i>= n:  # both will meet at middle only and after mid no need to check
        return
    arr[i],arr[n]= arr[n], arr[i]
    reverse(arr,i+1,n-1)

arr= [1,2,3,4,5]
reverse(arr,0,len(arr)-1)
print(arr)



# sum of digits of a number
def SumDigit(n):
    sum,r,q= 0,0,0
    if 0<=n<=9:   # or if n%10== n 
        return n
    r= n%10
    q= n//10
    sum1= SumDigit(q)
    return r+sum1

# print(SumDigit(234))

# method 2:
def SumDigit(n):
    if n==0:   # or if n%10== n 
        return 0
    ans= 0
    r= n%10
    q= int(n/10)
    ans+= r+ SumDigit(q)
    return ans

print(SumDigit(234))

# 3rd method: shortcut of above two
# Best one
# Pattern 2.
def SumDigit1(n):
    if n< 10:   # or if n%10== n 
        return n
    return n%10 + SumDigit1(n//10)

print(SumDigit1(234))


# check whether a given string is palindrome or not
def palindrome(s,i,n):
    if i>= n:  # if i reaches till middle means palindrome
        print("palindrome")
        return 
    if s[i]!= s[n] :
        print("not palindrome")
        return
    palindrome(s,i+1,n-1)

palindrome("malayalam",0,8)


# Note: Recursive function hmesha last valid input ya first invalid input pe aake rukega.

















