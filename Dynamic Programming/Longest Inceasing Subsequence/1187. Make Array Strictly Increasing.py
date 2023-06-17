# logic: 
# Note vvi: if you find arr1[i] > arr1[i+1] then you can't move simply ahead, you have to consider the swapping one also.
# Because you have to fidn the minimum swap.

# Here here choices will come and subproblem will repeat.

# For each element in arr1, you can either choose to not swap it or swap it with some element in arr2.

# 1) If you don't swap it, you need to make sure current element in arr1 is bigger than
# previous element in arr1. Otherwise you have to swap it.

# 2) If you swap it, you need to pick up the smallest element in arr2 that is bigger than the previous element in arr1. 
# If no such element in arr2, you can't swap

# dfs(i, prev): "i" represents index in arr1. "prev" represents the previous element in arr1 after swap (or maybe not swap). 
# It returns the minimal changes required to make 0~i of arr1 increasing.


# time: O(n^2 * logn)

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))

        @lru_cache(None)
        def dfs(ind, pre):  # pre will just store the last ele of arr2.
            if ind >= len(arr1):
                # we have traversed whole array
                return 0
            # 1) if curr index 'ind' has value greater than last ele i.e pre then no need of swap.
            no_swap = dfs(ind + 1 , arr1[ind]) if arr1[ind] > pre else float('inf')  # inf will tell 'not possible'
            # 2) find the rightmost position of 'pre' in arr2  
            j = bisect.bisect_right(arr2, pre)
            # make pre = arr2[j] , just swapping pre i.e instead of arr1[ind] -> arr2[j]
            swap = 1 + dfs(ind + 1 , arr2[j]) if j < len(arr2) else float('inf')
            return min(swap , no_swap)
        
        ans = dfs(0, float('-inf'))
        return ans if ans != float('inf') else -1


# Bisect function in python
# https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/