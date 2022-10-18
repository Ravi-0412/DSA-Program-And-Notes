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




# increasing order from 1 to n
def show(n):
    if n==1:
        print(n)
        return 
    show(n-1)
    print(n)

show(10)


# decreasing order
def show(n):
    if n==1:
        print(n)
        return 
    print(n)
    show(n-1)

show(10) 


#find factorial
def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5)) 

# find nth fibonacii number
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
def sum(n):
    if n==1:
        return 1
    else:
        # smallAns= sum(n-1)
        # return n+smallAns
        return n + sum(n-1)  # wherever there is format like 'smalAns'
                             # you may directly write the return 
# print(sum(5))


#2nd method
def sum1(n):
    ans= 0
    if n==0:
        return 0
    ans= n+ sum1(n-1)
    return ans

print(sum1(5))


# reverse an array
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


# check whether a given string is palindrome or not
def palindrome(s,i,n):
    if s[i]!= s[n] :
        print("not palindrome")
        return
    if i>= n:  # if i reaches till middle means palindrome
        print("palindrome")
        return 
    palindrome(s,i+1,n-1)

palindrome("malayalam",0,8)





















