# just similar logic, we did in "85.maximal Rectangle"
# logic: just find the area of each rectangle from every row one by one.
# i.e combine the row starting one by one and calculate the ans using kedane's algo.

# Note: just same as "finding max subarray sum". Here only we considering all rectangles that can be formed combing each row(or col).
# just the brute force of 1D(consider all subarray that can form from each ele)

# time: O(R*R*C) : for getting the sum array + O(R*R*C): for calculating the maximumSumSubArray using Kedane algo after getting the sum array.
class Solution:
    def maximumSumRectangle(self,R,C,M):
        maxSum= -99999999
        for start in range(R):
            sum= [0 for i in range(C)]
            for end in range(start,R):
                for c in range(C):
                    sum[c]+= M[end][c]
                # now find the maximum sum for current joined rows rectangle using Kedane Algo
                currSum= self.Kedane(sum)
                maxSum= max(currSum, maxSum)
        return maxSum
    
    def Kedane(self, arr):
        maxSum, currSum= -99999999, 0
        for i in range(len(arr)):
            currSum= max(arr[i], currSum + arr[i])  # if currSum is negative, make currSum= arr[i]
            maxSum= max(currSum, maxSum)
        return maxSum

