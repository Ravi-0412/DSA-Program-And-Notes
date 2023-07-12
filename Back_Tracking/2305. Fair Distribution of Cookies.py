# Exactly same as "698. Partition to K Equal Sum Subsets" except base condition.
# We have to get the max from each subset distribution and then update the ans with minimum of these maximum.

# Note vvvvi: why we can't apply binary serach?
# If it would have been given that "all children can get only contiguous cookies" 
# then, this will be same as "allocate minimum no of pages" binary search q.

# Time: O(k^n)

# Explanation of optimisation when: sums[j] == 0: return

# Let cookies = [8,15,10] and k=2.
# Then the subsets we calculate are [33,0] , [23,10], [18,15], [8,25], [25,8], [15,18], [10,23], [0,33].
# Here we observe [33,0] and [0,33] refers to same subset and similary other.
# So we can reduce the duplicates by breaking the loop if v[i] is equal to 0, as it will be covered in the other subset.
# In the for loop of above code, we break the loop if v[i] is equal to 0, 
# because without this line we are just calculating the same subset with different combinations which is unnecessary.
# So now the subsets we calculate will only be: [33,0] , [23,10], [18,15], [8,25].

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        self.ans = float('inf')
        sums = [0]*k

        def backtrack(i):
            if i == n:
                # we have to update ans
                # first find the max sum of all partition and then update the ans.
                maxSum = max(sums)
                # Now to get minimum of all max(sums) of every possible partition.
                self.ans = min(self.ans, maxSum)
                return 
            for j in range(k):
                if sums[j] + cookies[i] < self.ans:  # optimisation
                    sums[j] += cookies[i]
                    backtrack(i + 1)
                    sums[j] -= cookies[i]
                    if sums[j] == 0:   # optimisation
                        return
        
        backtrack(0)
        return self.ans


# Method 2: Try by DP + BitMaskimg
