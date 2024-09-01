# Logic : # say two subsets are s1 and s2 such that |s1 - s2| = diff.
# and 's1 + s2 = total_sum_arr' .
# After solving these two we will get s1 = (total_sum_arr + diff)//2.
# so Question now reduce to find the no of subests having sum = 's1'.


# method 1: 
# will work properly for all cases in which value of ele will be greater than zero may not for value of ele= 0
def NoOfSubsets(N, arr, sum):
    # 1st initialse the matrix properly, little diff from subset sum
    # or you can do by same way like subset sum as python treat 'False =0'
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

def SubsetWithDiff(arr,diff):
    total= sum(arr)
    if (total+diff) & 1:  # if odd then no such subsets possible 
        return 0
    s1= (total+diff)//2  # by solving mathematically(see the notes)
    return NoOfSubsets(len(arr), arr, s1)

# arr= [1,2,3,3]
# arr= [1,1,2,3]
# diff= 1  
arr= [5,2,6,4]
diff= 3
# print(SubsetWithDiff(arr,diff))

# method 2: will work in all cases
class Solution:
    def SubsetWithDiff1(self, arr, diff): 
        total, n= sum(arr), len(arr)
        if (total + diff) %2 :
            return 0
        s1= (total + diff) //2
        dp= [[-1 for i in range(s1+1)] for i in range(n)]  # no need to go till 'N+1' as we are starting from  'N-1' 
        return self.helper(n-1, arr, s1, dp)
    
    def helper(self, ind, arr, sum, dp):
        if ind== 0:
            if sum== 0 and arr[0]== 0:
                return 2    # either take or notTake
            if sum==0 or sum== arr[0]: # in actual sum== 0 and arr[0] != 0 or sum== arr[0]
                return 1
            else:
                return 0
        if dp[ind][sum] != -1: 
            return dp[ind][sum]
        if arr[ind]> sum:
            dp[ind][sum]= self.helper(ind -1, arr, sum, dp)
        else:   # arr[ind] <= sum
            dp[ind][sum]= self.helper(ind -1, arr, sum- arr[ind], dp) +  self.helper(ind -1, arr, sum, dp)
        return dp[ind][sum]  # return the last ele

# arr= [1,2,3,3]
# arr= [1,1,2,3]
# diff= 1 
arr= [5,2,6,4]
diff= 3
ob= Solution()
print(ob.SubsetWithDiff1(arr, diff))   
# print(ob.SubsetWithDiff1(arr, diff))
