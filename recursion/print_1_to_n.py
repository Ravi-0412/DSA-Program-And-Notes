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