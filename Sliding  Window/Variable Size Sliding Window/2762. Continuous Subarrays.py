# logic: similar to Q ."713. Subarray Product Less Than K"
# we need to keep track of minimum and max value in each window.
# Reason: If diff between max and min <= 2 then, difference between all the pairs will be <=2.
# Just traverse the array and keep on adding the current ele, and after adding find the valid subarray.

# What to do if invalid?
# We need to remove every ele from left side till we get valid window.

# After getting the valid window, just add the length of valid window to our ans 
# because every combination of that subarray can be part of our ans.

# Time: O(n^2)  , in reality will be less than this.
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        i, j= 0, 0
        hashmap = collections.defaultdict(int)  # [ele : frequency]
        ans = 0
        while j < n:
            hashmap[nums[j]] += 1
            while max(hashmap.keys()) - min(hashmap.keys()) > 2:
                # try to remove the ele from start 
                hashmap[nums[i]] -= 1
                if hashmap[nums[i]] == 0:  # removing the ele from left side
                    del hashmap[nums[i]]
                i += 1
            ans += j - i + 1
            j += 1
        return ans


# Method 2: Better one
# Using two heaps

# Reason: We need to keep track of min and max values so for this we can use two heaps 'minHeap' and 'maxHeap'.
# For knowing the index i.e where to move from left in case of invalid one, 
# we will also store the 'index + 1' with ele value. This will tell where to move for valid one.

# While adding any ele first we will check the valid condition wrt both minimum & max ele till now.
# and keep on poping till you get the valid window wrt both(min and max).
# And keep updating the left pointer i.e 'index' of poped ele.

# At last add cur ele into both the heaps and update the ans.

# Time: O(2*n*logk)    # k= max number of ele we need to remove after each ele

import heapq
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        i, j= 0, 0
        # Heaps will store (nums[j], j). Also storing index so that in case of invalid window we can move directly beyond that index.
        minHeap = []   # to get the minimum ele in cur window
        maxHeap = []   # to get the maximum ele in cur window
        while j < n:
            # find the leftmost position i.e 'i' if we place the cur ele in window
            while minHeap and abs(minHeap[0][0] - nums[j]) > 2:
                num, index = heapq.heappop(minHeap)
                # our window can start only after 'index +1' because we have to remove all those ele from start till we get a valid window
                i = max(i, index + 1)   # since top ele at heaps can have less index value than 'i' so taking maximum.
            # check the same in maxHeap
            while maxHeap and abs(-1* maxHeap[0][0] - nums[j]) > 2:
                num, index = heapq.heappop(maxHeap)
                i = max(i, index + 1)
            # Now push the cur ele into both the heaps with index
            heapq.heappush(minHeap, (nums[j], j))
            heapq.heappush(maxHeap, (-1* nums[j], j))
            # Now update the ans.
            ans += j- i + 1   # just window size only
            j += 1
        return ans

