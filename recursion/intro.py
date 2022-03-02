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
# def show(n):
#     if n>5:   # base condition: where the recursion will stop
#         return  # no base condition will give "stackoverflow error["
#     print(n)
#     show(n+1)
# show(1)


# find nth fibonacii number
# def fibonacii(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return fibonacii(n-1) + fibonacii(n-2)

# print(fibonacii(9))


# fibonacii using DP
def fibonacii(n):
    fib= [0,1]   # base case value are stored initially in the array
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
        print(fib[i])
    return fib[n]

print(fibonacii(9))


