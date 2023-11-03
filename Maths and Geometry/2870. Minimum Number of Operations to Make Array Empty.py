# Same logic as : "343. Integer break".

# Logic:1) Calculate the frequecny of each element.

# Note: Any number > 1 can be expressed as 'c1*3 + c2*2' where c1,c1 >=0 i.e combination of multiple of '2 and '3'.

# 2) So if freq of any number is < 1 then it on't possible else it is possible to make array empty.
# 3) For getting minimum we will try to get maximum part divisible by '3' i.e 'c1' as big as possible.
# Here comes three cases when we will divide freq by '3', say quotient = q, remainder = r 
# a) freq is divisible by '3' then, for removing that number we will need 'q' no of operations.
# b) freq is not divisible by '3' and r = 1 then we have to split last four frequency like (2 + 2)
# e.g : freq = 7 ,for this min on of operation = (3 + 2 + 2) 
# c) freq is not divisible by '3' and r = 2 then we have to split last five frequency like (3 + 2)
# e.g : freq = 8 ,for this min on of operation = (3 + 3 + 2)

# In both 'b' and 'c case we will require 'q + 1' operation.

# Time = O(n) = space


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0
        for val in freq.values():
            if val < 2:
                return -1
            q, r = divmod(val, 3)
            if r == 0:
                ans += q
            else:
                ans += q + 1
        return ans


# Shortcut and other way of writing above method
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0
        for val in freq.values():
            if val < 2:
                return -1
            ans += ceil(val /3)
        return ans

# Similar Q:
# 2244. Minimum Rounds to Complete All Tasks
# 343. Integer Break
