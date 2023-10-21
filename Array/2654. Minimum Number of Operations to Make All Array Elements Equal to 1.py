# logic: we can only make all ele equal to "1" by gcd if there is '1' already present in the array or we can make any ele =1 somehow.

# cases: 1) if there is already "1' is present in the array then
# ans= n- no_of_1. we can make other remaining ele(non-1)  =1 by taking gcd with its adjacent ele(here next adjacent ele).

# 2) If there is no "1", then ans= x + (n-1), where x= min cost of making any ele of any subarray =1 by doing gcd operation.
# for this we need to find the smallest subarray we for which we can make any ele of that subarray= 1.
# say for subarray [i, j] we can make any ele of this subarray =1 then cost= j- i  (i, j are index).
# we will have to do gcd operation "j-i" times.

# for solving, we will check every possible subarray from each index and will try to make gcd=1 including all its next ele one by one.
# time= O(n^2 * logn)  
# for time complexity gcd: https://codeforces.com/blog/entry/48417  

import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n= len(nums)
        one= nums.count(1)
        if one:  # if there is at least '1' present
            return n- one
        ans= float('inf')
        for i in range(n-1):
            g= nums[i]
            for j in range(i+ 1, n):  # Taking gcd of all ele from index 'i'.
                g= math.gcd(g, nums[j])
                if g== 1:
                    ans= min(ans, (j- i) + (n-1))  # "j-i" for cur subarray and "n-1" for remaining 'n-1' ele.
        return ans if ans!= float('inf') else -1


# Note: if Q "find the min operation to make any ele =1 by relacing(like above Q)".
# we would have applied the same approach: "find the smallest subarray we for which we can make any ele of that subarray= 1 " then ans= j -i.

# later try by other approach also(solution in sheet).
