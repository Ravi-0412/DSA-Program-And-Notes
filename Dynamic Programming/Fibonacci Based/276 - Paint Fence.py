# submitted on coding ninja
# write the logic in notes properly. 

# time: O(n)

def numberOfWays(n: int, k: int) -> int:
    
    def solve(n):
            if n== 1:
                return k
            if n== 2:
                return k + k*(k-1)    # k: when last two same, k*(k-1): when las two diff
            if dp[n]!= -1:
                return dp[n]
            # same= (solve(n-2) * (k-1))  % (10**9 + 7)   # when last two fence have same color.
            # diff= (solve(n-1) * (k-1))  % (10**9 + 7)   # when last two fence have diff color.
            # dp[n]= (same +  diff) % (10**9 + 7)
            dp[n]= ((solve(n-2) * (k-1)) % (10**9 + 7)  + (solve(n-1) * (k-1)) % (10**9 + 7)) % (10**9 + 7)   # shortcut
            return dp[n]
        
    dp= [-1 for i in range(n+1)]
    return solve(n)


# tabulation
def numberOfWays(n: int, k: int) -> int:
    if n==1 : return k
    mod= 10**9 + 7
    dp= [0 for i in range(n+1)]
    dp[1]= k
    dp[2]= k + k*(k-1)
    for i in range(3, n+1):
        dp[i]= (dp[i-1]*(k-1) + dp[i-2] *(k-1)) % mod
    return dp[n]


# sapce optimisation to O(1)
def numberOfWays(n: int, k: int) -> int:
    if n==1 : return k
    mod= 10**9 + 7
    dp= [0 for i in range(n+1)]
    same= k
    diff= k + k*(k-1)
    for i in range(3, n+1):
        dp[i]= (diff*(k-1) + same *(k-1)) % mod
        same, diff= diff, dp[i]
    return diff