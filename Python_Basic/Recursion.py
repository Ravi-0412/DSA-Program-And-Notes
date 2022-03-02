
# def factorial(num):
#     if num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
# number= int(input("enter any number"))
# print(factorial(number))


def fib(num):
    return num if num<=1 else fib(num-1)+ fib(num-2)
number= int(input("enter any number \n"))
for num in range(number):
    print(fib(num))