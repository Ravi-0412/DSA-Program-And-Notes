# we are using range of subarrray and finsing the smallest number 'left' such that left>=right-k.
# from  'right- left <= k', we can't directly get the ans so converted into above form.

from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col= len(matrix), len(matrix[0])
        maxSum= -inf
        for start in range(col):
            sum= [0 for i in range(row)]
            for end in range(start,col):
                for r in range(row):
                    sum[r]+= matrix[r][end]
                # now find the maximum sum for current joined rows rectangle like Kedane Algo
                currSum= self.MaximumSumSubArray(sum, k)
                # print(currSum)
                maxSum= max(currSum, maxSum) 
        return maxSum
    
    def MaximumSumSubArray(self, arr, k):
        right= 0  # will store the currsum for all  index like 0,1,2...
        seen= SortedList([0])  # will store the curr sum i.e 'right'
        ans= -inf
        for i in range(len(arr)):
            right+= arr[i]
            left= self.Ceiling(seen, right-k)  # right - left <= k =  left >= right - k
            if left != None:   # means if we have seen the this difference then update the ans
                ans= max(ans, right - left)  # ans will be equal to 'right-left'
            seen.add(right)  
        return ans

    def Ceiling(self, SortedList, key):
        ind= SortedList.bisect_left(key)
        if ind < len(SortedList):
            return SortedList[ind]
        else:
            return None

# used python library
# https://www.geeksforgeeks.org/python-sorted-containers-an-introduction/
# https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/