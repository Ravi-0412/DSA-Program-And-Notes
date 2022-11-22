# my mistake: 
# note: if you do by storing into one variable the max value then it will not work
# since you will remove this ele from max if it will be at 'i'th index
# and then you will left with nothing to compare for next window elements
# the solution of this is above one


# solution: 

# logic: if curr ele is smaller than last ele of  array then simply add this into ans as this can be maximum for upcominmg window
# else: append at last after removing all the smaller than the curr ele i.e agar hmko bda ele mil rha this window ke liye ya upcoming window ke liye to chota wala kyu rakhna

# in this  way it will make sure that max ele for each window will be at first index only since we have poped all the smaller ele
# and when ith index ele is max for any window then pop that from deque 

# since we have to operate on both the right and left in ans array so best data structure comes into mind is "deque" for minimum time complexity
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        de= collections.deque()  
        i,j,ans,n= 0,0,[],len(nums)
        while j<n:
            while de and nums[j]> de[-1]:  # if curr ele is greater than the last elements then pop until you find any ele greater the curr ele
                de.pop()
            de.append(nums[j])   # if smaller or if you find any greater than curr ele then add to the 'de'
            if j+1 >= k:    # or j-i+1== k:
                ans.append(de[0])  # for that subarray first ele of 'deque' will give the ans
                if nums[i]==de[0]:  # before sliding the wind check whether the max ele is at the 'ith' index
                    de.popleft()    # here we have to pop from left since only leftmost was giving the ans
                i+= 1
            j+= 1
        return ans



