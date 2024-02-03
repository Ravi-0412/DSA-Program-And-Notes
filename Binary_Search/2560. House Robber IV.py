# logic: just similar as we find "kth smallest ele in 2D sorted matrix".
# But reducing inti this form is little tough.

# How? 
# We just need to chose >= k elements and take min(max) of all possibility.
# So if any number has >= k smaller element than him in array that can be our ans,
# But we have to minimum possible such number.

# So Q reduces to "Find the minimum ele say 'ans' from array which has >= k no of smaller ele in array from 'ans'
# when we chose those element non - adjacently ".
# how to solve?
# Ans: for each number in our ans range i.e min(nums) to max(nums) by taking 'mid',
# calculate the number of element <= 'mid' such that no two of them are adjacent.
# if number >= k then means we have found one of the ans so search for even more smaller.
# else increase the range.

# Q. How to find the number of ele which is <= 'mid' such that no two of them are adjacent?
# Ans: we can use greedy i.e then we will see any ele <= mid and if last ele is not taken then we can take the curr ele.

# Reason: we have to count such ele so why to skip if can include them. 
# Here we don't have to maximise or minimkse sum , so we can use greedy.

# time: O(n * logA), A= max(nums) - min(nums)
# Binary Search + Greedy.

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        lastTaken= False

        # Will the number of ele we can pick that have value <= mid such that no two of them are adjacent.
        def noLessThan(mid):
            lastTaken= False
            count= 0
            for num in nums:
                # if pre ele is taken then we can't take this ele so simply skip.
                if lastTaken:
                    lastTaken= False
                    continue
                # if smaller than 'mid', then increase the count.
                if num <= mid:
                    count+= 1
                    lastTaken= True
            return count

        # 2nd Template only
        start, end= min(nums) , max(nums) # our value will lie in this range only.
        while start < end:
            mid= start + (end - start)//2
            # if no of ele we can pick non-adjacent having value <= mid is >= k, then search for even more smaller value.
            if noLessThan(mid) >= k:
                end= mid
            else:  # search for greater one.
                start= mid + 1
        return start
    

