# Observation:
# all left elements must be same only otherwise they can cancel each other.

# Method 1:
# Just keep on cancelling till there is more than 1 distinct ele.
# We will cancel the most frequent ele first to minimise the length.

# In this we only care about freq not indices or element value because we need a pair(distinct ele) to cancel.

# Note: this will work for increasing order array or normal array.

# Time : O(n*logn)
# space = O(n)

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        maxHeap = []
        for value in freq.values():
            heapq.heappush(maxHeap, -1*value)  # we only care about freq not values
        
        # if there is >= 2 element then there is chance of cancellation
        while len(maxHeap) >= 2:
            # pick two most frequent ele remaining. 
            max1 = -1 * heapq.heappop(maxHeap)
            max2 = -1 * heapq.heappop(maxHeap)
            max1 -= 1
            max2 -= 1
            if max1:
                heapq.heappush(maxHeap, -1*max1)
            if max2:
                heapq.heappush(maxHeap, -1*max2)
        return -1*maxHeap[0] if maxHeap else 0
    

# Method 2: Using two pointer
# Optimising taking benefit of sorted array.

# https://leetcode.com/problems/minimum-array-length-after-pair-removals/
# Analyse why other cases won't work.

# Logic:  compare the last element with the element in the middle of the array. If our condition is satisfied, 
# then remove this pair; otherwise, traverse left of the array from the middle to find a smaller element that satisfies our condition for removal.

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)  # Total number of elements in the array.
        mid = n // 2    # The number of elements we want to keep.

        i = n - 1     # Pointer to the end of the array.
        j = mid - 1   # Pointer to the middle of the array. '-1' to get the more smaller element.
        ans = n

        # Iterate from the end of the array towards the middle.
        while j >= 0:
            if nums[i] > nums[j]:
                ans -= 2  # If nums[i] > nums[j], we need to remove two elements.
                i -= 1  # we got smaller ele to cancel nums[i] so decrease 'i'.
            j -= 1   # to find even more smaller if condition doesn't satisfy or if satisfy then find other ele for nums[i]
            
        return ans


# Method 3:
# other way of writing the same logic if we compare start and middle.
# Logic: compare the 1st ele with middle ele and if they satify the condition cancel both.

# Time : O(n)

# Note:Analyse this method properly.

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        i = 0
        j = (n + 1) // 2   # to get more bigger element.
        while i < n //2 and j < n:
            if nums[i] < nums[j]:
                ans -= 2   # cancel that pair so ele remaining will be 'ans-2'.
                i += 1
            j += 1
        return ans


# method 4:
# using hashmap and deep observation
# https://leetcode.com/problems/minimum-array-length-after-pair-removals/solutions/4052092/simple-explanation-with-intuition-c-o-n-time/comments/2075635/

# Logic: 1) if the count of max occuring element is less than n/2 times, 
# then the element can be cancelled by remaining elements 
# (It is given that elements are sorted in non-decreasing order. Hence all remaining elements will be cancelled amongst themselves). 
# In this case, if array size is even, then we say that ans is 0 and 1 incase the array size is odd. 
# Because after cancelling all elements, 1 element is still remaining at the end.

# 2) If the element occurs more than n/2 times, so now it cannot cancel all elements. But it will still cancel all remaining elements.
# How many elements are remaining? 
# The elements remaining are (n - maxi). 
# So elements left are maxi - (n - maxi) = 2*maxi - n;


# time = space = O(n)

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        max_count = max(freq.values())   # frequency of maximum ele in nums
        if max_count *2 < n:
            return n & 1
        return 2 * max_count - n   # max_count - (n - max_count)

