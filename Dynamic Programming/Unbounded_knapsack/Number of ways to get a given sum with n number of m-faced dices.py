# Note: Basically asking the number of ways to get sum = x in 'n' operations
# (or using 'n' numbers) such that all numbers are in range from 1 to m.

# Recursive way

def ways(n, sum):
    if sum == 0:
        return n == 0
    if n <= 0:
        return 0
    ans = 0
    for i in range(1, min(m, sum) + 1):  # will avoid getting sum negative.
        ans += ways(n - 1, sum - i)
    return ans

# n = 2
# m = 4
# X = 4

n = 3
m = 6
X = 12

print("No of ways: ", ways(n, X))


# Method 2: 
# We can reduce this problem to unbounded knapsack where numbers are from '1' to 'm' and
# We can use any number any number of times such that total number used must be = n.
# So we can solve using dp also. Just convert above solutio into dp.

