# ans of query (i, j)= prefixSum[j]- preixSum[i-1]

# time: O(n)
import collections
def RangeSum(arr, query):
    n= len(arr)
    prefixSum= {}  # [index: sumTillIndex]
    prefixSum= {-1: 0}  # to handle the case (i,j) when i== 0 
    curSum= 0
    for i , num in enumerate(arr):
        curSum+= num
        prefixSum[i]= curSum
    
    ans= []
    for i, j in query:
        curAns= prefixSum[j] - prefixSum[i-1]
        ans.append(curAns)
    return ans

arr= [1, 4, 1]
query= [[1,1], [1,2], [0,2]]
print(RangeSum(arr, query))

# Note: Whenever there is something related to 'sum in a range', apply prefix sum.
# Can you array also instead of hashmap of size 'n' or 'n + 1' depending upon Q.

# Related q: