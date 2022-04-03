def NoOfSubsets(N, arr, sum):
    # 1st initialse the matrix properly, little diff from subset sum
    # or you can do by same way lik esubset sum as python treat 'False =0'
    # and 'True=1' only
    dp= [[0 for i in range(sum+1) ] for i in range(N+1)]
    for i in range(N+1):
        for j in range(sum+1):
            if j==0:
                dp[i][j]= 1
    # exactyle same as subset sum          
    for i in range(1,N+1):
        for j in range(1,sum+1):
            if arr[i-1]> j:  # no subset possible,just replace or with '+'
                dp[i][j]= dp[i-1][j]
            else: # subset possible including this ele + subset possible without including it
                dp[i][j]= dp[i-1][j-arr[i-1]] + dp[i-1][j]
    return dp[N][sum]

# arr= [1,2,3,3]
# arr= [1,1,1,1]
arr= [1,1,2,3]
# print(NoOfSubsets(4,arr,6))   
print(NoOfSubsets(4,arr,4)) 

