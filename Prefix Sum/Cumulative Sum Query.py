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