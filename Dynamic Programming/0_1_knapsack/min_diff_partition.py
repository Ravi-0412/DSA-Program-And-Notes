# Q: You have to count the no of subsets such that their
# diff in sum is minimum among all the subsets sum difference

# submitted on GFG
def isSubsetSum (N, arr, sum):
    # 1st initialse the matrix properly
    dp= [[-1 for i in range(sum+1) ] for i in range(N+1)]
    for i in range(N+1):
        for j in range(sum+1):
            if i==0:
                dp[i][j]= False
            if j==0:
                dp[i][j]= True
    # now just same as 0/1 Knapsack           
    for i in range(1,N+1):
        for j in range(1,sum+1):
            if arr[i-1]> j:
                dp[i][j]= dp[i-1][j]
            else:
                dp[i][j]= dp[i-1][j-arr[i-1]] or dp[i-1][j]
    return dp[N]  # this will contain the possible subset sum for numbers till total(boolean array)
                  # since we are returning the last row and last row will give the ans for all possible subset sum till total

def minDifference(arr,n):
    total= sum(arr)
    possible_subset_sum= isSubsetSum(n,arr,total) 
    # possible_subset_sum will contain the array with possible_sum till total
    # print(possible_subset_sum) 
    subset_to_check= (total)//2+1   # we have to check till middle only 
    possibe_till_half= [0]*subset_to_check   # this will store the number for which subset sum 
                                            # is possible till middle of total(except 1st index) 
    j= 0
    # print(possibe_till_half)
    for i in range(subset_to_check):
        if possible_subset_sum[i]== True:
            possibe_till_half[j]= i
            j+= 1
    min_diff= 999999999
    # print(possibe_till_half)
    for num in possibe_till_half:
        min_diff= min(min_diff, total-2*num)
    return min_diff

arr= [1,6,11,5]
print(minDifference(arr,4))

