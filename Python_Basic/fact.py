number= int(input("enter any number \n"))
def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(number))
