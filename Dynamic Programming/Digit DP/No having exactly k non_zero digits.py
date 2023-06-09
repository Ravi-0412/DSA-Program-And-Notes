# Recursion + memoisation
# time: (no_digits * 2 * no_digits) i.e = max possible value of (ind * tight * count)
from functools import lru_cache

def findNo(n, k):
    s= str(n)
    
    @lru_cache(None)
    def solve(ind, tight, count):
        if ind == len(s):
            if count == k:
                return 1
            return 0
        ans= 0
        end= int(s[ind]) if tight else 9
        for digit in range(end + 1):
            newTight= tight and digit== end
            if digit== 0:
                ans+= solve(ind + 1, newTight, count)
            else:
                ans+= solve(ind + 1, newTight, count + 1)
        return ans
    
    return solve(0, 1, 0)   # [ind, tight, count_non_zero]
    
# n= 100
# k= 1

# n= 25
# k= 2

# n= 314159
# k= 2

n= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
k= 3

print(findNo(n, k))


# method 2: used dp array
def findNo(n, k):
    s= str(n)
    l= len(s)
    
    dp= [[[-1 for c in range(l+ 1)] for bound in range(2)] for i in range(l + 1)]  
    # here count can go till 'l + 1' because we are not using any base case if count > k.
    # because there is possiblity that count > k and some indexes are still left to fill.

    def solve(ind, tight, count):
        if ind == len(s):
            if count == k:
                return 1
            return 0
        if dp[ind][tight][count] != -1:
            return dp[ind][tight][count]
        ans= 0
        end= int(s[ind]) if tight else 9
        for digit in range(end + 1):
            newTight= tight and digit== end
            if digit== 0:
                ans+= solve(ind + 1, newTight, count)
            else:
                ans+= solve(ind + 1, newTight, count + 1)
        dp[ind][tight][count]= ans
        return ans
    
    return solve(0, 1, 0)   # [ind, tight, count_non_zero]
    
# n= 100
# k= 1

n= 25
k= 2

# n= 314159
# k= 2

# n= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# k= 3

print(findNo(n, k))


# here passing base case also for count > k then no need to take size of count = max i.e 101 
def findNo(n, k):
    s= str(n)
    l= len(s)
    
    dp= [[[-1 for c in range(k + 1)] for bound in range(2)] for i in range(l + 1)]
    def solve(ind, tight, count):
        if ind == len(s):
            if count == k:
                return 1
            return 0
        if count > k :
            return 0
        if dp[ind][tight][count] != -1:
            return dp[ind][tight][count]
        ans= 0
        end= int(s[ind]) if tight else 9
        for digit in range(end + 1):
            newTight= tight and digit== end
            if digit== 0:
                ans+= solve(ind + 1, newTight, count)
            else:
                ans+= solve(ind + 1, newTight, count + 1)
        dp[ind][tight][count]= ans
        return ans
    
    return solve(0, 1, 0)   # [ind, tight, count_non_zero]
    
# n= 100
# k= 1

# n= 25
# k= 2

n= 314159
k= 2

# n= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# k= 3

print(findNo(n, k))
