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