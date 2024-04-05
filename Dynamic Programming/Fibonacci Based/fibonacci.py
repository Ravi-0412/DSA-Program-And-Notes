# method 1: Recursive way
# recurrence relation: T(n)= T(n-1) + T(n-2);n>1 and T(n)= n;n<=1.. solve this reccurence relation to get the actual time complexity
# time: O(1.6180^n) nearly O(2^n).. '1.6180 is also called as golden ration'
# space: 0(n)
def fib(n):
    if n<=1:
        return n
    return fib(n-1) +fib(n-2)

# print(fib(5))

# method 2: memoization(Top Down)
# time= O(n)
# space: O(n+n)
# just replace by dp value instead of return in recursion call only.. not at all return places 
def fib1(n):
    dp= [-1]*(n+1)  # here no of variable changing in each recursion is only one, so we need only 1D dp
    return helper(n,dp)

def helper(n,dp):
    if n<=1:
        return n   # here don't replace by dp as this return is not with recursion call, it is associated with base case
    if dp[n]!= -1:  # check if value is already calculated.. this is memoization 
        return dp[n]
    dp[n]= helper(n-1,dp) + helper(n-2,dp)  # here we are returning for fib(n) so replace here 
    return dp[n]   # at alst return dp[n] for which function is called

# print(fib1(6))

# method 3: tabulation: Bottom up
# time= O(n)
# space: O(n)
def fib2(n):
    dp= [-1]*(n+1)
    # now initialise the base cases with their values so that we can directly remaining ans seeing the values of base cases
    dp[0],dp[1]= 0,1
    # now start finding the values other than base case
    for i in range(2,n+1):
        dp[i]= dp[i-1] + dp[i-2]
    return dp[n]

# print(fib2(6))


# optimising the space complexity
# we only need pre two values to calculate the fib of current no
# time: O(n), space: O(1)
def fib3(n):
    pre1, pre2= 1, 0  # just base cases values
    for i in range(2,n+1):
        curr= pre1 + pre2
        pre1, pre2= curr, pre1
    return pre1  # as after this loop will end , pre1 will store the value of fib(n)
print(fib3(6))


