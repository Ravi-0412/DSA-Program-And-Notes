# Note: 1) Here duplicate ele can repeat any number of times.
# So sum(nums) - sum_till_n won't work.

# Note : 2) we can reduce this q : "find the element with max frequency".
# We can think logic of 'majority ele' to do this but majority ele logic only works if 'majority ele' exists for sure.
# But here ans_ele can have any freq from 2,3,....till 'n'.
# So this will also don't work.

# Method 1:
# store freq and check if freq > 1

# Method 2: Marking visited value within the array

# Method 3:

# Logic: Since all values of the array are between '1' to 'n' and array size is 'n+1' .
# so index can go from '0' to 'n'.

# How to do?
# While tarversing array say cur_num =  'num' then, mark the ele at index 'num' to its negative value.
# You are just marking to check that you have already visited 'num' before and 
# if you find value at index 'num' negative, it will mean that that number is repeating.
# So 'num' will be our ans only.

# Note : we are modifying array in this method.

# Time = O(n), space = O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num)   # taking abs of 'num' to check value at that index.
                            # because we are modifying the array so later ele may contain negative values.
                            # But index can't be negative.
            if nums[idx] < 0:
                # 'num' index wala ele i.e 'num' only is already visited.
                return idx
            # mark 'num' visited by changing the value at index 'num' to negative value.
            nums[idx] = - nums[idx]


# Mmethod 4:
# using slow and fast pointer.

# How to think?
# The key is to understand how to treat the input array as a linked list.

# Take the array [1,3,4,2] as an example, the index of this
# array is [0,1,2,3], we can map the index to the nums[n]
# i.e 0→1→3→2→4 

# How mapping: 
# index '0' pe kon sa num h (1), '1' index pe kon sa number h '3', '3' index pe kon sa number h '2' ,.......
# till index goes out of bound like linklist.

# take another example
# array : [1,3,4,2,2]
# then it will form linklist like: 0 ->1 ->3 -> 2 -> 4 -> 2 -> 4 .....
# Here you can see cycle starts to repeat from num = 2.

# So now this Q reduces to: "Find the starting node from which cycle starts in linklist".

# Q is based on this logic only.

# Time = O(n), space = O(1)

# Note: Here we are not modifying the array.

# Just same logic :" 142. Linked List Cycle II".

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find whether cycle exist or not , but here it will exist for sure
        # for this , find the intersection point(index) slow and fast
        slow, fast= 0, 0  # we have to start from index '0' only
        while True:
            slow= nums[slow]
            fast= nums[nums[fast]]
            if fast== slow:
                break
        # now fins the starting node of the cycle
        slow1= 0
        while True:
            slow= nums[slow]
            slow1= nums[slow1]
            if slow== slow1:
                return slow