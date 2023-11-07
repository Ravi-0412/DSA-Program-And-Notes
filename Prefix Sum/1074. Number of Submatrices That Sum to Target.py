# 1D version of this "560. Subarray Sum Equals K"

# Logic : we will try to convert 2D matrix into 1D array and 
# after that we will apply same logic of "560. Subarray Sum Equals K".

# Logic : We can start row wise and take sum of all pair of rows starting from row 'i'
# and then we can apply the logic of 1D.

# in the case of 1D array you get results for subarrays of all lengths starting from any point.
# i.e you are checking rectangles of 1x1, 1x2, 1x3 ..... upto length.

# When you apply this to a 2D->1D array at each 'i' you are checking rectangles of all sizes starting from i.
# which looks like ( (1x1, 1x2 ...upto length of row then 2x1, 2x2 ...upto length of a row) .... upto length of columns)
# for each row in original matrix as their 1st row, hence the result includes all combinations of submatrices.


# time : O(r*c*c) + O(c)

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m , n = len(matrix) , len(matrix[0])

        def subarraySum(nums):
            ans,curr_sum= 0,0
            prefix_sum= {0:1}  # [sum: frequency]  # since we can get diff= 0 also because '-ve' number is also there. 
            for n in nums:
                curr_sum+= n
                diff= curr_sum - target  
                ans+= prefix_sum.get(diff, 0) 
                prefix_sum[curr_sum]= 1+ prefix_sum.get(curr_sum, 0) 
            return ans

        ans = 0
        row = [0]*n   # will store the prefixSum of rows
        for i in range(m):
            # store prefixSum of all rows starting from 'i'
            row = [0] *n  # initialising with '0' again to calculate sum starting from row 'i'.
            for j in range(i , m):
                for k in range(n):
                    row[k] += matrix[j][k]
                ans += subarraySum(row)
        return ans
