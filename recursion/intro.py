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
    if n>5:   # base condition
        return
    print(n)
    show(n+1)
show(1)
 